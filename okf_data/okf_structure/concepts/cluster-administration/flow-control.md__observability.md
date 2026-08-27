---
id: okf-structure/concepts/cluster-administration/flow-control.md#observability
kind: section
title: Observability
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Observability
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#health-check-concurrency-exemption
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#good-practices-for-using-api-priority-and-fairness
word_count: 1285
---

### Metrics

In versions of Kubernetes before v1.20, the labels `flow_schema` and
`priority_level` were inconsistently named `flowSchema` and `priorityLevel`,
respectively. If you're running Kubernetes versions v1.19 and earlier, you
should refer to the documentation for your version.

When you enable the API Priority and Fairness feature, the kube-apiserver
exports additional metrics. Monitoring these can help you determine whether your
configuration is inappropriately throttling important traffic, or find
poorly-behaved workloads that may be harming system health.

#### Maturity level BETA

* `apiserver_flowcontrol_rejected_requests_total` is a counter vector
  (cumulative since server start) of requests that were rejected,
  broken down by the labels `flow_schema` (indicating the one that
  matched the request), `priority_level` (indicating the one to which
  the request was assigned), and `reason`. The `reason` label will be
  one of the following values:

  * `queue-full`, indicating that too many requests were already
    queued.
  * `concurrency-limit`, indicating that the
    PriorityLevelConfiguration is configured to reject rather than
    queue excess requests.
  * `time-out`, indicating that the request was still in the queue
    when its queuing time limit expired.
  * `cancelled`, indicating that the request is not purge locked
    and has been ejected from the queue.

* `apiserver_flowcontrol_dispatched_requests_total` is a counter
  vector (cumulative since server start) of requests that began
  executing, broken down by `flow_schema` and `priority_level`.

* `apiserver_flowcontrol_current_inqueue_requests` is a gauge vector
  holding the instantaneous number of queued (not executing) requests,
  broken down by `priority_level` and `flow_schema`.

* `apiserver_flowcontrol_current_executing_requests` is a gauge vector
  holding the instantaneous number of executing (not waiting in a
  queue) requests, broken down by `priority_level` and `flow_schema`.

* `apiserver_flowcontrol_current_executing_seats` is a gauge vector
  holding the instantaneous number of occupied seats, broken down by
  `priority_level` and `flow_schema`.

* `apiserver_flowcontrol_request_wait_duration_seconds` is a histogram
  vector of how long requests spent queued, broken down by the labels
  `flow_schema`, `priority_level`, and `execute`. The `execute` label
  indicates whether the request has started executing.

  
  Since each FlowSchema always assigns requests to a single
  PriorityLevelConfiguration, you can add the histograms for all the
  FlowSchemas for one priority level to get the effective histogram for
  requests assigned to that priority level.
  

* `apiserver_flowcontrol_nominal_limit_seats` is a gauge vector
  holding each priority level's nominal concurrency limit, computed
  from the API server's total concurrency limit and the priority
  level's configured nominal concurrency shares.

#### Maturity level ALPHA

* `apiserver_current_inqueue_requests` is a gauge vector of recent
  high water marks of the number of queued requests, grouped by a
  label named `request_kind` whose value is `mutating` or `readOnly`.
  These high water marks describe the largest number seen in the one
  second window most recently completed. These complement the older
  `apiserver_current_inflight_requests` gauge vector that holds the
  last window's high water mark of number of requests actively being
  served.

* `apiserver_current_inqueue_seats` is a gauge vector of the sum over
  queued requests of the largest number of seats each will occupy,
  grouped by labels named `flow_schema` and `priority_level`.

* `apiserver_flowcontrol_read_vs_write_current_requests` is a
  histogram vector of observations, made at the end of every
  nanosecond, of the number of requests broken down by the labels
  `phase` (which takes on the values `waiting` and `executing`) and
  `request_kind` (which takes on the values `mutating` and
  `readOnly`). Each observed value is a ratio, between 0 and 1, of
  the number of requests divided by the corresponding limit on the
  number of requests (queue volume limit for waiting and concurrency
  limit for executing).

* `apiserver_flowcontrol_request_concurrency_in_use` is a gauge vector
  holding the instantaneous number of occupied seats, broken down by
  `priority_level` and `flow_schema`.

* `apiserver_flowcontrol_priority_level_request_utilization` is a
  histogram vector of observations, made at the end of each
  nanosecond, of the number of requests broken down by the labels
  `phase` (which takes on the values `waiting` and `executing`) and
  `priority_level`. Each observed value is a ratio, between 0 and 1,
  of a number of requests divided by the corresponding limit on the
  number of requests (queue volume limit for waiting and concurrency
  limit for executing).

