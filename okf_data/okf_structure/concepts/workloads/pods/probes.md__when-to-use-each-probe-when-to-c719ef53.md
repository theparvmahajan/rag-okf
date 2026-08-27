---
id: okf-structure/concepts/workloads/pods/probes.md#when-to-use-each-probe-when-to-use-each-probe
kind: section
title: When to use each probe {#when-to-use-each-probe}
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: When to use each probe {#when-to-use-each-probe}
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: okf-structure/concepts/workloads/pods/probes.md#types-of-probe-types-of-probe
next_sibling: okf-structure/concepts/workloads/pods/probes.md#check-mechanisms-check-mechanisms
word_count: 449
---

### When should you use a startup probe? {#when-should-you-use-a-startup-probe}

Startup probes are useful for Pods that have containers that take a long time to
come into service. Rather than set a long liveness interval, you can configure a
separate configuration for probing the container as it starts up, allowing a
time longer than the liveness interval would allow.

If your container usually starts in more than
\\( initialDelaySeconds + failureThreshold \times  periodSeconds \\), you should specify a
startup probe that checks the same endpoint as the liveness probe. The default
for `periodSeconds` is 10s. You should then set its `failureThreshold` high
enough to allow the container to start, without changing the default values of
the liveness probe. This helps to protect against deadlocks.

### When should you use a liveness probe? {#when-should-you-use-a-liveness-probe}

If the process in your container is able to crash on its own whenever it
encounters an issue or becomes unhealthy, you do not necessarily need a liveness
probe; the kubelet will automatically perform the correct action in accordance
with the Pod's `restartPolicy`.

If you'd like your container to be killed and restarted if a probe fails, then
specify a liveness probe, and specify a `restartPolicy` of `Always` or
`OnFailure`.

A common pattern for liveness probes is to use the same low-cost HTTP endpoint
as for readiness probes, but with a higher `failureThreshold`. This ensures
that the pod is observed as not-ready for some period of time before it is hard
killed.

### When should you use a readiness probe? {#when-should-you-use-a-readiness-probe}

To start sending traffic to a Pod only when a probe succeeds, specify a
readiness probe. The readiness probe might be the same as the liveness probe,
but the existence of the readiness probe in the spec means that the Pod will
start without receiving any traffic and only start receiving traffic after the
probe starts succeeding.

You can also use a readiness probe to let a container take itself down for
maintenance, by checking an endpoint specific to readiness that is different
from the liveness probe.

When your app has a strict dependency on back-end services, you can implement
both a liveness and a readiness probe. The liveness probe passes when the app
itself is healthy, but the readiness probe additionally checks that each
required back-end service is available. This helps you avoid directing traffic
to Pods that can only respond with error messages.

For containers that need to work on loading large data, configuration files, or
migrations during startup, consider using a startup probe.
However, if you want to detect the difference between an app that has failed
and an app that is still processing its startup data, you might prefer a readiness probe.
