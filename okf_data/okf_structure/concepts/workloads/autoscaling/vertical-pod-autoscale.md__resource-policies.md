---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#resource-policies
kind: section
title: Resource policies
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: Resource policies
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#update-modes
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#limitrange-resources
word_count: 245
---

Resource policies allow you to fine-tune how the VerticalPodAutoscaler generates recommendations and applies updates.
You can set boundaries for resource recommendations, specify which resources to manage, and configure different policies for individual containers within a Pod.

You define resource policies in the `resourcePolicy` field of the VPA spec:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Recreate"
  resourcePolicy:
    containerPolicies:
    - containerName: "application"
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
      controlledResources:
      - cpu
      - memory
      controlledValues: RequestsAndLimits
```

#### minAllowed and maxAllowed

These fields set boundaries for VPA recommendations.
The VPA will never recommend resources below `minAllowed` or above `maxAllowed`, even if the actual usage data suggests different values.

#### controlledResources

The `controlledResources` field specifies which resource types VPA should manage for a container in a Pod.
If not specified, VPA manages both CPU and memory by default. You can restrict VPA to manage only specific resources.
Valid resource names include `cpu` and `memory`.

### controlledValues

The `controlledValues` field determines whether VPA controls resource requests, limits, or both:

RequestsAndLimits
: VPA sets both requests and limits. The limit scales proportionally to the request based on the request-to-limit ratio defined in the Pod spec. This is the default mode.

RequestsOnly
: VPA only sets requests, leaving limits unchanged. Limits are respected and can still trigger throttling or out-of-memory kills if usage exceeds them.

See requests and limits to learn more about those two concepts.
