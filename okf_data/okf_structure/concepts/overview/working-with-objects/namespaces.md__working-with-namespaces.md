---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#working-with-namespaces
kind: section
title: Working with Namespaces
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: Working with Namespaces
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#initial-namespaces
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#namespaces-and-dns
word_count: 132
---

Creation and deletion of namespaces are described in the
Admin Guide documentation for namespaces.

Avoid creating namespaces with the prefix `kube-`, since it is reserved for Kubernetes system namespaces.

### Viewing namespaces

You can list the current namespaces in a cluster using:

```shell
kubectl get namespace
```
```
NAME              STATUS   AGE
default           Active   1d
kube-node-lease   Active   1d
kube-public       Active   1d
kube-system       Active   1d
```

### Setting the namespace for a request

To set the namespace for a current request, use the `--namespace` flag.

For example:

```shell
kubectl run nginx --image=nginx --namespace=<insert-namespace-name-here>
kubectl get pods --namespace=<insert-namespace-name-here>
```

### Setting the namespace preference

You can permanently save the namespace for all subsequent kubectl commands in that
context.

```shell
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:
```
