---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-horizontalpodautoscaler-in-kubectl
kind: section
title: Support for HorizontalPodAutoscaler in kubectl
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Support for HorizontalPodAutoscaler in kubectl
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#configurable-scaling-behavior
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#implicit-maintenance-mode-deactivation
word_count: 96
---

HorizontalPodAutoscaler, like every API resource, is supported in a standard way by `kubectl`.
You can create a new autoscaler using `kubectl create` command.
You can list autoscalers by `kubectl get hpa` or get detailed description by `kubectl describe hpa`.
Finally, you can delete an autoscaler using `kubectl delete hpa`.

In addition, there is a special `kubectl autoscale` command for creating a HorizontalPodAutoscaler object.
For instance, executing `kubectl autoscale rs foo --min=2 --max=5 --cpu=80%`
will create an autoscaler for ReplicaSet _foo_, with target CPU utilization set to `80%`
and the number of replicas between 2 and 5.
