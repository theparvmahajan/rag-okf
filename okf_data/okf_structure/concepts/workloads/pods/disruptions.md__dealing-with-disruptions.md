---
id: okf-structure/concepts/workloads/pods/disruptions.md#dealing-with-disruptions
kind: section
title: Dealing with disruptions
source: concepts/workloads/pods/disruptions.md
url: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
heading: Dealing with disruptions
parent: okf-structure/concepts/workloads/pods/disruptions
children: []
prev_sibling: okf-structure/concepts/workloads/pods/disruptions.md#voluntary-and-involuntary-disruptions
next_sibling: okf-structure/concepts/workloads/pods/disruptions.md#pod-disruption-budgets
word_count: 156
---

Here are some ways to mitigate involuntary disruptions:

- Ensure your pod requests the resources it needs.
- Replicate your application if you need higher availability.  (Learn about running replicated
  stateless
  and stateful applications.)
- For even higher availability when running replicated applications,
  spread applications across racks (using
  anti-affinity)
  or across zones (if using a
  multi-zone cluster.)

The frequency of voluntary disruptions varies.  On a basic Kubernetes cluster, there are
no automated voluntary disruptions (only user-triggered ones).  However, your cluster administrator or hosting provider
may run some additional services which cause voluntary disruptions. For example,
rolling out node software updates can cause voluntary disruptions. Also, some implementations
of cluster (node) autoscaling may cause voluntary disruptions to defragment and compact nodes.
Your cluster administrator or hosting provider should have documented what level of voluntary
disruptions, if any, to expect. Certain configuration options, such as
using PriorityClasses
in your pod spec can also cause voluntary (and involuntary) disruptions.
