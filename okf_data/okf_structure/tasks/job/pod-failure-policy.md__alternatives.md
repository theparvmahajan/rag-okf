---
id: okf-structure/tasks/job/pod-failure-policy.md#alternatives
kind: section
title: Alternatives
source: tasks/job/pod-failure-policy.md
url: https://kubernetes.io/docs/tasks/job/pod-failure-policy/
heading: Alternatives
parent: okf-structure/tasks/job/pod-failure-policy
children: []
prev_sibling: okf-structure/tasks/job/pod-failure-policy.md#usage-scenarios
next_sibling: null
word_count: 54
---

You could rely solely on the
Pod backoff failure policy,
by specifying the Job's `.spec.backoffLimit` field. However, in many situations
it is problematic to find a balance between setting a low value for `.spec.backoffLimit`
 to avoid unnecessary Pod retries, yet high enough to make sure the Job would
not be terminated by Pod disruptions.
