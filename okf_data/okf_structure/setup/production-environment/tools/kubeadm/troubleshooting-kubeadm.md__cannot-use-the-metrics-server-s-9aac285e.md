---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#cannot-use-the-metrics-server-securely-in-a-kubeadm-cluster
kind: section
title: Cannot use the metrics-server securely in a kubeadm cluster
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: Cannot use the metrics-server securely in a kubeadm cluster
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-reset-unmounts-var-lib-kubelet
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#upgrade-fails-due-to-etcd-hash-not-changing
word_count: 108
---

In a kubeadm cluster, the metrics-server
can be used insecurely by passing the `--kubelet-insecure-tls` to it. This is not recommended for production clusters.

If you want to use TLS between the metrics-server and the kubelet there is a problem,
since kubeadm deploys a self-signed serving certificate for the kubelet. This can cause the following errors
on the side of the metrics-server:

```
x509: certificate signed by unknown authority
x509: certificate is valid for IP-foo not IP-bar
```

See Enabling signed kubelet serving certificates
to understand how to configure the kubelets in a kubeadm cluster to have properly signed serving certificates.

Also see How to run the metrics-server securely.
