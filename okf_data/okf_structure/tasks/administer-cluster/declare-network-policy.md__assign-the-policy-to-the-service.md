---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#assign-the-policy-to-the-service
kind: section
title: Assign the policy to the service
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Assign the policy to the service
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#limit-access-to-the-nginx-service
next_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-access-to-the-service-when-access-label-is-not-defined
word_count: 21
---

Use kubectl to create a NetworkPolicy from the above `nginx-policy.yaml` file:

```console
kubectl apply -f https://k8s.io/examples/service/networking/nginx-policy.yaml
```

```none
networkpolicy.networking.k8s.io/access-nginx created
```
