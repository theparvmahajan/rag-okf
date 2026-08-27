---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#concepts
kind: section
title: Concepts
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: Concepts
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#numeric-comparison-operators-numeric-comparison-operators
word_count: 884
---

You add a taint to a node using kubectl taint.
For example,

```shell
kubectl taint nodes node1 key1=value1:NoSchedule
```

places a taint on node `node1`. The taint has key `key1`, value `value1`, and taint effect `NoSchedule`.
This means that no pod will be able to schedule onto `node1` unless it has a matching toleration.

To remove the taint added by the command above, you can run:

```shell
kubectl taint nodes node1 key1=value1:NoSchedule-
```

You specify a toleration for a pod in the PodSpec. Both of the following tolerations "match" the
taint created by the `kubectl taint` line above, and thus a pod with either toleration would be able
to schedule onto `node1`:

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
```

```yaml
tolerations:
- key: "key1"
  operator: "Exists"
  effect: "NoSchedule"
```

The default Kubernetes scheduler takes taints and tolerations into account when
selecting a node to run a particular Pod. However, if you manually specify the
`.spec.nodeName` for a Pod, that action bypasses the scheduler; the Pod is then
bound onto the node where you assigned it, even if there are `NoSchedule`
taints on that node that you selected.
If this happens and the node also has a `NoExecute` taint set, the kubelet will
eject the Pod unless there is an appropriate tolerance set.

Here's an example of a pod that has some tolerations defined:

The default value for `operator` is `Equal`.

A toleration "matches" a taint if the keys are the same and the effects are the same, and:

* the `operator` is `Exists` (in which case no `value` should be specified), or
* the `operator` is `Equal` and the values should be equal.

There are two special cases:

If the `key` is empty, then the `operator` must be `Exists`, which matches all keys and values.
Note that the `effect` still needs to be matched at the same time.

An empty `effect` matches all effects with key `key1`.

The above example used the `effect` of `NoSchedule`. Alternatively, you can use the `effect` of `PreferNoSchedule`.

The allowed values for the `effect` field are:

`NoExecute`
: This affects pods that are already running on the node as follows:

  * Pods that do not tolerate the taint are evicted immediately
  * Pods that tolerate the taint without specifying `tolerationSeconds` in
    their toleration specification remain bound forever
  * Pods that tolerate the taint with a specified `tolerationSeconds` remain
    bound for the specified amount of time. After that time elapses, the node
    lifecycle controller evicts the Pods from the node.

`NoSchedule`
: No new Pods will be scheduled on the tainted node unless they have a matching
  toleration. Pods currently running on the node are **not** evicted.

`PreferNoSchedule`
: `PreferNoSchedule` is a "preference" or "soft" version of `NoSchedule`.
  The control plane will *try* to avoid placing a Pod that does not tolerate
  the taint on the node, but it is not guaranteed.

You can put multiple taints on the same node and multiple tolerations on the same pod.
The way Kubernetes processes multiple taints and tolerations is like a filter: start
with all of a node's taints, then ignore the ones for which the pod has a matching toleration; the
remaining un-ignored taints have the indicated effects on the pod. In particular,

* if there is at least one un-ignored taint with effect `NoSchedule` then Kubernetes will not schedule
the pod onto that node
* if there is no un-ignored taint with effect `NoSchedule` but there is at least one un-ignored taint with
effect `PreferNoSchedule` then Kubernetes will *try* to not schedule the pod onto the node
* if there is at least one un-ignored taint with effect `NoExecute` then the pod will be evicted from
the node (if it is already running on the node), and will not be
scheduled onto the node (if it is not yet running on the node).

For example, imagine you taint a node like this

```shell
kubectl taint nodes node1 key1=value1:NoSchedule
kubectl taint nodes node1 key1=value1:NoExecute
kubectl taint nodes node1 key2=value2:NoSchedule
```

And a pod has two tolerations:

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoSchedule"
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
```

In this case, the pod will not be able to schedule onto the node, because there is no
toleration matching the third taint. But it will be able to continue running if it is
already running on the node when the taint is added, because the third taint is the only
one of the three that is not tolerated by the pod.

Normally, if a taint with effect `NoExecute` is added to a node, then any pods that do
not tolerate the taint will be evicted immediately, and pods that do tolerate the
taint will never be evicted. However, a toleration with `NoExecute` effect can specify
an optional `tolerationSeconds` field that dictates how long the pod will stay bound
to the node after the taint is added. For example,

```yaml
tolerations:
- key: "key1"
  operator: "Equal"
  value: "value1"
  effect: "NoExecute"
  tolerationSeconds: 3600
```

means that if this pod is running and a matching taint is added to the node, then
the pod will stay bound to the node for 3600 seconds, and then be evicted. If the
taint is removed before that time, the pod will not be evicted.
