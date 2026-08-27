---
id: okf-structure/concepts/workloads/podgroup-api/_index.md#api-structure
kind: section
title: API structure
source: concepts/workloads/podgroup-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
heading: API structure
parent: okf-structure/concepts/workloads/podgroup-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#what-is-a-podgroup
next_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#creating-a-podgroup
word_count: 307
---

A PodGroup consists of a `spec` that defines the desired scheduling behavior and
a `status` that reflects the current scheduling state.

### Scheduling policy

Each PodGroup carries a scheduling policy
(`basic` or `gang`) in `spec.schedulingPolicy`. When a workload controller creates
the PodGroup, this policy is copied from the Workload's PodGroupTemplate at creation time.
For standalone PodGroups, you set the policy directly.

```yaml
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

### Template reference

The optional `spec.podGroupTemplateRef` links the PodGroup back to the PodGroupTemplate
in the Workload it was created from. This is useful for observability and tooling.

```yaml
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
```

### Requesting DRA devices for a PodGroup

Devices available through
Dynamic Resource Allocation (DRA)
can be requested by a PodGroup through its `spec.resourceClaims` field:

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: training-group
  namespace: some-ns
spec:
  ...
  resourceClaims:
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
```

ResourceClaims
associated with PodGroups can be shared by all Pods belonging to the group. With
only a reference to the PodGroup in the ResourceClaim's `status.reservedFor`
instead of each individual Pod, any number of Pods in the same PodGroup can
share a ResourceClaim. ResourceClaims can also be generated from
ResourceClaimTemplates
for each PodGroup, allowing the devices allocated to each generated
ResourceClaim to be shared by the Pods in each PodGroup.

For more details and a more complete example, see the
DRA documentation.

### Status

The scheduler updates `status.conditions` to report whether the group has been
successfully scheduled. The primary condition is `PodGroupScheduled`, which is `True`
when all required Pods have been placed and `False` when scheduling fails.

The `PodGroupScheduled` condition reflects the initial scheduling decision only.
The scheduler does not update it if Pods later fail or are evicted. See
Limitations
for details.

See the PodGroup lifecycle
page for the full list of conditions and reasons.
