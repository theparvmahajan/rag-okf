---
id: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling.md#api-configuration-scheduling-constraints
kind: section
title: 'API configuration: scheduling constraints'
source: concepts/workloads/workload-api/topology-aware-scheduling.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
heading: 'API configuration: scheduling constraints'
parent: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling
children: []
prev_sibling: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling.md#topology-aware-scheduling-with-basic-scheduling-policy
next_sibling: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling.md#whatsnext
word_count: 147
---

Every PodGroup (or PodGroupTemplate) may optionally declare the `schedulingConstraints` field,
which is interpreted by the placement-based PodGroup scheduling algorithm.
If constraints are defined in PodGroupTemplate, they will be copied to referencing PodGroups.

As of Kubernetes v1.36, the API supports topology constraints.

As of Kubernetes v1.36, you can specify only a single topology constraint in each PodGroup.

### Topology constraint

To define a topology constraint for a PodGroup you need to set a `key`, which corresponds to
a Kubernetes node label, representing the target topology domain (for example, a rack or a zone).
The scheduler strictly enforces that all pods within the PodGroup are placed onto nodes that share
the exact same value for this specified label.

Here is an example of a PodGroup configured with a topology constraint:

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: example-podgroup
spec:
  schedulingPolicy:
    gang:
      minCount: 4
  schedulingConstraints:
    topology:
      - key: topology.example.com/rack
```
