---
id: okf-structure/concepts/windows/intro.md#container-runtimes-container-runtime
kind: section
title: Container runtimes {#container-runtime}
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Container runtimes {#container-runtime}
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#pause-container
next_sibling: okf-structure/concepts/windows/intro.md#windows-os-version-compatibility-windows-os-version-support
word_count: 104
---

You need to install a
container runtime
into each node in the cluster so that Pods can run there.

The following container runtimes work with Windows:

### ContainerD

You can use ContainerD 1.4.0+
as the container runtime for Kubernetes nodes that run Windows.

Learn how to install ContainerD on a Windows node.

There is a known limitation
when using GMSA with containerd to access Windows network shares, which requires a
kernel patch.

### Mirantis Container Runtime {#mcr}

Mirantis Container Runtime (MCR)
is available as a container runtime for all Windows Server 2019 and later versions.

See Install MCR on Windows Servers for more information.
