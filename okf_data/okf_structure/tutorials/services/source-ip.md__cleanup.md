---
id: okf-structure/tutorials/services/source-ip.md#cleanup
kind: section
title: Cleanup
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Cleanup
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#cross-platform-support
next_sibling: okf-structure/tutorials/services/source-ip.md#whatsnext
word_count: 22
---

Delete the Services:

```shell
kubectl delete svc -l app=source-ip-app
```

Delete the Deployment, ReplicaSet and Pod:

```shell
kubectl delete deployment source-ip-app
```
