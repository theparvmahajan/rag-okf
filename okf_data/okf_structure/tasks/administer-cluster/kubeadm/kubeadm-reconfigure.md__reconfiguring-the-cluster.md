---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#reconfiguring-the-cluster
kind: section
title: Reconfiguring the cluster
source: tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/
heading: Reconfiguring the cluster
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#persisting-the-reconfiguration
word_count: 886
---

kubeadm writes a set of cluster wide component configuration options in
ConfigMaps and other objects. These objects must be manually edited. The command `kubectl edit`
can be used for that.

The `kubectl edit` command will open a text editor where you can edit and save the object directly.

You can use the environment variables `KUBECONFIG` and `KUBE_EDITOR` to specify the location of
the kubectl consumed kubeconfig file and preferred text editor.

For example:
```
KUBECONFIG=/etc/kubernetes/admin.conf KUBE_EDITOR=nano kubectl edit <parameters>
```

Upon saving any changes to these cluster objects, components running on nodes may not be
automatically updated. The steps below instruct you on how to perform that manually.

Component configuration in ConfigMaps is stored as unstructured data (YAML string).
This means that validation will not be performed upon updating the contents of a ConfigMap.
You have to be careful to follow the documented API format for a particular
component configuration and avoid introducing typos and YAML indentation mistakes.

### Applying cluster configuration changes

#### Updating the `ClusterConfiguration`

During cluster creation and upgrade, kubeadm writes its
`ClusterConfiguration`
in a ConfigMap called `kubeadm-config` in the `kube-system` namespace.

To change a particular option in the `ClusterConfiguration` you can edit the ConfigMap with this command:

```shell
kubectl edit cm -n kube-system kubeadm-config
```

The configuration is located under the `data.ClusterConfiguration` key.

The `ClusterConfiguration` includes a variety of options that affect the configuration of individual
components such as kube-apiserver, kube-scheduler, kube-controller-manager, CoreDNS, etcd and kube-proxy.
Changes to the configuration must be reflected on node components manually.

#### Reflecting `ClusterConfiguration` changes on control plane nodes

kubeadm manages the control plane components as static Pod manifests located in
the directory `/etc/kubernetes/manifests`.
Any changes to the `ClusterConfiguration` under the `apiServer`, `controllerManager`, `scheduler` or `etcd`
keys must be reflected in the associated files in the manifests directory on a control plane node.

Such changes may include:
- `extraArgs` - requires updating the list of flags passed to a component container
- `extraVolumes` - requires updating the volume mounts for a component container
- `*SANs` - requires writing new certificates with updated Subject Alternative Names

Before proceeding with these changes, make sure you have backed up the directory `/etc/kubernetes/`.

To write new certificates you can use:
```shell
kubeadm init phase certs <component-name> --config <config-file>
```

To write new manifest files in `/etc/kubernetes/manifests` you can use:

```shell
# For Kubernetes control plane components
kubeadm init phase control-plane <component-name> --config <config-file>
# For local etcd
kubeadm init phase etcd local --config <config-file>
```

The `<config-file>` contents must match the updated `ClusterConfiguration`.
The `<component-name>` value must be a name of a Kubernetes control plane component (`apiserver`, `controller-manager` or `scheduler`).

Updating a file in `/etc/kubernetes/manifests` will tell the kubelet to restart the static Pod for the corresponding component.
Try doing these changes one node at a time to leave the cluster without downtime.

### Applying kubelet configuration changes

#### Updating the `KubeletConfiguration`

During cluster creation and upgrade, kubeadm writes its
`KubeletConfiguration`
in a ConfigMap called `kubelet-config` in the `kube-system` namespace.

You can edit the ConfigMap with this command:

```shell
kubectl edit cm -n kube-system kubelet-config
```

The configuration is located under the `data.kubelet` key.

#### Reflecting the kubelet changes

To reflect the change on kubeadm nodes you must do the following:
- Log in to a kubeadm node
- Run `kubeadm upgrade node phase kubelet-config` to download the latest `kubelet-config`
ConfigMap contents into the local file `/var/lib/kubelet/config.yaml`
- Edit the file `/var/lib/kubelet/kubeadm-flags.env` to apply additional configuration with
flags
- Restart the kubelet service with `systemctl restart kubelet`

Do these changes one node at a time to allow workloads to be rescheduled properly.

During `kubeadm upgrade`, kubeadm downloads the `KubeletConfiguration` from the
`kubelet-config` ConfigMap and overwrite the contents of `/var/lib/kubelet/config.yaml`.
This means that node local configuration must be applied either by flags in
`/var/lib/kubelet/kubeadm-flags.env` or by manually updating the contents of
`/var/lib/kubelet/config.yaml` after `kubeadm upgrade`, and then restarting the kubelet.

### Applying kube-proxy configuration changes

#### Updating the `KubeProxyConfiguration`

During cluster creation and upgrade, kubeadm writes its
`KubeProxyConfiguration`
in a ConfigMap in the `kube-system` namespace called `kube-proxy`.

This ConfigMap is used by the `kube-proxy` DaemonSet in the `kube-system` namespace.

To change a particular option in the `KubeProxyConfiguration`, you can edit the ConfigMap with this command:

```shell
kubectl edit cm -n kube-system kube-proxy
```

The configuration is located under the `data.config.conf` key.

#### Reflecting the kube-proxy changes

Once the `kube-proxy` ConfigMap is updated, you can restart all kube-proxy Pods:

Delete the Pods with:

```shell
kubectl delete po -n kube-system -l k8s-app=kube-proxy
```

New Pods that use the updated ConfigMap will be created.

Because kubeadm deploys kube-proxy as a DaemonSet, node specific configuration is unsupported.

### Applying CoreDNS configuration changes

#### Updating the CoreDNS Deployment and Service

kubeadm deploys CoreDNS as a Deployment called `coredns` and with a Service `kube-dns`,
both in the `kube-system` namespace.

To update any of the CoreDNS settings, you can edit the Deployment and
Service objects:

```shell
kubectl edit deployment -n kube-system coredns
kubectl edit service -n kube-system kube-dns
```

#### Reflecting the CoreDNS changes

Once the CoreDNS changes are applied you can restart the CoreDNS deployment:

```shell
kubectl rollout restart deployment -n kube-system coredns
```

kubeadm does not allow CoreDNS configuration during cluster creation and upgrade.
This means that if you execute `kubeadm upgrade apply`, your changes to the CoreDNS
objects will be lost and must be reapplied.
