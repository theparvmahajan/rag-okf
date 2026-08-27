---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#troubleshooting-hostprocess-containers
kind: section
title: Troubleshooting HostProcess containers
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Troubleshooting HostProcess containers
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#base-image-for-hostprocess-containers
next_sibling: null
word_count: 51
---

- HostProcess containers fail to start with `failed to create user process token: failed to logon user: Access is denied.: unknown`

  Ensure containerd is running as `LocalSystem` or `LocalService` service accounts. User accounts (even Administrator accounts) do not have permissions to create logon tokens for any of the supported user accounts.
