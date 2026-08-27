---
id: okf-structure/concepts/workloads/pods/probes.md#check-mechanisms-check-mechanisms
kind: section
title: Check mechanisms {#check-mechanisms}
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: Check mechanisms {#check-mechanisms}
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: okf-structure/concepts/workloads/pods/probes.md#when-to-use-each-probe-when-to-use-each-probe
next_sibling: okf-structure/concepts/workloads/pods/probes.md#probe-results-probe-results
word_count: 239
---

There are four different ways to check a container using a probe. Each probe
must define exactly one of these four mechanisms:

`exec`
: Executes a specified command inside the container. The diagnostic is
  considered successful if the command exits with a status code of 0.

`grpc`
: Performs a remote procedure call using gRPC. The target
  should implement gRPC health checks.
  The diagnostic is considered successful if the `status` of the response is
  `SERVING`. For more details, see gRPC probes.

`httpGet`
: Performs an HTTP `GET` request against the Pod's IP address on a specified
  port and path. The diagnostic is considered successful if the response has a
  status code greater than or equal to 200 and less than 400.
  For more details, see HTTP probes.

`tcpSocket`
: Performs a TCP check against the Pod's IP address on a specified port. The
  diagnostic is considered successful if the port is open. If the remote system
  (the container) closes the connection immediately after it opens, this counts
  as healthy.
  For more details, see TCP probes.

Unlike the other mechanisms, `exec` probe's implementation involves the
creation/forking of multiple processes each time when executed. As a result, in
case of the clusters having higher pod densities, lower intervals of
`initialDelaySeconds`, `periodSeconds`, configuring any probe with exec
mechanism might introduce an overhead on the cpu usage of the node. In such
scenarios, consider using the alternative probe mechanisms to avoid the overhead.
