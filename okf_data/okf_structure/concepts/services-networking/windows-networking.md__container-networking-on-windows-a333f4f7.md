---
id: okf-structure/concepts/services-networking/windows-networking.md#container-networking-on-windows-networking
kind: section
title: Container networking on Windows {#networking}
source: concepts/services-networking/windows-networking.md
url: https://kubernetes.io/docs/concepts/services-networking/windows-networking/
heading: Container networking on Windows {#networking}
parent: okf-structure/concepts/services-networking/windows-networking
children: []
prev_sibling: okf-structure/concepts/services-networking/windows-networking.md#introduction
next_sibling: okf-structure/concepts/services-networking/windows-networking.md#network-modes
word_count: 221
---

Networking for Windows containers is exposed through
CNI plugins.
Windows containers function similarly to virtual machines in regards to
networking. Each container has a virtual network adapter (vNIC) which is connected
to a Hyper-V virtual switch (vSwitch). The Host Networking Service (HNS) and the
Host Compute Service (HCS) work together to create containers and attach container
vNICs to networks. HCS is responsible for the management of containers whereas HNS
is responsible for the management of networking resources such as:

* Virtual networks (including creation of vSwitches)
* Endpoints / vNICs
* Namespaces
* Policies including packet encapsulations, load-balancing rules, ACLs, and NAT rules.

The Windows HNS and vSwitch implement namespacing and can
create virtual NICs as needed for a pod or container. However, many configurations such
as DNS, routes, and metrics are stored in the Windows registry database rather than as
files inside `/etc`, which is how Linux stores those configurations. The Windows registry for the container
is separate from that of the host, so concepts like mapping `/etc/resolv.conf` from
the host into a container don't have the same effect they would on Linux. These must
be configured using Windows APIs run in the context of that container. Therefore
CNI implementations need to call the HNS instead of relying on file mappings to pass
network details into the pod or container.
