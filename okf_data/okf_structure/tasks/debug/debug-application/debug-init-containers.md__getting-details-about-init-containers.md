---
id: okf-structure/tasks/debug/debug-application/debug-init-containers.md#getting-details-about-init-containers
kind: section
title: Getting details about Init Containers
source: tasks/debug/debug-application/debug-init-containers.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/
heading: Getting details about Init Containers
parent: okf-structure/tasks/debug/debug-application/debug-init-containers
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#checking-the-status-of-init-containers
next_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#accessing-logs-from-init-containers
word_count: 119
---

View more detailed information about Init Container execution:

```shell
kubectl describe pod <pod-name>
```

For example, a Pod with two Init Containers might show the following:

```
Init Containers:
  <init-container-1>:
    Container ID:    ...
    ...
    State:           Terminated
      Reason:        Completed
      Exit Code:     0
      Started:       ...
      Finished:      ...
    Ready:           True
    Restart Count:   0
    ...
  <init-container-2>:
    Container ID:    ...
    ...
    State:           Waiting
      Reason:        CrashLoopBackOff
    Last State:      Terminated
      Reason:        Error
      Exit Code:     1
      Started:       ...
      Finished:      ...
    Ready:           False
    Restart Count:   3
    ...
```

You can also access the Init Container statuses programmatically by reading the
`status.initContainerStatuses` field on the Pod Spec:

```shell
kubectl get pod <pod-name> --template '{{.status.initContainerStatuses}}'
```

This command will return the same information as above, formatted using a Go template.
