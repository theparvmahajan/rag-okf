---
id: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#discussion
kind: section
title: Discussion
source: tasks/access-application-cluster/port-forward-access-application-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/
heading: Discussion
parent: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#forward-a-local-port-to-a-port-on-the-pod
next_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#authorization-and-security-considerations
word_count: 59
---

Connections made to local port 28015 are forwarded to port 27017 of the Pod that
is running the MongoDB server. With this connection in place, you can use your
local workstation to debug the database that is running in the Pod.

`kubectl port-forward` is implemented for TCP ports only.
The support for UDP protocol is tracked in
issue 47862.
