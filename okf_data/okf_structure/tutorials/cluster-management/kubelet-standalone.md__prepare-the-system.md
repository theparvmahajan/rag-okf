---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prepare-the-system
kind: section
title: Prepare the system
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Prepare the system
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prerequisites
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#download-install-and-configure-the-components
word_count: 244
---

### Swap configuration

By default, kubelet fails to start if swap memory is detected on a node.
This means that swap should either be disabled or tolerated by kubelet.

If you configure the kubelet to tolerate swap, the kubelet still configures Pods (and the
containers in those Pods) not to use swap space. To find out how Pods can actually
use the available swap, you can read more about
swap memory management on Linux nodes.

If you have swap memory enabled, either disable it or add `failSwapOn: false` to the
kubelet configuration file.

To check if swap is enabled:

```shell
sudo swapon --show
```

If there is no output from the command, then swap memory is already disabled.

To disable swap temporarily:

```shell
sudo swapoff -a
```

To make this change persistent across reboots:

Make sure swap is disabled in either `/etc/fstab` or `systemd.swap`, depending on how it was
configured on your system.

### Enable IPv4 packet forwarding

To check if IPv4 packet forwarding is enabled:

```shell
cat /proc/sys/net/ipv4/ip_forward
```

If the output is `1`, it is already enabled. If the output is `0`, then follow next steps.

To enable IPv4 packet forwarding, create a configuration file that sets the
`net.ipv4.ip_forward` parameter to `1`:

```shell
sudo tee /etc/sysctl.d/k8s.conf <<EOF
net.ipv4.ip_forward = 1
EOF
```

Apply the changes to the system:

```shell
sudo sysctl --system
```

The output is similar to:

```
...
* Applying /etc/sysctl.d/k8s.conf ...
net.ipv4.ip_forward = 1
* Applying /etc/sysctl.conf ...
```
