---
id: okf-structure/tasks/manage-daemon/create-daemon-set.md#cleanup
kind: section
title: Cleanup
source: tasks/manage-daemon/create-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/create-daemon-set/
heading: Cleanup
parent: okf-structure/tasks/manage-daemon/create-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/create-daemon-set.md#define-the-daemonset
next_sibling: okf-structure/tasks/manage-daemon/create-daemon-set.md#whatsnext
word_count: 45
---

To delete the DaemonSet, run this command:

```shell
kubectl delete --cascade=foreground --ignore-not-found --now daemonsets/example-daemonset
```

This simple DaemonSet example introduces key components like init containers and host path volumes,
which can be expanded upon for more advanced use cases. For more details refer to
DaemonSet.
