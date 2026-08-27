---
id: okf-structure/concepts/extend-kubernetes/_index.md#infrastructure-extensions
kind: section
title: Infrastructure extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: Infrastructure extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#api-access-extensions
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#scheduling-extensions
word_count: 274
---

### Device plugins

_Device plugins_ allow a node to discover new Node resources (in addition to the
builtin ones like cpu and memory) via a
Device Plugin.

### Storage plugins

Container Storage Interface (CSI) plugins provide
a way to extend Kubernetes with supports for new kinds of volumes. The volumes can be backed by
durable external storage, or provide ephemeral storage, or they might offer a read-only interface
to information using a filesystem paradigm.

Kubernetes also includes support for FlexVolume plugins,
which are deprecated since Kubernetes v1.23 (in favour of CSI).

FlexVolume plugins allow users to mount volume types that aren't natively supported by Kubernetes. When
you run a Pod that relies on FlexVolume storage, the kubelet calls a binary plugin to mount the volume.
The archived FlexVolume
design proposal has more detail on this approach.

The Kubernetes Volume Plugin FAQ for Storage Vendors
includes general information on storage plugins.

### Network plugins

Your Kubernetes cluster needs a _network plugin_ in order to have a working Pod network
and to support other aspects of the Kubernetes network model.

Network Plugins
allow Kubernetes to work with different networking topologies and technologies.

### Kubelet image credential provider plugins

Kubelet image credential providers are plugins for the kubelet to dynamically retrieve image registry
credentials. The credentials are then used when pulling images from container image registries that
match the configuration.

The plugins can communicate with external services or use local files to obtain credentials. This way,
the kubelet does not need to have static credentials for each registry, and can support various
authentication methods and protocols.

For plugin configuration details, see
Configure a kubelet image credential provider.
