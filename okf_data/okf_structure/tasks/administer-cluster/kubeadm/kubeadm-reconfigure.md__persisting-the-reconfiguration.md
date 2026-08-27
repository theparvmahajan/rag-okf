---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#persisting-the-reconfiguration
kind: section
title: Persisting the reconfiguration
source: tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/
heading: Persisting the reconfiguration
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#reconfiguring-the-cluster
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#whatsnext
word_count: 272
---

During the execution of `kubeadm upgrade` on a managed node, kubeadm might overwrite configuration
that was applied after the cluster was created (reconfiguration).

### Persisting Node object reconfiguration

kubeadm writes Labels, Taints, CRI socket and other information on the Node object for a particular
Kubernetes node. To change any of the contents of this Node object you can use:

```shell
kubectl edit no <node-name>
```

During `kubeadm upgrade` the contents of such a Node might get overwritten.
If you would like to persist your modifications to the Node object after upgrade,
you can prepare a kubectl patch
and apply it to the Node object:

```shell
kubectl patch no <node-name> --patch-file <patch-file>
```

#### Persisting control plane component reconfiguration

The main source of control plane configuration is the `ClusterConfiguration`
object stored in the cluster. To extend the static Pod manifests configuration,
patches can be used.

These patch files must remain as files on the control plane nodes to ensure that
they can be used by the `kubeadm upgrade ... --patches <directory>`.

If reconfiguration is done to the `ClusterConfiguration` and static Pod manifests on disk,
the set of node specific patches must be updated accordingly.

#### Persisting kubelet reconfiguration

Any changes to the `KubeletConfiguration` stored in `/var/lib/kubelet/config.yaml` will be overwritten on
`kubeadm upgrade` by downloading the contents of the cluster wide `kubelet-config` ConfigMap.
To persist kubelet node specific configuration either the file `/var/lib/kubelet/config.yaml`
has to be updated manually post-upgrade or the file `/var/lib/kubelet/kubeadm-flags.env` can include flags.
The kubelet flags override the associated `KubeletConfiguration` options, but note that
some of the flags are deprecated.

A kubelet restart will be required after changing `/var/lib/kubelet/config.yaml` or
`/var/lib/kubelet/kubeadm-flags.env`.
