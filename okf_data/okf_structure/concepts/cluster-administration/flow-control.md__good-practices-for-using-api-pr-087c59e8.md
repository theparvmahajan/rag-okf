---
id: okf-structure/concepts/cluster-administration/flow-control.md#good-practices-for-using-api-priority-and-fairness
kind: section
title: Good practices for using API Priority and Fairness
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Good practices for using API Priority and Fairness
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#observability
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#whatsnext
word_count: 876
---

When a given priority level exceeds its permitted concurrency, requests can
experience increased latency or be dropped with an HTTP 429 (Too Many Requests)
error. To prevent these side effects of APF, you can modify your workload or
tweak your APF settings to ensure there are sufficient seats available to serve
your requests.

To detect whether requests are being rejected due to APF, check the following
metrics:

- apiserver_flowcontrol_rejected_requests_total: the total number of requests
  rejected per FlowSchema and PriorityLevelConfiguration.
- apiserver_flowcontrol_current_inqueue_requests: the current number of requests
  queued per FlowSchema and PriorityLevelConfiguration.
- apiserver_flowcontrol_request_wait_duration_seconds: the latency added to
  requests waiting in queues.
- apiserver_flowcontrol_priority_level_seat_utilization: the seat utilization
  per PriorityLevelConfiguration.

### Workload modifications {#good-practice-workload-modifications}

To prevent requests from queuing and adding latency or being dropped due to APF,
you can optimize your requests by:

- Reducing the rate at which requests are executed. A fewer number of requests
  over a fixed period will result in a fewer number of seats being needed at a
  given time.
- Avoid issuing a large number of expensive requests concurrently. Requests can
  be optimized to use fewer seats or have lower latency so that these requests
  hold those seats for a shorter duration. List requests can occupy more than 1
  seat depending on the number of objects fetched during the request. Restricting
  the number of objects retrieved in a list request, for example by using
  pagination, will use less total seats over a shorter period. Furthermore,
  replacing list requests with watch requests will require lower total concurrency
  shares as watch requests only occupy 1 seat during its initial burst of
  notifications. If using streaming lists in versions 1.27 and later, watch
  requests will occupy the same number of seats as a list request for its initial
  burst of notifications because the entire state of the collection has to be
  streamed. Note that in both cases, a watch request will not hold any seats after
  this initial phase.

Keep in mind that queuing or rejected requests from APF could be induced by
either an increase in the number of requests or an increase in latency for
existing requests. For example, if requests that normally take 1s to execute
start taking 60s, it is possible that APF will start rejecting requests because
requests are occupying seats for a longer duration than normal due to this
increase in latency. If APF starts rejecting requests across multiple priority
levels without a significant change in workload, it is possible there is an
underlying issue with control plane performance rather than the workload or APF
settings.

### Priority and fairness settings {#good-practice-apf-settings}

You can also modify the default FlowSchema and PriorityLevelConfiguration
objects or create new objects of these types to better accommodate your
workload.

APF settings can be modified to:

- Give more seats to high priority requests.
- Isolate non-essential or expensive requests that would starve a concurrency
  level if it was shared with other flows.

#### Give more seats to high priority requests

1. If possible, the number of seats available across all priority levels for a
   particular `kube-apiserver` can be increased by increasing the values for the
   `max-requests-inflight` and `max-mutating-requests-inflight` flags. Alternatively,
   horizontally scaling the number of `kube-apiserver` instances will increase the
   total concurrency per priority level across the cluster assuming there is
   sufficient load balancing of requests.
1. You can create a new FlowSchema which references a PriorityLevelConfiguration
   with a larger concurrency level. This new PriorityLevelConfiguration could be an
   existing level or a new level with its own set of nominal concurrency shares.
   For example, a new FlowSchema could be introduced to change the
   PriorityLevelConfiguration for your requests from global-default to workload-low
   to increase the number of seats available to your user. Creating a new
   PriorityLevelConfiguration will reduce the number of seats designated for
   existing levels. Recall that editing a default FlowSchema or
   PriorityLevelConfiguration will require setting the
   `apf.kubernetes.io/autoupdate-spec` annotation to false.
1. You can also increase the NominalConcurrencyShares for the
   PriorityLevelConfiguration which is serving your high priority requests.
   Alternatively, for versions 1.26 and later, you can increase the LendablePercent
   for competing priority levels so that the given priority level has a higher pool
   of seats it can borrow.

#### Isolate non-essential requests from starving other flows

For request isolation, you can create a FlowSchema whose subject matches the
user making these requests or create a FlowSchema that matches what the request
is (corresponding to the resourceRules). Next, you can map this FlowSchema to a
PriorityLevelConfiguration with a low share of seats.

For example, suppose list event requests from Pods running in the default namespace
are using 10 seats each and execute for 1 minute. To prevent these expensive
requests from impacting requests from other Pods using the existing service-accounts
FlowSchema, you can apply the following FlowSchema to isolate these list calls
from other requests.

Example FlowSchema object to isolate list event requests:

- This FlowSchema captures all list event calls made by the default service
  account in the default namespace. The matching precedence 8000 is lower than the
  value of 9000 used by the existing service-accounts FlowSchema so these list
  event calls will match list-events-default-service-account rather than
  service-accounts.
- The catch-all PriorityLevelConfiguration is used to isolate these requests.
  The catch-all priority level has a very small concurrency share and does not
  queue requests.
