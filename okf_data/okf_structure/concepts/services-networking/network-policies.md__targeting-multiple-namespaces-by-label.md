---
id: okf-structure/concepts/services-networking/network-policies.md#targeting-multiple-namespaces-by-label
kind: section
title: Targeting multiple namespaces by label
source: concepts/services-networking/network-policies.md
url: https://kubernetes.io/docs/concepts/services-networking/network-policies/
heading: Targeting multiple namespaces by label
parent: okf-structure/concepts/services-networking/network-policies
children: []
prev_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-a-range-of-ports
next_sibling: okf-structure/concepts/services-networking/network-policies.md#targeting-a-namespace-by-its-name
word_count: 114
---

In this scenario, your `Egress` NetworkPolicy targets more than one namespace using their
label names. For this to work, you need to label the target namespaces. For example:

```shell
kubectl label namespace frontend namespace=frontend
kubectl label namespace backend namespace=backend
```

Add the labels under `namespaceSelector` in your NetworkPolicy document. For example:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: egress-namespaces
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchExpressions:
        - key: namespace
          operator: In
          values: ["frontend", "backend"]
```

It is not possible to directly specify the name of the namespaces in a NetworkPolicy.
You must use a `namespaceSelector` with `matchLabels` or `matchExpressions` to select the
namespaces based on their labels.
