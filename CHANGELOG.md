# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Update pytest-helm-charts from beta to [v0.7.0](https://github.com/giantswarm/pytest-helm-charts/blob/master/CHANGELOG.md) ([#68](https://github.com/giantswarm/linkerd2-cni-app/pull/68))
- Add Giant Swarm team label to resources.

## [0.7.0] - 2022-05-12

### Added

- Set team annotation in Chart.yaml for alert routing.

### Changed

- Align with and upgrade to upstream `stable-2.11.2`. ([#59](https://github.com/giantswarm/linkerd2-cni-app/pull/59))

## [0.4.0] - 2021-07-29

### Changed

- Align with and upgrade to upstream `stable-2.10.2`. ([#28](https://github.com/giantswarm/linkerd2-cni-app/pull/28))
- First release published to the `giantswarm` catalog.

## [0.2.1] - 2020-12-16

### Changed

- Upddate missed `appVersion` in Chart.yaml. ([#16](https://github.com/giantswarm/linkerd2-cni-app/pull/16))

## [0.2.0] - 2020-12-16

### Changed

- Bump CNI image to `stable-2.9.1`. ([#7](https://github.com/giantswarm/linkerd2-cni-app/pull/7))
- Use Giant Swarm image repository. ([#13](https://github.com/giantswarm/linkerd2-cni-app/pull/13))

### Fixed

- Correct indentation in pod spec. ([#6](https://github.com/giantswarm/linkerd2-cni-app/pull/6))

## [0.1.0] - 2020-12-03

[Unreleased]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.7.0...HEAD
[0.7.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.4.0...v0.7.0
[0.4.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.2.1...v0.4.0
[0.2.1]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/giantswarm/linkerd2-cni-app/releases/tag/v0.1.0
