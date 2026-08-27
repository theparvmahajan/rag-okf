---
id: okf-structure/concepts/policy/pid-limiting.md#node-pid-limits
kind: section
title: Node PID limits
source: concepts/policy/pid-limiting.md
url: https://kubernetes.io/docs/concepts/policy/pid-limiting/
heading: Node PID limits
parent: okf-structure/concepts/policy/pid-limiting
children: []
prev_sibling: okf-structure/concepts/policy/pid-limiting.md#introduction
next_sibling: okf-structure/concepts/policy/pid-limiting.md#pod-pid-limits
word_count: 60
---

Kubernetes allows you to reserve a number of process IDs for the system use. To
configure the reservation, use the parameter `pid=<number>` in the
`--system-reserved` and `--kube-reserved` command line options to the kubelet.
The value you specified declares that the specified number of process IDs will
be reserved for the system as a whole and for Kubernetes system daemons
respectively.
