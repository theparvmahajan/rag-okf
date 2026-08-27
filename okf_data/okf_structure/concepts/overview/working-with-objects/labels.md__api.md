---
id: okf-structure/concepts/overview/working-with-objects/labels.md#api
kind: section
title: API
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: API
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#label-selectors
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#using-labels-effectively
word_count: 440
---

### LIST and WATCH filtering

For **list** and **watch** operations, you can specify label selectors to filter the sets of objects
returned; you specify the filter using a query parameter.
(To learn in detail about watches in Kubernetes, read
efficient detection of changes).
Both requirements are permitted
(presented here as they would appear in a URL query string):

* _equality-based_ requirements: `?labelSelector=environment%3Dproduction,tier%3Dfrontend`
* _set-based_ requirements: `?labelSelector=environment+in+%28production%2Cqa%29%2Ctier+in+%28frontend%29`

Both label selector styles can be used to list or watch resources via a REST client.
For example, targeting `apiserver` with `kubectl` and using _equality-based_ one may write:

```shell
kubectl get pods -l environment=production,tier=frontend
```

or using _set-based_ requirements:

```shell
kubectl get pods -l 'environment in (production),tier in (frontend)'
```

As already mentioned _set-based_ requirements are more expressive.
For instance, they can implement the _OR_ operator on values:

```shell
kubectl get pods -l 'environment in (production, qa)'
```

or restricting negative matching via _notin_ operator:

```shell
kubectl get pods -l 'environment,environment notin (frontend)'
```

### Set references in API objects

Some Kubernetes objects, such as `services`
and `replicationcontrollers`,
also use label selectors to specify sets of other resources, such as
pods.

#### Service and ReplicationController

The set of pods that a `service` targets is defined with a label selector.
Similarly, the population of pods that a `replicationcontroller` should
manage is also defined with a label selector.

Label selectors for both objects are defined in `json` or `yaml` files using maps,
and only _equality-based_ requirement selectors are supported:

```json
"selector": {
    "component" : "redis",
}
```

or

```yaml
selector:
  component: redis
```

This selector (respectively in `json` or `yaml` format) is equivalent to
`component=redis` or `component in (redis)`.

#### Resources that support set-based requirements

Newer resources, such as `Job`,
`Deployment`,
`ReplicaSet`, and
`DaemonSet`,
support _set-based_ requirements as well.

```yaml
selector:
  matchLabels:
    component: redis
  matchExpressions:
    - { key: tier, operator: In, values: [cache] }
    - { key: environment, operator: NotIn, values: [dev] }
```

`matchLabels` is a map of `{key,value}` pairs. A single `{key,value}` in the
`matchLabels` map is equivalent to an element of `matchExpressions`, whose `key`
field is "key", the `operator` is "In", and the `values` array contains only "value".
`matchExpressions` is a list of pod selector requirements. Valid operators include
In, NotIn, Exists, and DoesNotExist. The values set must be non-empty in the case of
In and NotIn. All of the requirements, from both `matchLabels` and `matchExpressions`
are ANDed together -- they must all be satisfied in order to match.

#### Selecting sets of nodes

One use case for selecting over labels is to constrain the set of nodes onto which
a pod can schedule. See the documentation on
node selection for more information.
