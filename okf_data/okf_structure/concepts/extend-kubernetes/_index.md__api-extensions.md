---
id: okf-structure/concepts/extend-kubernetes/_index.md#api-extensions
kind: section
title: API extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: API extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#client-extensions
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#api-access-extensions
word_count: 224
---

### Custom resource definitions

Consider adding a _Custom Resource_ to Kubernetes if you want to define new controllers, application
configuration objects or other declarative APIs, and to manage them using Kubernetes tools, such
as `kubectl`.

For more about Custom Resources, see the
Custom Resources concept guide.

### API aggregation layer

You can use Kubernetes' API Aggregation Layer
to integrate the Kubernetes API with additional services such as for metrics.

### Combining new APIs with automation

A combination of a custom resource API and a control loop is called the
controllers pattern. If your controller takes
the place of a human operator deploying infrastructure based on a desired state, then the controller
may also be following the operator pattern.
The Operator pattern is used to manage specific applications; usually, these are applications that
maintain state and require care in how they are managed.

You can also make your own custom APIs and control loops that manage other resources, such as storage,
or to define policies (such as an access control restriction).

### Changing built-in resources

When you extend the Kubernetes API by adding custom resources, the added resources always fall
into a new API Groups. You cannot replace or change existing API groups.
Adding an API does not directly let you affect the behavior of existing APIs (such as Pods), whereas
_API Access Extensions_ do.
