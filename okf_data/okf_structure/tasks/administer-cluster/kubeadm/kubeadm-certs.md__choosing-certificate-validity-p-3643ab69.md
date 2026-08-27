---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#choosing-certificate-validity-period-choosing-cert-validity-period
kind: section
title: Choosing certificate validity period {#choosing-cert-validity-period}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Choosing certificate validity period {#choosing-cert-validity-period}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#choosing-an-encryption-algorithm-choosing-encryption-algorithm
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#external-ca-mode-external-ca-mode
word_count: 81
---

kubeadm allows you to choose the validity period of CA and leaf certificates.
That can be done by using the `certificateValidityPeriod` and `caCertificateValidityPeriod`
fields of the kubeadm configuration:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
certificateValidityPeriod: 8760h # Default: 365 days × 24 hours = 1 year
caCertificateValidityPeriod: 87600h # Default: 365 days × 24 hours * 10 = 10 years
```

The values of the fields follow the accepted format for
Go's `time.Duration` values, with the longest supported
unit being `h` (hours).
