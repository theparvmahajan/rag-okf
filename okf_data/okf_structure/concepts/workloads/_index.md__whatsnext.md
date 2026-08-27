---
id: okf-structure/concepts/workloads/_index.md#whatsnext
kind: section
title: Whatsnext
source: concepts/workloads/_index.md
url: https://kubernetes.io/docs/concepts/workloads/
heading: Whatsnext
parent: okf-structure/concepts/workloads/_index
children: []
prev_sibling: okf-structure/concepts/workloads/_index.md#workload-placement
next_sibling: null
word_count: 135
---

As well as reading about each API kind for workload management, you can read how to
do specific tasks:

* Run a stateless application using a Deployment
* Run a stateful application either as a single instance
  or as a replicated set
* Run automated tasks with a CronJob

To learn about Kubernetes' mechanisms for separating code from configuration,
visit Configuration.

There are two supporting concepts that provide backgrounds about how Kubernetes manages pods
for applications:
* Garbage collection tidies up objects
  from your cluster after their _owning resource_ has been removed.
* The _time-to-live after finished_ controller
  removes Jobs once a defined time has passed since they completed.

Once your application is running, you might want to make it available on the internet as
a Service or, for web application only,
using an Ingress.
