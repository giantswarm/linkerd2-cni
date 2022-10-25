import json
import logging
import os
import requests
import shutil
import subprocess  # nosec
import time
from typing import Dict

import pykube
import pytest
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.utils import wait_for_objects_condition
from pytest_helm_charts.giantswarm_app_platform.app import AppCR

logger = logging.getLogger(__name__)

app_name = "linkerd2-cni"
namespace_name = "linkerd-cni"
catalog_name = "chartmuseum"

timeout: int = 360


def get_linkerd_cli(version):
    url = f"https://github.com/linkerd/linkerd2/releases/download/{version}/linkerd2-cli-{version}-linux-amd64"
    local_filename = "linkerd-cli"
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    os.chmod(local_filename, 0o755)


def exec_linkerd_cli(kube_config_path, namespace):
    result = subprocess.run(
        [
            "./linkerd-cli",
            "--kubeconfig", kube_config_path,
            "--cni-namespace", namespace,
            "check", "--pre",
            "--linkerd-cni-enabled",
            "--output", "json",
        ],
        check=False,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    ).stdout

    return json.loads(result)


def _app_deployed(app: AppCR) -> bool:
    complete = (
        "status" in app.obj
        and "release" in app.obj["status"]
        and "appVersion" in app.obj["status"]
        and "status" in app.obj["status"]["release"]
        and app.obj["status"]["release"]["status"] == "deployed"
    )
    return complete


@pytest.fixture(scope="module")
def app_cr(kube_cluster, chart_version):
    app = {
       "kind": "App",
       "apiVersion": "application.giantswarm.io/v1alpha1",
       "metadata": {
          "name": app_name,
          "namespace": "giantswarm",
          "labels": {
              "app-operator.giantswarm.io/version": "0.0.0"
          }
       },
       "spec": {
          "catalog": catalog_name,
          "kubeConfig": {
             "inCluster": True
          },
          "name": app_name,
          "namespace": namespace_name,
          "namespaceConfig": {
             "annotations": {
                "linkerd.io/inject": "disabled"
             },
             "labels": {
                "linkerd.io/cni-resource": "true",
                "config.linkerd.io/admission-webhooks": "disabled"
             }
          },
          "version": chart_version
       }
    }
    app_obj = AppCR(kube_cluster.kube_client, app)
    app_obj.create()
    time.sleep(5)
    apps = wait_for_objects_condition(
        kube_cluster.kube_client,
        AppCR,
        [app_name],
        "giantswarm",
        _app_deployed,
        timeout,
        False
    )
    return apps[0]


@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """
    Test if the kubernetes api works
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1


@pytest.mark.smoke
def test_cluster_info(
    kube_cluster: Cluster, cluster_type: str, chart_extra_info: Dict[str, str]
) -> None:
    """Test if the culster_info is available"""
    logger.info(f"Running on cluster type {cluster_type}")
    key = "external_cluster_type"
    if key in chart_extra_info:
        logger.info(f"{key} is {chart_extra_info[key]}")
    assert kube_cluster.kube_client is not None
    assert cluster_type != ""


@pytest.mark.smoke
def test_installation(kube_cluster: Cluster, app_cr: AppCR):
    """Test using the linkerd cli using 'check --pre'"""
    app_version = app_cr.obj["status"]["appVersion"]
    logger.info(f"Installed App CR shows installed appVersion {app_version}")

    get_linkerd_cli(app_version)

    curr = 0
    while curr < timeout:
        success = exec_linkerd_cli(kube_cluster.kube_config_path, namespace_name)["success"]
        if success:
            break
        time.sleep(1)

    cli_output = exec_linkerd_cli(kube_cluster.kube_config_path, namespace_name)

    logger.info(f"Final output of 'linkerd check --pre`: {cli_output}")

    assert cli_output["success"]
