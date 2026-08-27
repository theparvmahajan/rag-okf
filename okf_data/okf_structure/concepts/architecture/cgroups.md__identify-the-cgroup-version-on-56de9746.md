---
id: okf-structure/concepts/architecture/cgroups.md#identify-the-cgroup-version-on-linux-nodes-check-cgroup-version
kind: section
title: Identify the cgroup version on Linux Nodes  {#check-cgroup-version}
source: concepts/architecture/cgroups.md
url: https://kubernetes.io/docs/concepts/architecture/cgroups/
heading: Identify the cgroup version on Linux Nodes  {#check-cgroup-version}
parent: okf-structure/concepts/architecture/cgroups
children: []
prev_sibling: okf-structure/concepts/architecture/cgroups.md#using-cgroup-v2-using-cgroupv2
next_sibling: okf-structure/concepts/architecture/cgroups.md#deprecation-of-cgroup-v1
word_count: 57
---

The cgroup version depends on the Linux distribution being used and the
default cgroup version configured on the OS. To check which cgroup version your
distribution uses, run the `stat -fc %T /sys/fs/cgroup/` command on
the node:

```shell
stat -fc %T /sys/fs/cgroup/
```

For cgroup v2, the output is `cgroup2fs`.

For cgroup v1, the output is `tmpfs.`
