---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#enabling-signed-kubelet-serving-certificates-kubelet-serving-certs
kind: section
title: Enabling signed kubelet serving certificates {#kubelet-serving-certs}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Enabling signed kubelet serving certificates {#kubelet-serving-certs}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#certificate-authority-ca-rotation-certificate-authority-rotation
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#generating-kubeconfig-files-for-additional-users-kubeconfig-additional-users
word_count: 385
---

By default the kubelet serving certificate deployed by kubeadm is self-signed.
This means a connection from external services like the
metrics-server to a
kubelet cannot be secured with TLS.

To configure the kubelets in a new kubeadm cluster to obtain properly signed serving
certificates you must pass the following minimal configuration to `kubeadm init`:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
serverTLSBootstrap: true
```

If you have already created the cluster you must adapt it by doing the following:
 - Find and edit the `kubelet-config` ConfigMap in the `kube-system` namespace.
In that ConfigMap, the `kubelet` key has a
KubeletConfiguration
document as its value. Edit the KubeletConfiguration document to set `serverTLSBootstrap: true`.
- On each node, add the `serverTLSBootstrap: true` field in `/var/lib/kubelet/config.yaml`
and restart the kubelet with `systemctl restart kubelet`

The field `serverTLSBootstrap: true` will enable the bootstrap of kubelet serving
certificates by requesting them from the `certificates.k8s.io` API. One known limitation
is that the CSRs (Certificate Signing Requests) for these certificates cannot be automatically
approved by the default signer in the kube-controller-manager -
`kubernetes.io/kubelet-serving`.
This will require action from the user or a third party controller.

These CSRs can be viewed using:

```shell
kubectl get csr
```
```console
NAME        AGE     SIGNERNAME                        REQUESTOR                      CONDITION
csr-9wvgt   112s    kubernetes.io/kubelet-serving     system:node:worker-1           Pending
csr-lz97v   1m58s   kubernetes.io/kubelet-serving     system:node:control-plane-1    Pending
```

To approve them you can do the following:
```shell
kubectl certificate approve <CSR-name>
```

By default, these serving certificate will expire after one year. Kubeadm sets the
`KubeletConfiguration` field `rotateCertificates` to `true`, which means that close
to expiration a new set of CSRs for the serving certificates will be created and must
be approved to complete the rotation. To understand more see
Certificate Rotation.

If you are looking for a solution for automatic approval of these CSRs it is recommended
that you contact your cloud provider and ask if they have a CSR signer that verifies
the node identity with an out of band mechanism.

Third party custom controllers can be used:
- kubelet-csr-approver

Such a controller is not a secure mechanism unless it not only verifies the CommonName
in the CSR but also verifies the requested IPs and domain names. This would prevent
a malicious actor that has access to a kubelet client certificate to create
CSRs requesting serving certificates for any IP or domain name.