* `apiserver_flowcontrol_priority_level_seat_utilization` is a
  histogram vector of observations, made at the end of each
  nanosecond, of the utilization of a priority level's concurrency
  limit, broken down by `priority_level`. This utilization is the
  fraction (number of seats occupied) / (concurrency limit). This
  metric considers all stages of execution (both normal and the extra
  delay at the end of a write to cover for the corresponding
  notification work) of all requests except WATCHes; for those it
  considers only the initial stage that delivers notifications of
  pre-existing objects. Each histogram in the vector is also labeled
  with `phase: executing` (there is no seat limit for the waiting
  phase).

* `apiserver_flowcontrol_request_queue_length_after_enqueue` is a
  histogram vector of queue lengths for the queues, broken down by
  `priority_level` and `flow_schema`, as sampled by the enqueued requests.
  Each request that gets queued contributes one sample to its histogram,
  reporting the length of the queue immediately after the request was added.
  Note that this produces different statistics than an unbiased survey would.

  
  An outlier value in a histogram here means it is likely that a single flow
  (i.e., requests by one user or for one namespace, depending on
  configuration) is flooding the API server, and being throttled. By contrast,
  if one priority level's histogram shows that all queues for that priority
  level are longer than those for other priority levels, it may be appropriate
  to increase that PriorityLevelConfiguration's concurrency shares.
  

* `apiserver_flowcontrol_request_concurrency_limit` is the same as
  `apiserver_flowcontrol_nominal_limit_seats`. Before the
  introduction of concurrency borrowing between priority levels,
  this was always equal to `apiserver_flowcontrol_current_limit_seats`
  (which did not exist as a distinct metric).

* `apiserver_flowcontrol_lower_limit_seats` is a gauge vector holding
  the lower bound on each priority level's dynamic concurrency limit.

* `apiserver_flowcontrol_upper_limit_seats` is a gauge vector holding
  the upper bound on each priority level's dynamic concurrency limit.

* `apiserver_flowcontrol_demand_seats` is a histogram vector counting
  observations, at the end of every nanosecond, of each priority
  level's ratio of (seat demand) / (nominal concurrency limit). 
  A priority level's seat demand is the sum, over both queued requests
  and those in the initial phase of execution, of the maximum of the
  number of seats occupied in the request's initial and final
  execution phases.

* `apiserver_flowcontrol_demand_seats_high_watermark` is a gauge vector
  holding, for each priority level, the maximum seat demand seen
  during the last concurrency borrowing adjustment period.

* `apiserver_flowcontrol_demand_seats_average` is a gauge vector
  holding, for each priority level, the time-weighted average seat
  demand seen during the last concurrency borrowing adjustment period.

* `apiserver_flowcontrol_demand_seats_stdev` is a gauge vector
  holding, for each priority level, the time-weighted population
  standard deviation of seat demand seen during the last concurrency
  borrowing adjustment period.

* `apiserver_flowcontrol_demand_seats_smoothed` is a gauge vector
  holding, for each priority level, the smoothed enveloped seat demand
  determined at the last concurrency adjustment.

* `apiserver_flowcontrol_target_seats` is a gauge vector holding, for
  each priority level, the concurrency target going into the borrowing
  allocation problem.

* `apiserver_flowcontrol_seat_fair_frac` is a gauge holding the fair
  allocation fraction determined in the last borrowing adjustment.

* `apiserver_flowcontrol_current_limit_seats` is a gauge vector
  holding, for each priority level, the dynamic concurrency limit
  derived in the last adjustment.

* `apiserver_flowcontrol_request_execution_seconds` is a histogram
  vector of how long requests took to actually execute, broken down by
  `flow_schema` and `priority_level`.

* `apiserver_flowcontrol_watch_count_samples` is a histogram vector of
  the number of active WATCH requests relevant to a given write,
  broken down by `flow_schema` and `priority_level`.

* `apiserver_flowcontrol_work_estimated_seats` is a histogram vector
  of the number of estimated seats (maximum of initial and final stage
  of execution) associated with requests, broken down by `flow_schema`
  and `priority_level`.

* `apiserver_flowcontrol_request_dispatch_no_accommodation_total` is a
  counter vector of the number of events that in principle could have led
  to a request being dispatched but did not, due to lack of available
  concurrency, broken down by `flow_schema` and `priority_level`.

* `apiserver_flowcontrol_epoch_advance_total` is a counter vector of
  the number of attempts to jump a priority level's progress meter
  backward to avoid numeric overflow, grouped by `priority_level` and
  `success`.
