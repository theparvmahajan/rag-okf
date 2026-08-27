---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#limit-access-to-the-nginx-service
kind: section
title: Limit access to the `nginx` service
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Limit access to the `nginx` service
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-the-service-by-accessing-it-from-another-pod
next_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#assign-the-policy-to-the-service
word_count: 86
---

To limit the access to the `nginx` service so that only Pods with the label `access: true` can query it, create a NetworkPolicy object as follows:

The name of a NetworkPolicy object must be a valid
DNS subdomain name.

NetworkPolicy includes a `podSelector` which selects the grouping of Pods to which the policy applies. You can see this policy selects Pods with the label `app=nginx`. The label was automatically added to the Pod in the `nginx` Deployment. An empty `podSelector` selects all pods in the namespace.
