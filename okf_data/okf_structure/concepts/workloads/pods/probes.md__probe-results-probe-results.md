---
id: okf-structure/concepts/workloads/pods/probes.md#probe-results-probe-results
kind: section
title: Probe results {#probe-results}
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: Probe results {#probe-results}
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: okf-structure/concepts/workloads/pods/probes.md#check-mechanisms-check-mechanisms
next_sibling: okf-structure/concepts/workloads/pods/probes.md#configuration-fields-configure-probes
word_count: 120
---

The kubelet evaluates the result of each probe execution and takes action
accordingly. Each probe has one of three results:

`Success`
: The container passed the diagnostic.

`Failure`
: The container failed the diagnostic. For liveness and startup probes, the
  kubelet kills the container, and the container is subjected to its
  restart policy.
  For readiness probes, the kubelet marks the container as not ready, and the
  Pod stops receiving traffic from matching Services.

`Unknown`
: The diagnostic failed (no action should be taken, and the kubelet will make
  further checks).

If a container does not provide a particular probe, the kubelet always
considers the result as `Success`. For readiness probes specifically,
the result is considered `Failure` before the initial delay.
