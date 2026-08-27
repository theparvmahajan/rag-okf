---
id: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#install-the-weave-net-addon
kind: section
title: Install the Weave Net addon
source: tasks/administer-cluster/network-policy-provider/weave-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/
heading: Install the Weave Net addon
parent: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#test-the-installation
word_count: 45
---

Follow the Integrating Kubernetes via the Addon guide.

The Weave Net addon for Kubernetes comes with a
Network Policy Controller
that automatically monitors Kubernetes for any NetworkPolicy annotations on all
namespaces and configures `iptables` rules to allow or block traffic as directed by the policies.
