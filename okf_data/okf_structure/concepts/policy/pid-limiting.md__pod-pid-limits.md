---
id: okf-structure/concepts/policy/pid-limiting.md#pod-pid-limits
kind: section
title: Pod PID limits
source: concepts/policy/pid-limiting.md
url: https://kubernetes.io/docs/concepts/policy/pid-limiting/
heading: Pod PID limits
parent: okf-structure/concepts/policy/pid-limiting
children: []
prev_sibling: okf-structure/concepts/policy/pid-limiting.md#node-pid-limits
next_sibling: okf-structure/concepts/policy/pid-limiting.md#pid-based-eviction
word_count: 64
---

Kubernetes allows you to limit the number of processes running in a Pod. You
specify this limit at the node level, rather than configuring it as a resource
limit for a particular Pod. Each Node can have a different PID limit.  
To configure the limit, you can specify the command line parameter `--pod-max-pids`
to the kubelet, or set `PodPidsLimit` in the kubelet
configuration file.
