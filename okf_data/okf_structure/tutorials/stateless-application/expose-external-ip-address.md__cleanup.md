---
id: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#cleanup
kind: section
title: Cleanup
source: tutorials/stateless-application/expose-external-ip-address.md
url: https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
heading: Cleanup
parent: okf-structure/tutorials/stateless-application/expose-external-ip-address
children: []
prev_sibling: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#creating-a-service-for-an-application-running-in-five-pods
next_sibling: okf-structure/tutorials/stateless-application/expose-external-ip-address.md#whatsnext
word_count: 38
---

To delete the Service, enter this command:

```shell
kubectl delete services my-service
```

To delete the Deployment, the ReplicaSet, and the Pods that are running
the Hello World application, enter this command:

```shell
kubectl delete deployment hello-world
```
