---
id: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#define-poststart-and-prestop-handlers
kind: section
title: Define postStart and preStop handlers
source: tasks/configure-pod-container/attach-handler-lifecycle-event.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/
heading: Define postStart and preStop handlers
parent: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/attach-handler-lifecycle-event.md#discussion
word_count: 135
---

In this exercise, you create a Pod that has one Container. The Container has handlers
for the postStart and preStop events.

Here is the configuration file for the Pod:

In the configuration file, you can see that the postStart command writes a `message`
file to the Container's `/usr/share` directory. The preStop command shuts down
nginx gracefully. This is helpful if the Container is being terminated because of a failure.

Create the Pod:

    kubectl apply -f https://k8s.io/examples/pods/lifecycle-events.yaml

Verify that the Container in the Pod is running:

    kubectl get pod lifecycle-demo

Get a shell into the Container running in your Pod:

    kubectl exec -it lifecycle-demo -- /bin/bash

In your shell, verify that the `postStart` handler created the `message` file:

    root@lifecycle-demo:/# cat /usr/share/message

The output shows the text written by the postStart handler:

    Hello from the postStart handler
