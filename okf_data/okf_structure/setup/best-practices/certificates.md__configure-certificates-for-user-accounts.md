---
id: okf-structure/setup/best-practices/certificates.md#configure-certificates-for-user-accounts
kind: section
title: Configure certificates for user accounts
source: setup/best-practices/certificates.md
url: https://kubernetes.io/docs/setup/best-practices/certificates/
heading: Configure certificates for user accounts
parent: okf-structure/setup/best-practices/certificates
children: []
prev_sibling: okf-structure/setup/best-practices/certificates.md#configure-certificates-manually
next_sibling: null
word_count: 391
---

You must manually configure these administrator accounts and service accounts:

| Filename                | Credential name            | Default CN                          | O (in Subject)         |
|-------------------------|----------------------------|-------------------------------------|------------------------|
| admin.conf              | default-admin              | kubernetes-admin                    | `<admin-group>`        |
| super-admin.conf        | default-super-admin        | kubernetes-super-admin              | system:masters         |
| kubelet.conf            | default-auth               | system:node:`<nodeName>` (see note) | system:nodes           |
| controller-manager.conf | default-controller-manager | system:kube-controller-manager      |                        |
| scheduler.conf          | default-scheduler          | system:kube-scheduler               |                        |

The value of `<nodeName>` for `kubelet.conf` **must** match precisely the value of the node name
provided by the kubelet as it registers with the apiserver. For further details, read the
Node Authorization.

In the above example `<admin-group>` is implementation specific. Some tools sign the
certificate in the default `admin.conf` to be part of the `system:masters` group.
`system:masters` is a break-glass, super user group can bypass the authorization
layer of Kubernetes, such as RBAC. Also some tools do not generate a separate
`super-admin.conf` with a certificate bound to this super user group.

kubeadm generates two separate administrator certificates in kubeconfig files.
One is in `admin.conf` and has `Subject: O = kubeadm:cluster-admins, CN = kubernetes-admin`.
`kubeadm:cluster-admins` is a custom group bound to the `cluster-admin` ClusterRole.
This file is generated on all kubeadm managed control plane machines.

Another is in `super-admin.conf` that has `Subject: O = system:masters, CN = kubernetes-super-admin`.
This file is generated only on the node where `kubeadm init` was called.

1. For each configuration, generate an x509 certificate/key pair with the
   given Common Name (CN) and Organization (O).

1. Run `kubectl` as follows for each configuration:

   ```
   KUBECONFIG=<filename> kubectl config set-cluster default-cluster --server=https://<host ip>:6443 --certificate-authority <path-to-kubernetes-ca> --embed-certs
   KUBECONFIG=<filename> kubectl config set-credentials <credential-name> --client-key <path-to-key>.pem --client-certificate <path-to-cert>.pem --embed-certs
   KUBECONFIG=<filename> kubectl config set-context default-system --cluster default-cluster --user <credential-name>
   KUBECONFIG=<filename> kubectl config use-context default-system
   ```

These files are used as follows:

| Filename                | Command                 | Comment                                                               |
|-------------------------|-------------------------|-----------------------------------------------------------------------|
| admin.conf              | kubectl                 | Configures administrator user for the cluster                         |
| super-admin.conf        | kubectl                 | Configures super administrator user for the cluster                   |
| kubelet.conf            | kubelet                 | One required for each node in the cluster.                            |
| controller-manager.conf | kube-controller-manager | Must be added to manifest in `manifests/kube-controller-manager.yaml` |
| scheduler.conf          | kube-scheduler          | Must be added to manifest in `manifests/kube-scheduler.yaml`          |

The following files illustrate full paths to the files listed in the previous table:

```
/etc/kubernetes/admin.conf
/etc/kubernetes/super-admin.conf
/etc/kubernetes/kubelet.conf
/etc/kubernetes/controller-manager.conf
/etc/kubernetes/scheduler.conf
```
