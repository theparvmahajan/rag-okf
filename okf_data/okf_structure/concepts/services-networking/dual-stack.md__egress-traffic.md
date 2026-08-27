---
id: okf-structure/concepts/services-networking/dual-stack.md#egress-traffic
kind: section
title: Egress traffic
source: concepts/services-networking/dual-stack.md
url: https://kubernetes.io/docs/concepts/services-networking/dual-stack/
heading: Egress traffic
parent: okf-structure/concepts/services-networking/dual-stack
children: []
prev_sibling: okf-structure/concepts/services-networking/dual-stack.md#services
next_sibling: okf-structure/concepts/services-networking/dual-stack.md#windows-support
word_count: 64
---

If you want to enable egress traffic in order to reach off-cluster destinations (eg. the public
Internet) from a Pod that uses non-publicly routable IPv6 addresses, you need to enable the Pod to
use a publicly routed IPv6 address via a mechanism such as transparent proxying or IP
masquerading. The ip-masq-agent project
supports IP masquerading on dual-stack clusters.

Ensure your CNI provider supports IPv6.
