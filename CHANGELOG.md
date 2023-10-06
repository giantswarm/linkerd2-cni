# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Upgrade ATS to 0.4.1 and its python deps.

## [1.2.0] - 2023-10-05

### Changed

- Add PSS flag for PSP->PSS migration.

## [1.1.0] - 2023-08-29

### Changed

- Upgrade to linkerd 2.13.6

## [1.0.0] - 2023-06-13

### Changed

- Upgrade to linkerd 2.13.4

## [0.10.0] - 2023-03-09

### Changed

- Upgrade to linkerd 2.12.4

## [0.9.0] - 2023-03-07

### Added

- Add icon url to chart

### Changed

- Changes linkerd CNI priority class to "giantswarm-critical" to improve scheduling.

## [0.8.0] - 2022-10-27

### Changed

- Bumped version 2.12.2 ([#87](https://github.com/giantswarm/linkerd2-cni-app/pull/87)).
- App renamed to `linkerd2-cni`.
- Moved partials as a subchart of linkerd2-cni-app and bumped version to 2.12.1 using vendir.

## [0.7.4] - 2022-08-25

Skipping 0.7.3 to align with linkerd2-app version

### Changed

- Align with upstream version `stable-2.11.4`. [No changes](https://github.com/linkerd/linkerd2/blob/stable-2.11.4/CHANGES.md#stable-2114) of the cni-plugin actuallly.

## [0.7.2] - 2022-08-03

Skipping 0.7.1 to re-align with linkerd2-app version

### Changed

- Update pytest-helm-charts from beta to [v0.7.0](https://github.com/giantswarm/pytest-helm-charts/blob/main/CHANGELOG.md) ([#68](https://github.com/giantswarm/linkerd2-cni-app/pull/68))
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

[Unreleased]: https://github.com/giantswarm/linkerd2-cni-app/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.10.0...v1.0.0
[0.10.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.7.4...v0.8.0
[0.7.4]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.7.2...v0.7.4
[0.7.2]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.7.0...v0.7.2
[0.7.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.4.0...v0.7.0
[0.4.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.2.1...v0.4.0
[0.2.1]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/giantswarm/linkerd2-cni-app/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/giantswarm/linkerd2-cni-app/releases/tag/v0.1.0
