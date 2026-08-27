---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-with-patches-patches
kind: section
title: Customizing with patches {#patches}
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: Customizing with patches {#patches}
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-control-plane-with-flags-in-clusterconfiguration
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-kubelet-kubelet
word_count: 224
---

Kubeadm allows you to pass a directory with patch files to `InitConfiguration`,
`JoinConfiguration` and `UpgradeConfiguration`.
on individual nodes. These patches can be used as the last customization step before component configuration
is written to disk.

You can pass this file to `kubeadm init` with `--config <YOUR CONFIG YAML>`:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: InitConfiguration
patches:
  directory: /home/user/somedir
```

For `kubeadm init` you can pass a file containing both a `ClusterConfiguration` and `InitConfiguration`
separated by `---`.

You can pass this file to `kubeadm join` with `--config <YOUR CONFIG YAML>`:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: JoinConfiguration
patches:
  directory: /home/user/somedir
```

If you are using `kubeadm upgrade apply` and `kubeadm upgrade node` to upgrade your kubeadm
nodes, you must again provide the same patches, so that the customization is preserved after upgrade.

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: UpgradeConfiguration
apply:
  patches:
    directory: /home/user/somedir
```

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: UpgradeConfiguration
node:
  patches:
    directory: /home/user/somedir
```

The directory must contain files named `target[suffix][+patchtype].extension`.
For example, `kube-apiserver0+merge.yaml` or just `etcd.json`.

- `target` can be one of `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `etcd`,
`kubeletconfiguration` and `corednsdeployment`.
- `suffix` is an optional string that can be used to determine which patches are applied first
alpha-numerically.
- `patchtype` can be one of `strategic`, `merge` or `json` and these must match the patching formats
supported by kubectl.
The default `patchtype` is `strategic`.
- `extension` must be either `json` or `yaml`.
