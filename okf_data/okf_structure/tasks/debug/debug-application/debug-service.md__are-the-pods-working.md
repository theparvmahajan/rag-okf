---
id: okf-structure/tasks/debug/debug-application/debug-service.md#are-the-pods-working
kind: section
title: Are the Pods working?
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: Are the Pods working?
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-have-any-endpointslices
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#is-the-kube-proxy-working
word_count: 128
---

At this point, you know that your Service exists and has selected your Pods.
At the beginning of this walk-through, you verified the Pods themselves.
Let's check again that the Pods are actually working - you can bypass the
Service mechanism and go straight to the Pods, as listed by the Endpoints
above.

These commands use the Pod port (9376), rather than the Service port (80).

From within a Pod:

```shell
for ep in 10.244.0.5:9376 10.244.0.6:9376 10.244.0.7:9376; do
    wget -qO- $ep
done
```

This should produce something like:

```
hostnames-632524106-bbpiw
hostnames-632524106-ly40y
hostnames-632524106-tlaok
```

You expect each Pod in the endpoints list to return its own hostname.  If
this is not what happens (or whatever the correct behavior is for your own
Pods), you should investigate what's happening there.
