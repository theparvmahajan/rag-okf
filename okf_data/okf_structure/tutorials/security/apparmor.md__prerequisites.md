---
id: okf-structure/tutorials/security/apparmor.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/security/apparmor.md
url: https://kubernetes.io/docs/tutorials/security/apparmor/
heading: Prerequisites
parent: okf-structure/tutorials/security/apparmor
children: []
prev_sibling: okf-structure/tutorials/security/apparmor.md#objectives
next_sibling: okf-structure/tutorials/security/apparmor.md#securing-a-pod
word_count: 224
---

AppArmor is an optional kernel module and Kubernetes feature, so verify it is supported on your
Nodes before proceeding:

1. AppArmor kernel module is enabled -- For the Linux kernel to enforce an AppArmor profile, the
   AppArmor kernel module must be installed and enabled. Several distributions enable the module by
   default, such as Ubuntu and SUSE, and many others provide optional support. To check whether the
   module is enabled, check the `/sys/module/apparmor/parameters/enabled` file:

   ```shell
   cat /sys/module/apparmor/parameters/enabled
   Y
   ```

   The kubelet verifies that AppArmor is enabled on the host before admitting a pod with AppArmor
   explicitly configured.

1. Container runtime supports AppArmor -- All common Kubernetes-supported container
   runtimes should support AppArmor, including containerd and
   cri o. Please refer to the corresponding runtime
   documentation and verify that the cluster fulfills the requirements to use AppArmor.

1. Profile is loaded -- AppArmor is applied to a Pod by specifying an AppArmor profile that each
   container should be run with. If any of the specified profiles are not loaded in the
   kernel, the kubelet will reject the Pod. You can view which profiles are loaded on a
   node by checking the `/sys/kernel/security/apparmor/profiles` file. For example:

   ```shell
   ssh gke-test-default-pool-239f5d02-gyn2 "sudo cat /sys/kernel/security/apparmor/profiles | sort"
   ```
   ```
   apparmor-test-deny-write (enforce)
   apparmor-test-audit-write (enforce)
   docker-default (enforce)
   k8s-nginx (enforce)
   ```

   For more details on loading profiles on nodes, see
   Setting up nodes with profiles.
