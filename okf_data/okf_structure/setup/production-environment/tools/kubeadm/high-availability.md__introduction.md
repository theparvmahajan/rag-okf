---
id: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#introduction
kind: section
title: Creating Highly Available Clusters with kubeadm
source: setup/production-environment/tools/kubeadm/high-availability.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/high-availability
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#prerequisites
word_count: 139
---

This page explains two different approaches to setting up a highly available Kubernetes
cluster using kubeadm:

- With stacked control plane nodes. This approach requires less infrastructure. The etcd members
  and control plane nodes are co-located.
- With an external etcd cluster. This approach requires more infrastructure. The
  control plane nodes and etcd members are separated.

Before proceeding, you should carefully consider which approach best meets the needs of your applications
and environment. Options for Highly Available topology
outlines the advantages and disadvantages of each.

If you encounter issues with setting up the HA cluster, please report these
in the kubeadm issue tracker.

See also the upgrade documentation.

This page does not address running your cluster on a cloud provider. In a cloud
environment, neither approach documented here works with Service objects of type
LoadBalancer, or with dynamic PersistentVolumes.
