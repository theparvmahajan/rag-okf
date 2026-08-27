---
id: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#usage-example
kind: section
title: Usage example
source: concepts/scheduling-eviction/pod-scheduling-readiness.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
heading: Usage example
parent: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#configuring-pod-schedulinggates
next_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#observability
word_count: 176
---

To mark a Pod not-ready for scheduling, you can create it with one or more scheduling gates like this:

After the Pod's creation, you can check its state using:

```bash
kubectl get pod test-pod
```

The output reveals it's in `SchedulingGated` state:

```none
NAME       READY   STATUS            RESTARTS   AGE
test-pod   0/1     SchedulingGated   0          7s
```

You can also check its `schedulingGates` field by running:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.schedulingGates}'
```

The output is:

```none
[{"name":"example.com/foo"},{"name":"example.com/bar"}]
```

To inform scheduler this Pod is ready for scheduling, you can remove its `schedulingGates` entirely
by reapplying a modified manifest:

You can check if the `schedulingGates` is cleared by running:

```bash
kubectl get pod test-pod -o jsonpath='{.spec.schedulingGates}'
```

The output is expected to be empty. And you can check its latest status by running:

```bash
kubectl get pod test-pod -o wide
```

Given the test-pod doesn't request any CPU/memory resources, it's expected that this Pod's state get
transited from previous `SchedulingGated` to `Running`:

```none
NAME       READY   STATUS    RESTARTS   AGE   IP         NODE
test-pod   1/1     Running   0          15s   10.0.0.4   node-2
```
