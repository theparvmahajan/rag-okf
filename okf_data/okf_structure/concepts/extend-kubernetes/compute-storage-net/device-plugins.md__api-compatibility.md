---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#api-compatibility
kind: section
title: API compatibility
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: API compatibility
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-deployment
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#monitoring-device-plugin-resources
word_count: 188
---

Previously, the versioning scheme required the Device Plugin's API version to match
exactly the Kubelet's version. Since the graduation of this feature to Beta in v1.12
this is no longer a hard requirement. The API is versioned and has been stable since
Beta graduation of this feature. Because of this, kubelet upgrades should be seamless
but there still may be changes in the API before stabilization making upgrades not
guaranteed to be non-breaking.

Although the Device Manager component of Kubernetes is a generally available feature,
the _device plugin API_ is not stable. For information on the device plugin API and
version compatibility, read Device Plugin API versions.

As a project, Kubernetes recommends that device plugin developers:

* Watch for Device Plugin API changes in the future releases.
* Support multiple versions of the device plugin API for backward/forward compatibility.

To run device plugins on nodes that need to be upgraded to a Kubernetes release with
a newer device plugin API version, upgrade your device plugins to support both versions
before upgrading these nodes. Taking that approach will ensure the continuous functioning
of the device allocations during the upgrade.
