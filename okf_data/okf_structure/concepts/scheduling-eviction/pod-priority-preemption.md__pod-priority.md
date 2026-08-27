---
id: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#pod-priority
kind: section
title: Pod priority
source: concepts/scheduling-eviction/pod-priority-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
heading: Pod priority
parent: okf-structure/concepts/scheduling-eviction/pod-priority-preemption
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#non-preempting-priorityclass-non-preempting-priority-class
next_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#preemption
word_count: 185
---

After you have one or more PriorityClasses, you can create Pods that specify one
of those PriorityClass names in their specifications. The priority admission
controller uses the `priorityClassName` field and populates the integer value of
the priority. If the priority class is not found, the Pod is rejected.

The following YAML is an example of a Pod configuration that uses the
PriorityClass created in the preceding example. The priority admission
controller checks the specification and resolves the priority of the Pod to
1000000.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  priorityClassName: high-priority
```

### Effect of Pod priority on scheduling order

When Pod priority is enabled, the scheduler orders pending Pods by
their priority and a pending Pod is placed ahead of other pending Pods
with lower priority in the scheduling queue. As a result, the higher
priority Pod may be scheduled sooner than Pods with lower priority if
its scheduling requirements are met. If such Pod cannot be scheduled, the
scheduler will continue and try to schedule other lower priority Pods.
