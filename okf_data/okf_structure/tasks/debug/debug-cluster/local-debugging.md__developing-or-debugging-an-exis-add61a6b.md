---
id: okf-structure/tasks/debug/debug-cluster/local-debugging.md#developing-or-debugging-an-existing-service
kind: section
title: Developing or debugging an existing service
source: tasks/debug/debug-cluster/local-debugging.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/
heading: Developing or debugging an existing service
parent: okf-structure/tasks/debug/debug-cluster/local-debugging
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#connecting-your-local-machine-to-a-remote-kubernetes-cluster
next_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#how-does-telepresence-work
word_count: 164
---

When developing an application on Kubernetes, you typically program
or debug a single service. The service might require access to other
services for testing and debugging. One option is to use the continuous
deployment pipeline, but even the fastest deployment pipeline introduces
a delay in the program or debug cycle.
 
Use the `telepresence intercept $SERVICE_NAME --port $LOCAL_PORT:$REMOTE_PORT`
command to create an "intercept" for rerouting remote service traffic.
 
Where:

-   `$SERVICE_NAME`  is the name of your local service
-   `$LOCAL_PORT` is the port that your service is running on your local workstation
-   And `$REMOTE_PORT` is the port your service listens to in the cluster

Running this command tells Telepresence to send remote traffic to your
local service instead of the service in the remote Kubernetes cluster.
Make edits to your service source code locally, save, and see the corresponding
changes when accessing your remote application take effect immediately.
You can also run your local service using a debugger or any other local development tool.
