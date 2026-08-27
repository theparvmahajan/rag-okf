---
id: okf-structure/setup/production-environment/container-runtimes.md#install-and-configure-prerequisites
kind: section
title: Install and configure prerequisites
source: setup/production-environment/container-runtimes.md
url: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
heading: Install and configure prerequisites
parent: okf-structure/setup/production-environment/container-runtimes
children: []
prev_sibling: okf-structure/setup/production-environment/container-runtimes.md#introduction
next_sibling: okf-structure/setup/production-environment/container-runtimes.md#cgroup-drivers
word_count: 119
---

### Network configuration

By default, the Linux kernel does not allow IPv4 packets to be routed
between interfaces. Most Kubernetes cluster networking implementations
will change this setting (if needed), but some might expect the
administrator to do it for them. (Some might also expect other sysctl
parameters to be set, kernel modules to be loaded, etc; consult the
documentation for your specific network implementation.)

### Enable IPv4 packet forwarding {#prerequisite-ipv4-forwarding-optional}

To manually enable IPv4 packet forwarding:

```bash
# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

Verify that `net.ipv4.ip_forward` is set to 1 with:

```bash
sysctl net.ipv4.ip_forward
```
