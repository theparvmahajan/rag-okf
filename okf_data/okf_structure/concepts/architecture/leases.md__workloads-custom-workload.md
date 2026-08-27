---
id: okf-structure/concepts/architecture/leases.md#workloads-custom-workload
kind: section
title: Workloads {#custom-workload}
source: concepts/architecture/leases.md
url: https://kubernetes.io/docs/concepts/architecture/leases/
heading: Workloads {#custom-workload}
parent: okf-structure/concepts/architecture/leases
children: []
prev_sibling: okf-structure/concepts/architecture/leases.md#api-server-identity
next_sibling: null
word_count: 154
---

Your own workload can define its own use of Leases. For example, you might run a custom
controller where a primary or leader member
performs operations that its peers do not. You define a Lease so that the controller replicas can select
or elect a leader, using the Kubernetes API for coordination.
If you do use a Lease, it's a good practice to define a name for the Lease that is obviously linked to
the product or component. For example, if you have a component named Example Foo, use a Lease named
`example-foo`.

If a cluster operator or another end user could deploy multiple instances of a component, select a name
prefix and pick a mechanism (such as hash of the name of the Deployment) to avoid name collisions
for the Leases.

You can use another approach so long as it achieves the same outcome: different software products do
not conflict with one another.
