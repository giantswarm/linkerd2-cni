# linkerd2-cni

Linkerd is a *service mesh*, designed to give platform-wide observability,
reliability, and security without requiring configuration or code changes. The
Linkerd [CNI plugin](https://linkerd.io/2/features/cni/) takes care of setting
up your pod's network so  incoming and outgoing traffic is proxied through the
data plane.

## Requirements

Kubernetes: `>=1.13.0-0`

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cniPluginImage | string | `"ghcr.io/linkerd/cni-plugin"` | Docker image for the CNI plugin |
| cniPluginVersion | string | `"linkerdVersionValue"` | Tag for the CNI container Docker image |
| cniResourceLabel | string | `"linkerd.io/cni-resource"` | CNI resource annotation. Do not edit |
| createdByAnnotation | string | `"linkerd.io/created-by"` | Annotation label for the proxy create. Do not edit.  |
| destCNIBinDir | string | `"/opt/cni/bin"` | Directory on the host where the CNI configuration will be placed |
| destCNINetDir | string | `"/etc/cni/net.d"` | Directory on the host where the CNI plugin binaries reside  |
| ignoreInboundPorts | string | `"25,443,587,3306,11211"` | Inbound ports the proxy should ignore - SMTP (25,587) server-first - HTTPS (443) opaque TLS - MYSQL (3306) server-first - Memcached (11211) clients do not issue any preamble, which breaks detection |
| ignoreOutboundPorts | string | `"25,443,587,3306,11211"` | Outbound ports the proxy should ignore |
| imagePullSecrets | string | `nil` |  |
| inboundProxyPort | int | `4143` | Inbound port for the proxy container |
| installNamespace | bool | `true` | Whether to create the CNI plugin plane namespace or not  |
| logLevel | string | `"info"` | Log level for the CNI plugin |
| namespace | string | `"linkerd-cni"` | CNI plugin plane namespace |
| outboundProxyPort | int | `4140` | Outbound port for the proxy container |
| portsToRedirect | string | `""` | Ports to redirect to proxy  |
| priorityClassName | string | `""` | Kubernetes priorityClassName for the CNI plugin's Pods |
| proxyInjectAnnotation | string | `"linkerd.io/inject"` |  |
| proxyInjectDisabled | string | `"disabled"` |  |
| proxyUID | int | `2102` | User id under which the proxy shall be ran |
| useWaitFlag | bool | `false` | Configures the CNI plugin to use the -w flag for the iptables command |

