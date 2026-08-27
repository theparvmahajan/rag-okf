---
id: okf-structure/tasks/manage-daemon/update-daemon-set.md#daemonset-update-strategy
kind: section
title: DaemonSet Update Strategy
source: tasks/manage-daemon/update-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/
heading: DaemonSet Update Strategy
parent: okf-structure/tasks/manage-daemon/update-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#prerequisites
next_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#performing-a-rolling-update
word_count: 99
---

DaemonSet has two update strategy types:

* `OnDelete`: With `OnDelete` update strategy, after you update a DaemonSet template, new
  DaemonSet pods will *only* be created when you manually delete old DaemonSet
  pods. This is the same behavior of DaemonSet in Kubernetes version 1.5 or
  before.
* `RollingUpdate`: This is the default update strategy.  
  With `RollingUpdate` update strategy, after you update a
  DaemonSet template, old DaemonSet pods will be killed, and new DaemonSet pods
  will be created automatically, in a controlled fashion. At most one pod of
  the DaemonSet will be running on each node during the whole update process.
