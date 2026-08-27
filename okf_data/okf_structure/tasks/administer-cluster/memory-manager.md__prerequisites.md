---
id: okf-structure/tasks/administer-cluster/memory-manager.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#how-does-the-memory-manager-operate
word_count: 113
---

If you are running an older version of Kubernetes, check the documentation
for the version of Kubernetes you are running.

### Resource alignment prerequisites

To align memory resources with other requested resources in a Pod spec:

- the CPU Manager should be enabled and proper CPU Manager policy should be configured on a Node.
  See control CPU Management Policies;
- the Topology Manager should be enabled and proper Topology Manager policy should be configured on a Node.
  See control Topology Management Policies.

### Windows support

Windows support can be enabled via the `WindowsCPUAndMemoryAffinity` feature gate
and it requires support in the container runtime.  
Only the None and BestEffort policies are supported on Windows.
