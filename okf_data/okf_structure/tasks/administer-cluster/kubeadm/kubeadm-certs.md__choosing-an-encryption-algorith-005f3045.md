---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#choosing-an-encryption-algorithm-choosing-encryption-algorithm
kind: section
title: Choosing an encryption algorithm {#choosing-encryption-algorithm}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Choosing an encryption algorithm {#choosing-encryption-algorithm}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#using-custom-certificates-custom-certificates
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#choosing-certificate-validity-period-choosing-cert-validity-period
word_count: 49
---

kubeadm allows you to choose an encryption algorithm that is used for creating
public and private keys. That can be done by using the `encryptionAlgorithm` field of the
kubeadm configuration:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
encryptionAlgorithm: <ALGORITHM>
```

`<ALGORITHM>` can be one of `RSA-2048` (default), `RSA-3072`, `RSA-4096` or `ECDSA-P256`.
