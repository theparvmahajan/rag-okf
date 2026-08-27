---
id: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#whatsnext
kind: section
title: Whatsnext
source: tasks/configure-pod-container/configure-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-volume-storage/
heading: Whatsnext
parent: okf-structure/tasks/configure-pod-container/configure-volume-storage
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-volume-storage.md#configure-a-volume-for-a-pod
next_sibling: null
word_count: 57
---

- See Volume.

- See Pod.

- In addition to the local disk storage provided by `emptyDir`, Kubernetes
  supports many different network-attached storage solutions, including PD on
  GCE and EBS on EC2, which are preferred for critical data and will handle
  details such as mounting and unmounting the devices on the nodes. See
  Volumes for more details.
