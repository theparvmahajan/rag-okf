---
id: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#version-skew-policy-version-skew-policy
kind: section
title: Version skew policy {#version-skew-policy}
source: setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
heading: Version skew policy {#version-skew-policy}
parent: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#clean-up-tear-down
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#limitations-limitations
word_count: 334
---

While kubeadm allows version skew against some components that it manages, it is recommended that you
match the kubeadm version with the versions of the control plane components, kube-proxy and kubelet.

### kubeadm's skew against the Kubernetes version

kubeadm can be used with Kubernetes components that are the same version as kubeadm
or one version older. The Kubernetes version can be specified to kubeadm by using the
`--kubernetes-version` flag of `kubeadm init` or the
`ClusterConfiguration.kubernetesVersion`
field when using `--config`. This option will control the versions
of kube-apiserver, kube-controller-manager, kube-scheduler and kube-proxy.

Example:

* kubeadm is at 
* `kubernetesVersion` must be at  or 

### kubeadm's skew against the kubelet

Similarly to the Kubernetes version, kubeadm can be used with a kubelet version that is
the same version as kubeadm or three versions older.

Example:

* kubeadm is at 
* kubelet on the host must be at , ,
   or 

### kubeadm's skew against kubeadm

There are certain limitations on how kubeadm commands can operate on existing nodes or whole clusters
managed by kubeadm.

If new nodes are joined to the cluster, the kubeadm binary used for `kubeadm join` must match
the last version of kubeadm used to either create the cluster with `kubeadm init` or to upgrade
the same node with `kubeadm upgrade`. Similar rules apply to the rest of the kubeadm commands
with the exception of `kubeadm upgrade`.

Example for `kubeadm join`:

* kubeadm version  was used to create a cluster with `kubeadm init`
* Joining nodes must use a kubeadm binary that is at version 

Nodes that are being upgraded must use a version of kubeadm that is the same MINOR
version or one MINOR version newer than the version of kubeadm used for managing the
node.

Example for `kubeadm upgrade`:

* kubeadm version  was used to create or upgrade the node
* The version of kubeadm used for upgrading the node must be at 
  or 

To learn more about the version skew between the different Kubernetes component see
the Version Skew Policy.
