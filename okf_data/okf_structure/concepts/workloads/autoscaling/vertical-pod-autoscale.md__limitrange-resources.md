---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#limitrange-resources
kind: section
title: LimitRange resources
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: LimitRange resources
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#resource-policies
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#whatsnext
word_count: 73
---

The admission controller and updater VPA components post-process recommendations to comply with the constraints defined in LimitRanges. The LimitRange resources with `type` Pod and Container are checked in the Kubernetes cluster. 

For example, if the `max` field in a Container LimitRange resource is exceeded, both VPA components lower the limit to the value defined in the `max` field, and the request is proportionally decreased to maintain the request-to-limit ratio in the Pod spec.
