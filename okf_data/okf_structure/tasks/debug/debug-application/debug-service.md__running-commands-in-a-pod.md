---
id: okf-structure/tasks/debug/debug-application/debug-service.md#running-commands-in-a-pod
kind: section
title: Running commands in a Pod
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: Running commands in a Pod
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#introduction
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#setup
word_count: 79
---

For many steps here you will want to see what a Pod running in the cluster
sees.  The simplest way to do this is to run an interactive busybox Pod:

```none
kubectl run -it --rm --restart=Never busybox --image=registry.k8s.io/busybox:1.27.2 sh
```

If you don't see a command prompt, try pressing enter.

If you already have a running Pod that you prefer to use, you can run a
command in it using:

```shell
kubectl exec <POD-NAME> -c <CONTAINER-NAME> -- <COMMAND>
```
