---
id: okf-structure/concepts/services-networking/dual-stack.md#configure-ipv4-ipv6-dual-stack
kind: section
title: Configure IPv4/IPv6 dual-stack
source: concepts/services-networking/dual-stack.md
url: https://kubernetes.io/docs/concepts/services-networking/dual-stack/
heading: Configure IPv4/IPv6 dual-stack
parent: okf-structure/concepts/services-networking/dual-stack
children: []
prev_sibling: okf-structure/concepts/services-networking/dual-stack.md#prerequisites
next_sibling: okf-structure/concepts/services-networking/dual-stack.md#services
word_count: 140
---

To configure IPv4/IPv6 dual-stack, set dual-stack cluster network assignments:

* kube-apiserver:
  * `--service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>`
* kube-controller-manager:
  * `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>`
  * `--service-cluster-ip-range=<IPv4 CIDR>,<IPv6 CIDR>`
  * `--node-cidr-mask-size-ipv4|--node-cidr-mask-size-ipv6` defaults to /24 for IPv4 and /64 for IPv6
* kube-proxy:
  * `--cluster-cidr=<IPv4 CIDR>,<IPv6 CIDR>`
* kubelet:
  * `--node-ip=<IPv4 IP>,<IPv6 IP>`
    * This option is required for bare metal dual-stack nodes (nodes that do not define a
      cloud provider with the `--cloud-provider` flag). If you are using a cloud provider
      and choose to override the node IPs chosen by the cloud provider, set the
      `--node-ip` option.
    * (The legacy built-in cloud providers do not support dual-stack `--node-ip`.)

An example of an IPv4 CIDR: `10.244.0.0/16` (though you would supply your own address range)

An example of an IPv6 CIDR: `fdXY:IJKL:MNOP:15::/64` (this shows the format but is not a valid
address - see RFC 4193)
