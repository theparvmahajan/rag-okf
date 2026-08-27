---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#manual-certificate-renewal
kind: section
title: Manual certificate renewal
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Manual certificate renewal
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#automatic-certificate-renewal
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#renew-certificates-with-the-kubernetes-certificates-api
word_count: 333
---

You can renew your certificates manually at any time with the `kubeadm certs renew` command,
with the appropriate command line options. If you are running cluster with a replicated control
plane, this command needs to be executed on all the control-plane nodes.

This command performs the renewal using CA (or front-proxy-CA) certificate and key stored in `/etc/kubernetes/pki`.

`kubeadm certs renew` uses the existing certificates as the authoritative source for attributes
(Common Name, Organization, subject alternative name) and does not rely on the `kubeadm-config`
ConfigMap.
Even so, the Kubernetes project recommends keeping the served certificate and the associated
values in that ConfigMap synchronized, to avoid any risk of confusion.

After running the command you should restart the control plane Pods. This is required since
dynamic certificate reload is currently not supported for all components and certificates.
Static Pods are managed by the local kubelet
and not by the API Server, thus kubectl cannot be used to delete and restart them.
To restart a static Pod you can temporarily remove its manifest file from `/etc/kubernetes/manifests/`
and wait for 20 seconds (see the `fileCheckFrequency` value in KubeletConfiguration struct).
The kubelet will terminate the Pod if it's no longer in the manifest directory.
You can then move the file back and after another `fileCheckFrequency` period, the kubelet will recreate
the Pod and the certificate renewal for the component can complete.

`kubeadm certs renew` can renew any specific certificate or, with the subcommand `all`, it can renew all of them:

```shell
# If you are running cluster with a replicated control plane, this command
# needs to be executed on all the control-plane nodes.
kubeadm certs renew all
```

### Copying the administrator certificate (optional) {#admin-certificate-copy}

Clusters built with kubeadm often copy the `admin.conf` certificate into
`$HOME/.kube/config`, as instructed in Creating a cluster with kubeadm.
On such a system, to update the contents of `$HOME/.kube/config`
after renewing the `admin.conf`, you could run the following commands:

```shell
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
