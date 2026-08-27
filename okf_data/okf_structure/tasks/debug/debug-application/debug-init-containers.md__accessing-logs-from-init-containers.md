---
id: okf-structure/tasks/debug/debug-application/debug-init-containers.md#accessing-logs-from-init-containers
kind: section
title: Accessing logs from Init Containers
source: tasks/debug/debug-application/debug-init-containers.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/
heading: Accessing logs from Init Containers
parent: okf-structure/tasks/debug/debug-application/debug-init-containers
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#getting-details-about-init-containers
next_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#understanding-pod-status
word_count: 51
---

Pass the Init Container name along with the Pod name
to access its logs.

```shell
kubectl logs <pod-name> -c <init-container-2>
```

Init Containers that run a shell script print
commands as they're executed. For example, you can do this in Bash by running
`set -x` at the beginning of the script.
