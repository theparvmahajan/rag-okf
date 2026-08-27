---
id: okf-structure/concepts/services-networking/windows-networking.md#limitations
kind: section
title: Limitations
source: concepts/services-networking/windows-networking.md
url: https://kubernetes.io/docs/concepts/services-networking/windows-networking/
heading: Limitations
parent: okf-structure/concepts/services-networking/windows-networking
children: []
prev_sibling: okf-structure/concepts/services-networking/windows-networking.md#load-balancing-and-services
next_sibling: null
word_count: 244
---

The following networking functionality is _not_ supported on Windows nodes:

* Host networking mode
* Local NodePort access from the node itself (works for other nodes or external clients)
* More than 64 backend pods (or unique destination addresses) for a single Service
* IPv6 communication between Windows pods connected to overlay networks
* Local Traffic Policy in non-DSR mode
* Outbound communication using the ICMP protocol via the `win-overlay`, `win-bridge`, or using the Azure-CNI plugin.
  Specifically, the Windows data plane (VFP)
  doesn't support ICMP packet transpositions, and this means:
  * ICMP packets directed to destinations within the same network (such as pod to pod communication via ping) 
    work as expected;
  * TCP/UDP packets work as expected;
  * ICMP packets directed to pass through a remote network (e.g. pod to external internet communication via ping) 
    cannot be transposed and thus will not be routed back to their source;
  * Since TCP/UDP packets can still be transposed, you can substitute `ping <destination>` with
    `curl <destination>` when debugging connectivity with the outside world.

Other limitations:

* Windows reference network plugins win-bridge and win-overlay do not implement
  CNI spec v0.4.0,
  due to a missing `CHECK` implementation.
* The Flannel VXLAN CNI plugin has the following limitations on Windows:
  * Node-pod connectivity is only possible for local pods with Flannel v0.12.0 (or higher).
  * Flannel is restricted to using VNI 4096 and UDP port 4789. See the official
    Flannel VXLAN
    backend docs for more details on these parameters.
