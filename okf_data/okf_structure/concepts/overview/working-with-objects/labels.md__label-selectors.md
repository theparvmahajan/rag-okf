---
id: okf-structure/concepts/overview/working-with-objects/labels.md#label-selectors
kind: section
title: Label selectors
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: Label selectors
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#syntax-and-character-set
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#api
word_count: 536
---

Unlike names and UIDs, labels
do not provide uniqueness. In general, we expect many objects to carry the same label(s).

Via a _label selector_, the client/user can identify a set of objects.
The label selector is the core grouping primitive in Kubernetes.

The API currently supports two types of selectors: _equality-based_ and _set-based_.
A label selector can be made of multiple _requirements_ which are comma-separated.
In the case of multiple requirements, all must be satisfied so the comma separator
acts as a logical _AND_ (`&&`) operator.

The semantics of empty or non-specified selectors are dependent on the context,
and API types that use selectors should document the validity and meaning of
them.

For some API types, such as ReplicaSets, the label selectors of two instances must
not overlap within a namespace, or the controller can see that as conflicting
instructions and fail to determine how many replicas should be present.

For both equality-based and set-based conditions there is no logical _OR_ (`||`) operator.
Ensure your filter statements are structured accordingly.

### _Equality-based_ requirement

_Equality-_ or _inequality-based_ requirements allow filtering by label keys and values.
Matching objects must satisfy all of the specified label constraints, though they may
have additional labels as well. Three kinds of operators are admitted `=`,`==`,`!=`.
The first two represent _equality_ (and are synonyms), while the latter represents _inequality_.
For example:

```
environment = production
tier != frontend
```

The former selects all resources with key equal to `environment` and value equal to `production`.
The latter selects all resources with key equal to `tier` and value distinct from `frontend`,
and all resources with no labels with the `tier` key. One could filter for resources in `production`
excluding `frontend` using the comma operator: `environment=production,tier!=frontend`

One usage scenario for equality-based label requirement is for Pods to specify
node selection criteria. For example, the sample Pod below selects nodes where
the `accelerator` label exists and is set to `nvidia-tesla-p100`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
    - name: cuda-test
      image: "registry.k8s.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1
  nodeSelector:
    accelerator: nvidia-tesla-p100
```

### _Set-based_ requirement

_Set-based_ label requirements allow filtering keys according to a set of values.
Three kinds of operators are supported: `in`,`notin` and `exists` (only the key identifier).
For example:

```
environment in (production, qa)
tier notin (frontend, backend)
partition
!partition
```

- The first example selects all resources with key equal to `environment` and value
  equal to `production` or `qa`.
- The second example selects all resources with key equal to `tier` and values other
  than `frontend` and `backend`, and all resources with no labels with the `tier` key.
- The third example selects all resources including a label with key `partition`;
  no values are checked.
- The fourth example selects all resources without a label with key `partition`;
  no values are checked.

Similarly the comma separator acts as an _AND_ operator. So filtering resources
with a `partition` key (no matter the value) and with `environment` different
than `qa` can be achieved using `partition,environment notin (qa)`.
The _set-based_ label selector is a general form of equality since
`environment=production` is equivalent to `environment in (production)`;
similarly for `!=` and `notin`.

_Set-based_ requirements can be mixed with _equality-based_ requirements.
For example: `partition in (customerA, customerB),environment!=qa`.
