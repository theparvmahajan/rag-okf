---
id: okf-structure/tasks/administer-cluster/cpu-management-policies.md#introduction
kind: section
title: Control CPU Management Policies on the Node
source: tasks/administer-cluster/cpu-management-policies.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/
heading: null
parent: okf-structure/tasks/administer-cluster/cpu-management-policies
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#prerequisites
word_count: 89
---

Kubernetes keeps many aspects of how pods execute on nodes abstracted
from the user. This is by design.  However, some workloads require
stronger guarantees in terms of latency and/or performance in order to operate
acceptably. The kubelet provides methods to enable more complex workload
placement policies while keeping the abstraction free from explicit placement
directives.

For detailed information on resource management, please refer to the
Resource Management for Pods and Containers
documentation.

For detailed information on how the kubelet implements resource management, please refer to the
Node ResourceManagers documentation.
