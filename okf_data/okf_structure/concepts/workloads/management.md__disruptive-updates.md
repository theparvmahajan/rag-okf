---
id: okf-structure/concepts/workloads/management.md#disruptive-updates
kind: section
title: Disruptive updates
source: concepts/workloads/management.md
url: https://kubernetes.io/docs/concepts/workloads/management/
heading: Disruptive updates
parent: okf-structure/concepts/workloads/management
children: []
prev_sibling: okf-structure/concepts/workloads/management.md#in-place-updates-of-resources
next_sibling: okf-structure/concepts/workloads/management.md#whatsnext
word_count: 72
---

In some cases, you may need to update resource fields that cannot be updated once initialized, or
you may want to make a recursive change immediately, such as to fix broken pods created by a
Deployment. To change such fields, use `replace --force`, which deletes and re-creates the
resource. In this case, you can modify your original configuration file:

```shell
kubectl replace -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml --force
```

```none
deployment.apps/my-nginx deleted
deployment.apps/my-nginx replaced
```
