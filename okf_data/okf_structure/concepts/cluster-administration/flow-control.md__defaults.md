---
id: okf-structure/concepts/cluster-administration/flow-control.md#defaults
kind: section
title: Defaults
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Defaults
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#resources
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#health-check-concurrency-exemption
word_count: 865
---

Each kube-apiserver maintains two sorts of APF configuration objects:
mandatory and suggested.

### Mandatory Configuration Objects

The four mandatory configuration objects reflect fixed built-in
guardrail behavior. This is behavior that the servers have before
those objects exist, and when those objects exist their specs reflect
this behavior. The four mandatory objects are as follows.

* The mandatory `exempt` priority level is used for requests that are
  not subject to flow control at all: they will always be dispatched
  immediately. The mandatory `exempt` FlowSchema classifies all
  requests from the `system:masters` group into this priority
  level. You may define other FlowSchemas that direct other requests
  to this priority level, if appropriate.

* The mandatory `catch-all` priority level is used in combination with
  the mandatory `catch-all` FlowSchema to make sure that every request
  gets some kind of classification. Typically you should not rely on
  this catch-all configuration, and should create your own catch-all
  FlowSchema and PriorityLevelConfiguration (or use the suggested
  `global-default` priority level that is installed by default) as
  appropriate. Because it is not expected to be used normally, the
  mandatory `catch-all` priority level has a very small concurrency
  share and does not queue requests.

### Suggested Configuration Objects

The suggested FlowSchemas and PriorityLevelConfigurations constitute a
reasonable default configuration. You can modify these and/or create
additional configuration objects if you want. If your cluster is
likely to experience heavy load then you should consider what
configuration will work best.

The suggested configuration groups requests into six priority levels:

* The `node-high` priority level is for health updates from nodes.

* The `system` priority level is for non-health requests from the
  `system:nodes` group, i.e. Kubelets, which must be able to contact
  the API server in order for workloads to be able to schedule on
  them.

* The `leader-election` priority level is for leader election requests from
  built-in controllers (in particular, requests for `endpoints`, `configmaps`,
  or `leases` coming from the `system:kube-controller-manager` or
  `system:kube-scheduler` users and service accounts in the `kube-system`
  namespace). These are important to isolate from other traffic because failures
  in leader election cause their controllers to fail and restart, which in turn
  causes more expensive traffic as the new controllers sync their informers.

* The `workload-high` priority level is for other requests from built-in
  controllers.

* The `workload-low` priority level is for requests from any other service
  account, which will typically include all requests from controllers running in
  Pods.

* The `global-default` priority level handles all other traffic, e.g.
  interactive `kubectl` commands run by nonprivileged users.

The suggested FlowSchemas serve to steer requests into the above
priority levels, and are not enumerated here.

### Maintenance of the Mandatory and Suggested Configuration Objects

Each `kube-apiserver` independently maintains the mandatory and
suggested configuration objects, using initial and periodic behavior.
Thus, in a situation with a mixture of servers of different versions
there may be thrashing as long as different servers have different
opinions of the proper content of these objects.

Each `kube-apiserver` makes an initial maintenance pass over the
mandatory and suggested configuration objects, and after that does
periodic maintenance (once per minute) of those objects.

For the mandatory configuration objects, maintenance consists of
ensuring that the object exists and, if it does, has the proper spec.
The server refuses to allow a creation or update with a spec that is
inconsistent with the server's guardrail behavior.

Maintenance of suggested configuration objects is designed to allow
their specs to be overridden. Deletion, on the other hand, is not
respected: maintenance will restore the object. If you do not want a
suggested configuration object then you need to keep it around but set
its spec to have minimal consequences. Maintenance of suggested
objects is also designed to support automatic migration when a new
version of the `kube-apiserver` is rolled out, albeit potentially with
thrashing while there is a mixed population of servers.

Maintenance of a suggested configuration object consists of creating
it --- with the server's suggested spec --- if the object does not
exist. OTOH, if the object already exists, maintenance behavior
depends on whether the `kube-apiservers` or the users control the
object. In the former case, the server ensures that the object's spec
is what the server suggests; in the latter case, the spec is left
alone.

The question of who controls the object is answered by first looking
for an annotation with key `apf.kubernetes.io/autoupdate-spec`. If
there is such an annotation and its value is `true` then the
kube-apiservers control the object. If there is such an annotation
and its value is `false` then the users control the object. If
neither of those conditions holds then the `metadata.generation` of the
object is consulted. If that is 1 then the kube-apiservers control
the object. Otherwise the users control the object. These rules were
introduced in release 1.22 and their consideration of
`metadata.generation` is for the sake of migration from the simpler
earlier behavior. Users who wish to control a suggested configuration
object should set its `apf.kubernetes.io/autoupdate-spec` annotation
to `false`.

Maintenance of a mandatory or suggested configuration object also
includes ensuring that it has an `apf.kubernetes.io/autoupdate-spec`
annotation that accurately reflects whether the kube-apiservers
control the object.

Maintenance also includes deleting objects that are neither mandatory
nor suggested but are annotated
`apf.kubernetes.io/autoupdate-spec=true`.
