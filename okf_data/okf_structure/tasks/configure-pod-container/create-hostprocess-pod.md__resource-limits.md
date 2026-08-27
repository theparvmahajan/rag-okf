---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#resource-limits
kind: section
title: Resource limits
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Resource limits
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#volume-mounts
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#choosing-a-user-account
word_count: 89
---

Resource limits (disk, memory, cpu count) are applied to the job and are job wide.
For example, with a limit of 10MB set, the memory allocated for any HostProcess job object
will be capped at 10MB. This is the same behavior as other Windows container types.
These limits would be specified the same way they are currently for whatever orchestrator
or runtime is being used. The only difference is in the disk resource usage calculation
used for resource tracking due to the difference in how HostProcess containers are bootstrapped.
