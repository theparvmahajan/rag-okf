---
id: okf-structure/tutorials/hello-minikube.md#clean-up
kind: section
title: Clean up
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Clean up
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#enable-addons
next_sibling: okf-structure/tutorials/hello-minikube.md#conclusion
word_count: 59
---

Now you can clean up the resources you created in your cluster:

```shell
kubectl delete service hello-node
kubectl delete deployment hello-node
```

Stop the Minikube cluster

```shell
minikube stop
```

Optionally, delete the Minikube VM:

```shell
# Optional
minikube delete
```

If you want to use minikube again to learn more about Kubernetes, you don't need to delete it.
