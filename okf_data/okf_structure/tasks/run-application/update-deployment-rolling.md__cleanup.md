---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#cleanup
kind: section
title: Cleanup
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Cleanup
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#rolling-back-to-a-previous-revision-rollback
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#whatsnext
word_count: 9
---

Delete the Deployment:

```shell
kubectl delete deployment nginx-deployment
```
