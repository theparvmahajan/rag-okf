---
id: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager.md#developing
kind: section
title: Developing
source: tasks/administer-cluster/developing-cloud-controller-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/
heading: Developing
parent: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager.md#background
next_sibling: null
word_count: 131
---

### Out of tree

To build an out-of-tree cloud-controller-manager for your cloud:

1. Create a go package with an implementation that satisfies cloudprovider.Interface.
2. Use `main.go` in cloud-controller-manager from Kubernetes core as a template for your `main.go`. As mentioned above, the only difference should be the cloud package that will be imported.
3. Import your cloud package in `main.go`, ensure your package has an `init` block to run `cloudprovider.RegisterCloudProvider`.

Many cloud providers publish their controller manager code as open source. If you are creating
a new cloud-controller-manager from scratch, you could take an existing out-of-tree cloud
controller manager as your starting point.

### In tree

For in-tree cloud providers, you can run the in-tree cloud controller manager as a daemonset in your cluster. See Cloud Controller Manager Administration for more details.
