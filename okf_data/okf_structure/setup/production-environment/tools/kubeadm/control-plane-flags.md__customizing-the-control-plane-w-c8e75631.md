---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-the-control-plane-with-flags-in-clusterconfiguration
kind: section
title: Customizing the control plane with flags in `ClusterConfiguration`
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: Customizing the control plane with flags in `ClusterConfiguration`
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-with-patches-patches
word_count: 311
---

The kubeadm `ClusterConfiguration` object exposes a way for users to override the default
flags passed to control plane components such as the APIServer, ControllerManager, Scheduler and Etcd.
The components are defined using the following structures:

- `apiServer`
- `controllerManager`
- `scheduler`
- `etcd`

These structures contain a common `extraArgs` field, that consists of `name` / `value` pairs.
To override a flag for a control plane component:

1.  Add the appropriate `extraArgs` to your configuration.
2.  Add flags to the `extraArgs` field.
3.  Run `kubeadm init` with `--config <YOUR CONFIG YAML>`.

You can generate a `ClusterConfiguration` object with default values by running `kubeadm config print init-defaults`
and saving the output to a file of your choice.

The `ClusterConfiguration` object is currently global in kubeadm clusters. This means that any flags that you add,
will apply to all instances of the same component on different nodes. To apply individual configuration per component
on different nodes you can use patches.

Duplicate flags (keys), or passing the same flag `--foo` multiple times, is currently not supported.
To workaround that you must use patches.

### APIServer flags

For details, see the reference documentation for kube-apiserver.

Example usage:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
apiServer:
  extraArgs:
  - name: "enable-admission-plugins"
    value: "AlwaysPullImages,DefaultStorageClass"
  - name: "audit-log-path"
    value: "/home/johndoe/audit.log"
```

### ControllerManager flags

For details, see the reference documentation for kube-controller-manager.

Example usage:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
controllerManager:
  extraArgs:
  - name: "cluster-signing-key-file"
    value: "/home/johndoe/keys/ca.key"
  - name: "deployment-controller-sync-period"
    value: "50"
```

### Scheduler flags

For details, see the reference documentation for kube-scheduler.

Example usage:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
kubernetesVersion: v1.16.0
scheduler:
  extraArgs:
  - name: "config"
    value: "/etc/kubernetes/scheduler-config.yaml"
  extraVolumes:
    - name: schedulerconfig
      hostPath: /home/johndoe/schedconfig.yaml
      mountPath: /etc/kubernetes/scheduler-config.yaml
      readOnly: true
      pathType: "File"
```

### Etcd flags

For details, see the etcd server documentation.

Example usage:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
etcd:
  local:
    extraArgs:
    - name: "election-timeout"
      value: 1000
```
