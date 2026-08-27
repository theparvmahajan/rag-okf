---
id: okf-structure/concepts/workloads/podgroup-api/_index.md#how-it-fits-together
kind: section
title: How it fits together
source: concepts/workloads/podgroup-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
heading: How it fits together
parent: okf-structure/concepts/workloads/podgroup-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#creating-a-podgroup
next_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#whatsnext
word_count: 168
---

The relationship between controllers, Workloads, PodGroups, and Pods follows this pattern:

1. The workload controller creates a Workload that defines PodGroupTemplates with scheduling policies.
2. For each runtime instance, the controller creates a PodGroup from one of the Workload's PodGroupTemplates.
3. The controller creates Pods that reference the PodGroup
   via the `spec.schedulingGroup.podGroupName` field.

The Job controller is the only built-in
workload controller that follows this pattern for now.
Custom controllers can implement the same flow for their own workload types.

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: Workload
metadata:
  name: training-policy
spec:
  podGroupTemplates:
  - name: worker
    schedulingPolicy:
      gang:
        minCount: 4
---
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: training-worker-0
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
  schedulingPolicy:
    gang:
      minCount: 4
---
apiVersion: v1
kind: Pod
metadata:
  name: worker-0
spec:
  schedulingGroup:
    podGroupName: training-worker-0
  containers:
  - name: ml-worker
    image: training:v1
```

The Workload acts as a long-lived policy definition, while PodGroups handle the 
transient, per-instance runtime state. This separation means that status updates for
individual PodGroups do not contend on the shared Workload object.
