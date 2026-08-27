---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#volume-mounts
kind: section
title: Volume mounts
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Volume mounts
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#hostprocess-pod-configuration-requirements
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#resource-limits
word_count: 164
---

HostProcess containers support the ability to mount volumes within the container volume space.
Volume mount behavior differs depending on the version of containerd runtime used by on the node.

### Containerd v1.6

Applications running inside the container can access volume mounts directly via relative or
absolute paths. An environment variable `$CONTAINER_SANDBOX_MOUNT_POINT` is set upon container
creation and provides the absolute host path to the container volume. Relative paths are based
upon the `.spec.containers.volumeMounts.mountPath` configuration.

To access service account tokens (for example) the following path structures are supported within the container:

- `.\var\run\secrets\kubernetes.io\serviceaccount\`
- `$CONTAINER_SANDBOX_MOUNT_POINT\var\run\secrets\kubernetes.io\serviceaccount\`

### Containerd v1.7 (and greater)

Applications running inside the container can access volume mounts directly via the volumeMount's
specified `mountPath` (just like Linux and non-HostProcess Windows containers).

For backwards compatibility volumes can also be accessed via using the same relative paths configured
by containerd v1.6.

As an example, to access service account tokens within the container you would use one of the following paths:

- `c:\var\run\secrets\kubernetes.io\serviceaccount`
- `/var/run/secrets/kubernetes.io/serviceaccount/`
- `$CONTAINER_SANDBOX_MOUNT_POINT\var\run\secrets\kubernetes.io\serviceaccount\`
