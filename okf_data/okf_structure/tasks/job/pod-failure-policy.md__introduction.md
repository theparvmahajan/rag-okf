---
id: okf-structure/tasks/job/pod-failure-policy.md#introduction
kind: section
title: Handling retriable and non-retriable pod failures with Pod failure policy
source: tasks/job/pod-failure-policy.md
url: https://kubernetes.io/docs/tasks/job/pod-failure-policy/
heading: null
parent: okf-structure/tasks/job/pod-failure-policy
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/pod-failure-policy.md#prerequisites
word_count: 71
---

This document shows you how to use the
Pod failure policy,
in combination with the default
Pod backoff failure policy,
to improve the control over the handling of container- or Pod-level failure
within a Job.

The definition of Pod failure policy may help you to:
* better utilize the computational resources by avoiding unnecessary Pod retries.
* avoid Job failures due to Pod disruptions (such preemption,
API-initiated eviction
or taint-based eviction).
