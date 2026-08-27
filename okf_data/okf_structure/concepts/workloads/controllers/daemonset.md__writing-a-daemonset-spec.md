---
id: okf-structure/concepts/workloads/controllers/daemonset.md#writing-a-daemonset-spec
kind: section
title: Writing a DaemonSet Spec
source: concepts/workloads/controllers/daemonset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
heading: Writing a DaemonSet Spec
parent: okf-structure/concepts/workloads/controllers/daemonset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#how-daemon-pods-are-scheduled
word_count: 376
---

### Create a DaemonSet

You can describe a DaemonSet in a YAML file. For example, the `daemonset.yaml` file below
describes a DaemonSet that runs the fluentd-elasticsearch Docker image:

Create a DaemonSet based on the YAML file:

```
kubectl apply -f https://k8s.io/examples/controllers/daemonset.yaml
```

### Required Fields

As with all other Kubernetes config, a DaemonSet needs `apiVersion`, `kind`, and `metadata` fields.  For
general information about working with config files, see
running stateless applications
and object management using kubectl.

The name of a DaemonSet object must be a valid
DNS subdomain name.

A DaemonSet also needs a
`.spec`
section.

### Pod Template

The `.spec.template` is one of the required fields in `.spec`.

The `.spec.template` is a pod template.
It has exactly the same schema as a Pod,
except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a Pod template in a DaemonSet has to specify appropriate
labels (see pod selector).

A Pod Template in a DaemonSet must have a `RestartPolicy`
 equal to `Always`, or be unspecified, which defaults to `Always`.

### Pod Selector

The `.spec.selector` field is a pod selector.  It works the same as the `.spec.selector` of
a Job.

You must specify a pod selector that matches the labels of the
`.spec.template`.
Also, once a DaemonSet is created,
its `.spec.selector` can not be mutated. Mutating the pod selector can lead to the
unintentional orphaning of Pods, and it was found to be confusing to users.

The `.spec.selector` is an object consisting of two fields:

* `matchLabels` - works the same as the `.spec.selector` of a
  ReplicationController.
* `matchExpressions` - allows to build more sophisticated selectors by specifying key,
  list of values and an operator that relates the key and values.

When the two are specified the result is ANDed.

The `.spec.selector` must match the `.spec.template.metadata.labels`.
Config with these two not matching will be rejected by the API.

### Running Pods on select Nodes

If you specify a `.spec.template.spec.nodeSelector`, then the DaemonSet controller will
create Pods on nodes which match that node selector.
Likewise if you specify a `.spec.template.spec.affinity`,
then DaemonSet controller will create Pods on nodes which match that
node affinity.
If you do not specify either, then the DaemonSet controller will create Pods on all nodes.
