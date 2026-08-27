---
id: okf-structure/tasks/administer-cluster/kubeadm/upgrading-linux-nodes.md#upgrading-worker-nodes
kind: section
title: Upgrading worker nodes
source: tasks/administer-cluster/kubeadm/upgrading-linux-nodes.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/
heading: Upgrading worker nodes
parent: okf-structure/tasks/administer-cluster/kubeadm/upgrading-linux-nodes
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/upgrading-linux-nodes.md#changing-the-package-repository
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/upgrading-linux-nodes.md#whatsnext
word_count: 287
---

### Upgrade kubeadm

Upgrade kubeadm:

```shell
# replace x in .x-* with the latest patch version
sudo apt-mark unhold kubeadm && \
sudo apt-get update && sudo apt-get install -y kubeadm='.x-*' && \
sudo apt-mark hold kubeadm
```

For systems with DNF:
```shell
# replace x in .x-* with the latest patch version
sudo yum install -y kubeadm-'.x-*' --disableexcludes=kubernetes
```
For systems with DNF5:
```shell
# replace x in .x-* with the latest patch version
sudo yum install -y kubeadm-'.x-*' --setopt=disable_excludes=kubernetes
```

### Call "kubeadm upgrade"

For worker nodes this upgrades the local kubelet configuration:

```shell
sudo kubeadm upgrade node
```

### Drain the node

Prepare the node for maintenance by marking it unschedulable and evicting the workloads:

```shell
# execute this command on a control plane node
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### Upgrade kubelet and kubectl

1. Upgrade the kubelet and kubectl:

   
   
   ```shell
   # replace x in .x-* with the latest patch version
   sudo apt-mark unhold kubelet kubectl && \
   sudo apt-get update && sudo apt-get install -y kubelet='.x-*' kubectl='.x-*' && \
   sudo apt-mark hold kubelet kubectl
   ```
   
   
   For systems with DNF:
   ```shell
   # replace x in .x-* with the latest patch version
   sudo yum install -y kubelet-'.x-*' kubectl-'.x-*' --disableexcludes=kubernetes
   ```
   For systems with DNF5:
   ```shell
   # replace x in .x-* with the latest patch version
   sudo yum install -y kubelet-'.x-*' kubectl-'.x-*' --setopt=disable_excludes=kubernetes
   ```
   
   

1. Restart the kubelet:

   ```shell
   sudo systemctl daemon-reload
   sudo systemctl restart kubelet
   ```

### Uncordon the node

Bring the node back online by marking it schedulable:

```shell
# execute this command on a control plane node
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```
