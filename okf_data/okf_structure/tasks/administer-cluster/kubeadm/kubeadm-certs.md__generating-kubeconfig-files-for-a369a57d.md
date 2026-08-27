---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#generating-kubeconfig-files-for-additional-users-kubeconfig-additional-users
kind: section
title: Generating kubeconfig files for additional users {#kubeconfig-additional-users}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Generating kubeconfig files for additional users {#kubeconfig-additional-users}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#enabling-signed-kubelet-serving-certificates-kubelet-serving-certs
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#signing-certificate-signing-requests-csr-generated-by-kubeadm-signing-csr
word_count: 326
---

During cluster creation, `kubeadm init` signs the certificate in the `super-admin.conf`
to have `Subject: O = system:masters, CN = kubernetes-super-admin`.
`system:masters`
is a break-glass, super user group that bypasses the authorization layer (for example,
RBAC). The file `admin.conf` is also created
by kubeadm on control plane nodes and it contains a certificate with
`Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin`. `kubeadm:cluster-admins`
is a group logically belonging to kubeadm. If your cluster uses RBAC
(the kubeadm default), the `kubeadm:cluster-admins` group is bound to the
`cluster-admin` ClusterRole.

Avoid sharing the `super-admin.conf` or `admin.conf` files. Instead, create least
privileged access even for people who work as administrators and use that least
privilege alternative for anything other than break-glass (emergency) access.

You can use the `kubeadm kubeconfig user`
command to generate kubeconfig files for additional users.
The command accepts a mixture of command line flags and
kubeadm configuration options.
The generated kubeconfig will be written to stdout and can be piped to a file using
`kubeadm kubeconfig user ... > somefile.conf`.

Example configuration file that can be used with `--config`:

```yaml
# example.yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
# Will be used as the target "cluster" in the kubeconfig
clusterName: "kubernetes"
# Will be used as the "server" (IP or DNS name) of this cluster in the kubeconfig
controlPlaneEndpoint: "some-dns-address:6443"
# The cluster CA key and certificate will be loaded from this local directory
certificatesDir: "/etc/kubernetes/pki"
```

Make sure that these settings match the desired target cluster settings.
To see the settings of an existing cluster use:

```shell
kubectl get cm kubeadm-config -n kube-system -o=jsonpath="{.data.ClusterConfiguration}"
```

The following example will generate a kubeconfig file with credentials valid for 24 hours
for a new user `johndoe` that is part of the `appdevs` group:

```shell
kubeadm kubeconfig user --config example.yaml --org appdevs --client-name johndoe --validity-period 24h
```

The following example will generate a kubeconfig file with administrator credentials valid for 1 week:

```shell
kubeadm kubeconfig user --config example.yaml --client-name admin --validity-period 168h
```
