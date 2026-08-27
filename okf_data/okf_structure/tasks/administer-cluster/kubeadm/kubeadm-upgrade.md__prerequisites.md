---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubeadm/kubeadm-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md#changing-the-package-repository
word_count: 389
---

- Make sure you read the release notes carefully.
- The cluster should use a static control plane and etcd pods or external etcd.
- Make sure to back up any important components, such as app-level state stored in a database.
  `kubeadm upgrade` does not touch your workloads, only components internal to Kubernetes, but backups are always a best practice.
- Swap must be disabled.

### Additional information

- The instructions below outline when to drain each node during the upgrade process.
  If you are performing a **minor** version upgrade for any kubelet, you **must**
  first drain the node (or nodes) that you are upgrading. In the case of control plane nodes,
  they could be running CoreDNS Pods or other critical workloads. For more information see
  Draining nodes.
- The Kubernetes project recommends that you match your kubelet and kubeadm versions.
  You can instead use a version of kubelet that is older than kubeadm, provided it is within the
  range of supported versions.
  For more details, please visit kubeadm's skew against the kubelet.
- All containers are restarted after upgrade, because the container spec hash value is changed.
- To verify that the kubelet service has successfully restarted after the kubelet has been upgraded,
  you can execute `systemctl status kubelet` or view the service logs with `journalctl -xeu kubelet`.
- `kubeadm upgrade` supports `--config` with a
`UpgradeConfiguration` API type which can
be used to configure the upgrade process.
- `kubeadm upgrade` does not support reconfiguration of an existing cluster. Follow the steps in
  Reconfiguring a kubeadm cluster instead.

### Considerations when upgrading etcd

Because the `kube-apiserver` static pod is running at all times (even if you
have drained the node), when you perform a kubeadm upgrade which includes an
etcd upgrade, in-flight requests to the server will stall while the new etcd
static pod is restarting. As a workaround, it is possible to actively stop the
`kube-apiserver` process a few seconds before starting the `kubeadm upgrade
apply` command. This permits to complete in-flight requests and close existing
connections, and minimizes the consequence of the etcd downtime. This can be
done as follows on control plane nodes:

```shell
killall -s SIGTERM kube-apiserver # trigger a graceful kube-apiserver shutdown
sleep 20 # wait a little bit to permit completing in-flight requests
kubeadm upgrade ... # execute a kubeadm upgrade command
```
