---
id: okf-structure/concepts/workloads/controllers/replicationcontroller.md#writing-a-replicationcontroller-manifest
kind: section
title: Writing a ReplicationController Manifest
source: concepts/workloads/controllers/replicationcontroller.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
heading: Writing a ReplicationController Manifest
parent: okf-structure/concepts/workloads/controllers/replicationcontroller
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#running-an-example-replicationcontroller
next_sibling: okf-structure/concepts/workloads/controllers/replicationcontroller.md#working-with-replicationcontrollers
word_count: 472
---

As with all other Kubernetes config, a ReplicationController needs `apiVersion`, `kind`, and `metadata` fields.

When the control plane creates new Pods for a ReplicationController, the `.metadata.name` of the
ReplicationController is part of the basis for naming those Pods.  The name of a ReplicationController must be a valid
DNS subdomain
value, but this can produce unexpected results for the Pod hostnames.  For best compatibility,
the name should follow the more restrictive rules for a
DNS label.

For general information about working with configuration files, see object management.

A ReplicationController also needs a `.spec` section.

### Pod Template

The `.spec.template` is the only required field of the `.spec`.

The `.spec.template` is a pod template. It has exactly the same schema as a Pod, except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a pod template in a ReplicationController must specify appropriate
labels and an appropriate restart policy. For labels, make sure not to overlap with other controllers. See pod selector.

Only a `.spec.template.spec.restartPolicy` equal to `Always` is allowed, which is the default if not specified.

For local container restarts, ReplicationControllers delegate to an agent on the node,
for example the Kubelet.

### Labels on the ReplicationController

The ReplicationController can itself have labels (`.metadata.labels`).  Typically, you
would set these the same as the `.spec.template.metadata.labels`; if `.metadata.labels` is not specified
then it defaults to  `.spec.template.metadata.labels`. However, they are allowed to be
different, and the `.metadata.labels` do not affect the behavior of the ReplicationController.

### Pod Selector

The `.spec.selector` field is a label selector. A ReplicationController
manages all the pods with labels that match the selector. It does not distinguish
between pods that it created or deleted and pods that another person or process created or
deleted. This allows the ReplicationController to be replaced without affecting the running pods.

If specified, the `.spec.template.metadata.labels` must be equal to the `.spec.selector`, or it will
be rejected by the API.  If `.spec.selector` is unspecified, it will be defaulted to
`.spec.template.metadata.labels`.

Also you should not normally create any pods whose labels match this selector, either directly, with
another ReplicationController, or with another controller such as Job. If you do so, the
ReplicationController thinks that it created the other pods.  Kubernetes does not stop you
from doing this.

If you do end up with multiple controllers that have overlapping selectors, you
will have to manage the deletion yourself (see below).

### Multiple Replicas

You can specify how many pods should run concurrently by setting `.spec.replicas` to the number
of pods you would like to have running concurrently.  The number running at any time may be higher
or lower, such as if the replicas were just increased or decreased, or if a pod is gracefully
shutdown, and a replacement starts early.

If you do not specify `.spec.replicas`, then it defaults to 1.
