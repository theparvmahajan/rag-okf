---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-deployment
kind: section
title: Device plugin deployment
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: Device plugin deployment
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-implementation
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#api-compatibility
word_count: 94
---

You can deploy a device plugin as a DaemonSet, as a package for your node's operating system,
or manually.

The canonical directory `/var/lib/kubelet/device-plugins` (which is hardcoded on the kubelet) requires privileged access,
so a device plugin must run in a privileged security context.
If you're deploying a device plugin as a DaemonSet, `/var/lib/kubelet/device-plugins`
must be mounted as a volume
in the plugin's PodSpec.

If you choose the DaemonSet approach you can rely on Kubernetes to: place the device plugin's
Pod onto Nodes, to restart the daemon Pod after failure, and to help automate upgrades.
