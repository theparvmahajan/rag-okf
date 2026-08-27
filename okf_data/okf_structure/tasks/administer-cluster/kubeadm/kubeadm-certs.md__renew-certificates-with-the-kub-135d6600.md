---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#renew-certificates-with-the-kubernetes-certificates-api
kind: section
title: Renew certificates with the Kubernetes certificates API
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Renew certificates with the Kubernetes certificates API
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#manual-certificate-renewal
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#renew-certificates-with-external-ca
word_count: 149
---

This section provides more details about how to execute manual certificate renewal using the Kubernetes certificates API.

These are advanced topics for users who need to integrate their organization's certificate
infrastructure into a kubeadm-built cluster. If the default kubeadm configuration satisfies your
needs, you should let kubeadm manage certificates instead.

### Set up a signer

The Kubernetes Certificate Authority does not work out of the box.
You can configure an external signer such as cert-manager,
or you can use the built-in signer.

The built-in signer is part of `kube-controller-manager`.

To activate the built-in signer, you must pass the `--cluster-signing-cert-file` and
`--cluster-signing-key-file` flags.

If you're creating a new cluster, you can use a kubeadm
configuration file:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
controllerManager:
  extraArgs:
  - name: "cluster-signing-cert-file"
    value: "/etc/kubernetes/pki/ca.crt"
  - name: "cluster-signing-key-file"
    value: "/etc/kubernetes/pki/ca.key"
```

### Create certificate signing requests (CSR)

See Create CertificateSigningRequest
for creating CSRs with the Kubernetes API.
