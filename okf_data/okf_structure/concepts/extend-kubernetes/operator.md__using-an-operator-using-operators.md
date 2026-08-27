---
id: okf-structure/concepts/extend-kubernetes/operator.md#using-an-operator-using-operators
kind: section
title: Using an operator {#using-operators}
source: concepts/extend-kubernetes/operator.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
heading: Using an operator {#using-operators}
parent: okf-structure/concepts/extend-kubernetes/operator
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/operator.md#deploying-operators
next_sibling: okf-structure/concepts/extend-kubernetes/operator.md#writing-your-own-operator-writing-operator
word_count: 77
---

Once you have an operator deployed, you'd use it by adding, modifying or
deleting the kind of resource that the operator uses. Following the above
example, you would set up a Deployment for the operator itself, and then:

```shell
kubectl get SampleDB                   # find configured databases

kubectl edit SampleDB/example-database # manually change some settings
```

…and that's it! The operator will take care of applying the changes
as well as keeping the existing service in good shape.
