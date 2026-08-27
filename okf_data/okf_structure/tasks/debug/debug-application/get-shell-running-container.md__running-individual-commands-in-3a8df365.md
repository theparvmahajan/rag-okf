---
id: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#running-individual-commands-in-a-container
kind: section
title: Running individual commands in a container
source: tasks/debug/debug-application/get-shell-running-container.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/
heading: Running individual commands in a container
parent: okf-structure/tasks/debug/debug-application/get-shell-running-container
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#writing-the-root-page-for-nginx
next_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#opening-a-shell-when-a-pod-has-more-than-one-container
word_count: 52
---

In an ordinary command window, not your shell, list the environment
variables in the running container:

```shell
kubectl exec shell-demo -- env
```

Experiment with running other commands. Here are some examples:

```shell
kubectl exec shell-demo -- ps aux
kubectl exec shell-demo -- ls /
kubectl exec shell-demo -- cat /proc/1/mounts
```
