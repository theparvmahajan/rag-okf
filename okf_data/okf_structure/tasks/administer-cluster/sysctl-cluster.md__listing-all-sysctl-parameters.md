---
id: okf-structure/tasks/administer-cluster/sysctl-cluster.md#listing-all-sysctl-parameters
kind: section
title: Listing all Sysctl Parameters
source: tasks/administer-cluster/sysctl-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/
heading: Listing all Sysctl Parameters
parent: okf-structure/tasks/administer-cluster/sysctl-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#safe-and-unsafe-sysctls
word_count: 75
---

In Linux, the sysctl interface allows an administrator to modify kernel
parameters at runtime. Parameters are available via the `/proc/sys/` virtual
process file system. The parameters cover various subsystems such as:

- kernel (common prefix: `kernel.`)
- networking (common prefix: `net.`)
- virtual memory (common prefix: `vm.`)
- MDADM (common prefix: `dev.`)
- More subsystems are described in Kernel docs.

To get a list of all parameters, you can run

```shell
sudo sysctl -a
```
