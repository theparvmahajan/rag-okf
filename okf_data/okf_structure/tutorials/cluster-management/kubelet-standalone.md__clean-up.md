---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#clean-up
kind: section
title: Clean up
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Clean up
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#where-to-look-for-more-details
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#conclusion
word_count: 88
---

### kubelet

```shell
sudo systemctl disable --now kubelet.service
sudo systemctl daemon-reload
sudo rm /etc/systemd/system/kubelet.service
sudo rm /usr/bin/kubelet
sudo rm -rf /etc/kubernetes
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/log/containers
sudo rm -rf /var/log/pods
```

### Container Runtime

```shell
sudo systemctl disable --now crio.service
sudo systemctl daemon-reload
sudo rm -rf /usr/local/bin
sudo rm -rf /usr/local/lib
sudo rm -rf /usr/local/share
sudo rm -rf /usr/libexec/crio
sudo rm -rf /etc/crio
sudo rm -rf /etc/containers
```

### Network Plugins

```shell
sudo rm -rf /opt/cni
sudo rm -rf /etc/cni
sudo rm -rf /var/lib/cni
```
