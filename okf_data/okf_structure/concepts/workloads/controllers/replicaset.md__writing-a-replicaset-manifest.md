---
id: okf-structure/concepts/workloads/controllers/replicaset.md#writing-a-replicaset-manifest
kind: section
title: Writing a ReplicaSet manifest
source: concepts/workloads/controllers/replicaset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
heading: Writing a ReplicaSet manifest
parent: okf-structure/concepts/workloads/controllers/replicaset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#non-template-pod-acquisitions
next_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#working-with-replicasets
word_count: 264
---

As with all other Kubernetes API objects, a ReplicaSet needs the `apiVersion`, `kind`, and `metadata` fields.
For ReplicaSets, the `kind` is always a ReplicaSet.

When the control plane creates new Pods for a ReplicaSet, the `.metadata.name` of the
ReplicaSet is part of the basis for naming those Pods. The name of a ReplicaSet must be a valid
DNS subdomain
value, but this can produce unexpected results for the Pod hostnames. For best compatibility,
the name should follow the more restrictive rules for a
DNS label.

A ReplicaSet also needs a `.spec` section.

### Pod Template

The `.spec.template` is a pod template which is also
required to have labels in place. In our `frontend.yaml` example we had one label: `tier: frontend`.
Be careful not to overlap with the selectors of other controllers, lest they try to adopt this Pod.

For the template's restart policy field,
`.spec.template.spec.restartPolicy`, the only allowed value is `Always`, which is the default.

### Pod Selector

The `.spec.selector` field is a label selector. As discussed
earlier these are the labels used to identify potential Pods to acquire. In our
`frontend.yaml` example, the selector was:

```yaml
matchLabels:
  tier: frontend
```

In the ReplicaSet, `.spec.template.metadata.labels` must match `spec.selector`, or it will
be rejected by the API.

For 2 ReplicaSets specifying the same `.spec.selector` but different
`.spec.template.metadata.labels` and `.spec.template.spec` fields, each ReplicaSet ignores the
Pods created by the other ReplicaSet.

### Replicas

You can specify how many Pods should run concurrently by setting `.spec.replicas`. The ReplicaSet will create/delete
its Pods to match this number.

If you do not specify `.spec.replicas`, then it defaults to 1.
