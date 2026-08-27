---
id: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#customizing-the-termination-message
kind: section
title: Customizing the termination message
source: tasks/debug/debug-application/determine-reason-pod-failure.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/
heading: Customizing the termination message
parent: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#writing-and-reading-a-termination-message
next_sibling: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#whatsnext
word_count: 247
---

Kubernetes retrieves termination messages from the termination message file
specified in the `terminationMessagePath` field of a Container, which has a default
value of `/dev/termination-log`. By customizing this field, you can tell Kubernetes
to use a different file. Kubernetes use the contents from the specified file to
populate the Container's status message on both success and failure.

The termination message is intended to be brief final status, such as an assertion failure message.
The kubelet truncates messages that are longer than 4096 bytes.

The total message length across all containers is limited to 12KiB, divided equally among each container.
For example, if there are 12 containers (`initContainers` or `containers`), each has 1024 bytes of available termination message space.

The default termination message path is `/dev/termination-log`.
You cannot set the termination message path after a Pod is launched.

In the following example, the container writes termination messages to
`/tmp/my-log` for Kubernetes to retrieve:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: msg-path-demo
spec:
  containers:
  - name: msg-path-demo-container
    image: debian
    terminationMessagePath: "/tmp/my-log"
```

Moreover, users can set the `terminationMessagePolicy` field of a Container for
further customization. This field defaults to "`File`" which means the termination
messages are retrieved only from the termination message file. By setting the
`terminationMessagePolicy` to "`FallbackToLogsOnError`", you can tell Kubernetes
to use the last chunk of container log output if the termination message file
is empty and the container exited with an error. The log output is limited to
2048 bytes or 80 lines, whichever is smaller.
