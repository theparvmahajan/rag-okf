---
id: okf-structure/concepts/workloads/pods/pod-qos.md#some-behavior-is-independent-of-qos-class-class-independent-behavior
kind: section
title: Some behavior is independent of QoS class {#class-independent-behavior}
source: concepts/workloads/pods/pod-qos.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
heading: Some behavior is independent of QoS class {#class-independent-behavior}
parent: okf-structure/concepts/workloads/pods/pod-qos
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#memory-qos-with-cgroup-v2
next_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#whatsnext
word_count: 197
---

Certain behavior is independent of the QoS class assigned by Kubernetes. For example:

* Any Container exceeding a resource limit will be killed and restarted by the kubelet without
  affecting other Containers in that Pod.

* If a Container exceeds its resource request and the node it runs on faces
  resource pressure, the Pod it is in becomes a candidate for eviction.
  If this occurs, all Containers in the Pod will be terminated. Kubernetes may create a
  replacement Pod, usually on a different node.

* The resource request of a Pod is equal to the sum of the resource requests of
  its component Containers, and the resource limit of a Pod is equal to the sum of
  the resource limits of its component Containers.

* The kube-scheduler does not consider QoS class when selecting which Pods to
  preempt.
  Preemption can occur when a cluster does not have enough resources to run all the Pods
  you defined.

* The QoS class is determined when the Pod is created and remains unchanged for the
  lifetime of the Pod. If you later attempt an
  in-place resize
  that would result in a different QoS class, the resize is rejected by admission.
