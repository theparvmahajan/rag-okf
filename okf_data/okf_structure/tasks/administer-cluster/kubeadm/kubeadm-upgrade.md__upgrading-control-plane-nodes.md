---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#upgrading-control-plane-nodes
kind: section
title: Upgrading control plane nodes
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: Upgrading control plane nodes
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#determine-which-version-to-upgrade-to
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#upgrade-worker-nodes
word_count: 696
---

The upgrade procedure on control plane nodes should be executed one node at a time.
Pick a control plane node that you wish to upgrade first. It must have the `/etc/kubernetes/admin.conf` file.

### Call "kubeadm upgrade"

**For the first control plane node**

1. Upgrade kubeadm:

   
   

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

   
   

1. Verify that the download works and has the expected version:

   ```shell
   kubeadm version
   ```

1. Verify the upgrade plan:

   ```shell
   sudo kubeadm upgrade plan
   ```

   This command checks that your cluster can be upgraded, and fetches the versions you can upgrade to.
   It also shows a table with the component config version states.

   
   `kubeadm upgrade` also automatically renews the certificates that it manages on this node.
   To opt-out of certificate renewal the flag `--certificate-renewal=false` can be used.
   For more information see the certificate management guide.
   

1. Choose a version to upgrade to, and run the appropriate command. For example:

   ```shell
   # replace x with the patch version you picked for this upgrade
   sudo kubeadm upgrade apply v.x
   ```

   Once the command finishes you should see:

   ```
   [upgrade/successful] SUCCESS! Your cluster was upgraded to "v.x". Enjoy!

   [upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
   ```

   
   For versions earlier than v1.28, kubeadm defaulted to a mode that upgrades the addons (including CoreDNS and kube-proxy)
   immediately during `kubeadm upgrade apply`, regardless of whether there are other control plane instances that have not
   been upgraded. This may cause compatibility problems. Since v1.28, kubeadm defaults to a mode that checks whether all
   the control plane instances have been upgraded before starting to upgrade the addons. You must perform control plane
   instances upgrade sequentially or at least ensure that the last control plane instance upgrade is not started until all
   the other control plane instances have been upgraded completely, and the addons upgrade will be performed after the last
   control plane instance is upgraded.
   

1. Manually upgrade your CNI provider plugin.

   Your Container Network Interface (CNI) provider may have its own upgrade instructions to follow.
   Check the addons page to
   find your CNI provider and see whether additional upgrade steps are required.

   This step is not required on additional control plane nodes if the CNI provider runs as a DaemonSet.

**For the other control plane nodes**

Same as the first control plane node but use:

```shell
sudo kubeadm upgrade node
```

instead of:

```shell
sudo kubeadm upgrade apply
```

Also calling `kubeadm upgrade plan` and upgrading the CNI provider plugin is no longer needed.

### Drain the node

Prepare the node for maintenance by marking it unschedulable and evicting the workloads:

```shell
# replace <node-to-drain> with the name of your node you are draining
kubectl drain <node-to-drain> --ignore-daemonsets
```

### Upgrade kubelet and kubectl

On Linux nodes, the kubelet defaults to supporting only cgroups v2.
For Kubernetes  the `FailCgroupV1` kubelet configuration option is set to `true` by default.

To learn more, refer to the Kubernetes cgroup v1 deprecation documentation.

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
# replace <node-to-uncordon> with the name of your node
kubectl uncordon <node-to-uncordon>
```
