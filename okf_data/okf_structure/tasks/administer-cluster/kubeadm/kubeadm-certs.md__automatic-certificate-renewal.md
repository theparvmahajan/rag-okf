---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#automatic-certificate-renewal
kind: section
title: Automatic certificate renewal
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Automatic certificate renewal
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#certificate-expiry-and-management-check-certificate-expiration
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#manual-certificate-renewal
word_count: 85
---

kubeadm renews all the certificates during control plane
upgrade.

This feature is designed for addressing the simplest use cases;
if you don't have specific requirements on certificate renewal and perform Kubernetes version
upgrades regularly (less than 1 year in between each upgrade), kubeadm will take care of keeping
your cluster up to date and reasonably secure.

If you have more complex requirements for certificate renewal, you can opt out from the default
behavior by passing `--certificate-renewal=false` to `kubeadm upgrade apply` or to `kubeadm
upgrade node`.
