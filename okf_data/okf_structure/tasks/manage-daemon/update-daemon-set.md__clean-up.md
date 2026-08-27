---
id: okf-structure/tasks/manage-daemon/update-daemon-set.md#clean-up
kind: section
title: Clean up
source: tasks/manage-daemon/update-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/
heading: Clean up
parent: okf-structure/tasks/manage-daemon/update-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#troubleshooting
next_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#whatsnext
word_count: 14
---

Delete DaemonSet from a namespace :

```shell
kubectl delete ds fluentd-elasticsearch -n kube-system
```
