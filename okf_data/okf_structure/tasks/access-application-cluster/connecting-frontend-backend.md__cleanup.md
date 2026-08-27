---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#cleanup
kind: section
title: Cleanup
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Cleanup
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#send-traffic-through-the-frontend
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#whatsnext
word_count: 41
---

To delete the Services, enter this command:

```shell
kubectl delete services frontend backend
```

To delete the Deployments, the ReplicaSets and the Pods that are running the backend and frontend applications, enter this command:

```shell
kubectl delete deployment frontend backend
```
