---
id: okf-structure/concepts/architecture/cgroups.md#using-cgroup-v2-using-cgroupv2
kind: section
title: Using cgroup v2 {#using-cgroupv2}
source: concepts/architecture/cgroups.md
url: https://kubernetes.io/docs/concepts/architecture/cgroups/
heading: Using cgroup v2 {#using-cgroupv2}
parent: okf-structure/concepts/architecture/cgroups
children: []
prev_sibling: okf-structure/concepts/architecture/cgroups.md#what-is-cgroup-v2-cgroup-v2
next_sibling: okf-structure/concepts/architecture/cgroups.md#identify-the-cgroup-version-on-linux-nodes-check-cgroup-version
word_count: 529
---

The recommended way to use cgroup v2 is to use a Linux distribution that
enables and uses cgroup v2 by default.

To check if your distribution uses cgroup v2, refer to Identify cgroup version on Linux nodes.

### Requirements

cgroup v2 has the following requirements:

* OS distribution enables cgroup v2
* Linux Kernel version is 5.8 or later
* Container runtime supports cgroup v2. For example:
  * containerd v1.4 and later
  * cri-o v1.20 and later
* The kubelet and the container runtime are configured to use the systemd cgroup driver

### Linux Distribution cgroup v2 support

For a list of Linux distributions that use cgroup v2, refer to the cgroup v2 documentation

* Container Optimized OS (since M97)
* Ubuntu (since 21.10, 22.04+ recommended)
* Debian GNU/Linux (since Debian 11 bullseye)
* Fedora (since 31)
* Arch Linux (since April 2021)
* RHEL and RHEL-like distributions (since 9)

To check if your distribution is using cgroup v2, refer to your distribution's
documentation or follow the instructions in Identify the cgroup version on Linux nodes.

You can also enable cgroup v2 manually on your Linux distribution by modifying
the kernel cmdline boot arguments. If your distribution uses GRUB,
`systemd.unified_cgroup_hierarchy=1` should be added in `GRUB_CMDLINE_LINUX`
under `/etc/default/grub`, followed by `sudo update-grub`.  However, the
recommended approach is to use a distribution that already enables cgroup v2 by
default.

### Migrating to cgroup v2 {#migrating-cgroupv2}

To migrate to cgroup v2, ensure that you meet the requirements, then upgrade
to a kernel version that enables cgroup v2 by default.

The kubelet automatically detects that the OS is running on cgroup v2 and
performs accordingly with no additional configuration required.

There should not be any noticeable difference in the user experience when
switching to cgroup v2, unless users are accessing the cgroup file system
directly, either on the node or from within the containers.

cgroup v2 uses a different API than cgroup v1, so if there are any
applications that directly access the cgroup file system, they need to be
updated to newer versions that support cgroup v2. For example:

* Some third-party monitoring and security agents may depend on the cgroup filesystem.
 Update these agents to versions that support cgroup v2.
* If you run cAdvisor as a stand-alone
 DaemonSet for monitoring pods and containers, update it to v0.43.0 or later.
* If you deploy Java applications, prefer to use versions which fully support cgroup v2:
    * OpenJDK / HotSpot: jdk8u372, 11.0.16, 15 and later
    * IBM Semeru Runtimes: 8.0.382.0, 11.0.20.0, 17.0.8.0, and later
    * IBM Java: 8.0.8.6 and later
* If you are using the uber-go/automaxprocs package, make sure
  the version you use is v1.5.1 or higher.
* If you deploy Node.js applications, prefer to use versions that detect cgroup v2
  memory limits. Node.js reads cgroup v2 memory limits (through libuv)
  starting with Node.js v20.3.0. The v18 release line does not reliably detect cgroup v2 memory limits.
  Versions without this support may read the host's total memory instead of the
  limit applied to the pod, which can lead to an incorrectly sized heap and out-of-memory (OOM)
  terminations. On affected versions, set the heap size explicitly, for example with the
  `--max-old-space-size` flag.
