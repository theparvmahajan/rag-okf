---
id: okf-structure/concepts/workloads/management.md#updating-annotations
kind: section
title: Updating annotations
source: concepts/workloads/management.md
url: https://kubernetes.io/docs/concepts/workloads/management/
heading: Updating annotations
parent: okf-structure/concepts/workloads/management
children: []
prev_sibling: okf-structure/concepts/workloads/management.md#canary-deployments
next_sibling: okf-structure/concepts/workloads/management.md#scaling-your-application
word_count: 71
---

Sometimes you would want to attach annotations to resources. Annotations are arbitrary
non-identifying metadata for retrieval by API clients such as tools or libraries.
This can be done with `kubectl annotate`. For example:

```shell
kubectl annotate pods my-nginx-v4-9gw19 description='my frontend running nginx'
kubectl get pods my-nginx-v4-9gw19 -o yaml
```

```shell
apiVersion: v1
kind: pod
metadata:
  annotations:
    description: my frontend running nginx
...
```

For more information, see annotations
and kubectl annotate.
