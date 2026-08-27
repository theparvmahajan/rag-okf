---
id: okf-structure/setup/production-environment/_index.md#set-limits-on-workload-resources
kind: section
title: Set limits on workload resources
source: setup/production-environment/_index.md
url: https://kubernetes.io/docs/setup/production-environment/
heading: Set limits on workload resources
parent: okf-structure/setup/production-environment/_index
children: []
prev_sibling: okf-structure/setup/production-environment/_index.md#production-user-management
next_sibling: okf-structure/setup/production-environment/_index.md#whatsnext
word_count: 178
---

Demands from production workloads can cause pressure both inside and outside
of the Kubernetes control plane. Consider these items when setting up for the
needs of your cluster's workloads:

- *Set namespace limits*: Set per-namespace quotas on things like memory and CPU. See
  Manage Memory, CPU, and API Resources
  for details.
- *Prepare for DNS demand*: If you expect workloads to massively scale up,
  your DNS service must be ready to scale up as well. See
  Autoscale the DNS service in a Cluster.
- *Create additional service accounts*: User accounts determine what users can
  do on a cluster, while a service account defines pod access within a particular
  namespace. By default, a pod takes on the default service account from its namespace.
  See Managing Service Accounts
  for information on creating a new service account. For example, you might want to:
  - Add secrets that a pod could use to pull images from a particular container registry. See
    Configure Service Accounts for Pods
    for an example.
  - Assign RBAC permissions to a service account. See
    ServiceAccount permissions
    for details.
