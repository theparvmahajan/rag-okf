---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#performance-and-latency-performance-latency
kind: section
title: Performance and latency {#performance-latency}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Performance and latency {#performance-latency}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#choose-an-admission-control-mechanism-choose-admission-mechanism
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#request-filtering-request-filtering
word_count: 523
---

This section describes recommendations for improving performance and reducing
latency. In summary, these are as follows:

* Consolidate webhooks and limit the number of API calls per webhook.
* Use audit logs to check for webhooks that repeatedly do the same action.
* Use load balancing for webhook availability.
* Set a small timeout value for each webhook.
* Consider cluster availability needs during webhook design.

### Design admission webhooks for low latency {#design-admission-webhooks-low-latency}

Mutating admission webhooks are called in sequence. Depending on the mutating
webhook setup, some webhooks might be called multiple times. Every mutating
webhook call adds latency to the admission process. This is unlike validating
webhooks, which get called in parallel. 

When designing your mutating webhooks, consider your latency requirements and
tolerance. The more mutating webhooks there are in your cluster, the greater the
chance of latency increases. 

Consider the following to reduce latency:

* Consolidate webhooks that perform a similar mutation on different objects.
* Reduce the number of API calls made in the mutating webhook server logic.
* Limit the match conditions of each mutating webhook to reduce how many
  webhooks are triggered by a specific API request.
* Consolidate small webhooks into one server and configuration to help with
  ordering and organization.

### Prevent loops caused by competing controllers {#prevent-loops-competing-controllers}

Consider any other components that run in your cluster that might conflict with
the mutations that your webhook makes. For example, if your webhook adds a label
that a different controller removes, your webhook gets called again. This leads
to a loop.

To detect these loops, try the following:

1.  Update your cluster audit policy to log audit events. Use the following
    parameters:
    
      * `level`: `RequestResponse`
      * `verbs`: `["patch"]`
      * `omitStages`: `RequestReceived`

    Set the audit rule to create events for the specific resources that your
    webhook mutates.

1.  Check your audit events for webhooks being reinvoked multiple times with the
    same patch being applied to the same object, or for an object having
    a field updated and reverted multiple times.

### Set a small timeout value {#small-timeout}

Admission webhooks should evaluate as quickly as possible (typically in
milliseconds), since they add to API request latency. Use a small timeout for
webhooks.

For details, see
Timeouts.

### Use a load balancer to ensure webhook availability {#load-balancer-webhook}

Admission webhooks should leverage some form of load-balancing to provide high
availability and performance benefits. If a webhook is running within the
cluster, you can run multiple webhook backends behind a Service of type
`ClusterIP`.

### Use a high-availability deployment model {#ha-deployment}

Consider your cluster's availability requirements when designing your webhook. 
For example, during node downtime or zonal outages, Kubernetes marks Pods as
`NotReady` to allow load balancers to reroute traffic to available zones and
nodes. These updates to Pods might trigger your mutating webhooks. Depending on
the number of affected Pods, the mutating webhook server has a risk of timing
out or causing delays in Pod processing. As a result, traffic won't get
rerouted as quickly as you need.

Consider situations like the preceding example when writing your webhooks.
Exclude operations that are a result of Kubernetes responding to unavoidable
incidents.
