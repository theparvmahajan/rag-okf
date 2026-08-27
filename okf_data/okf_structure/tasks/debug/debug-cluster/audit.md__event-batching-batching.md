---
id: okf-structure/tasks/debug/debug-cluster/audit.md#event-batching-batching
kind: section
title: Event batching {#batching}
source: tasks/debug/debug-cluster/audit.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
heading: Event batching {#batching}
parent: okf-structure/tasks/debug/debug-cluster/audit
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#audit-backends
next_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#parameter-tuning
word_count: 431
---

Both `log` and `webhook` backends support batching. Below is a list of
available flags specific to each backend. 
By default, batching and throttling are **enabled** for the `webhook` backend and **disabled** for the `log` backend.

- `--audit-webhook-mode` defines the buffering strategy. One of the following:
  - `batch` - buffer events and asynchronously process them in batches. This is the default mode for the `webhook` backend.
  - `blocking` - block API server responses on processing each individual event.
  - `blocking-strict` - Same as blocking, but when there is a failure during audit logging at the
    RequestReceived stage, the whole request to the kube-apiserver fails.

The following flags are used only in the `batch` mode:

- `--audit-webhook-batch-buffer-size` defines the number of events to buffer before batching.
  If the rate of incoming events overflows the buffer, events are dropped. The default value is 10000.
- `--audit-webhook-batch-max-size` defines the maximum number of events in one batch. The default value is 400.
- `--audit-webhook-batch-max-wait` defines the maximum amount of time to wait before unconditionally
  batching events in the queue. The default value is 30 seconds.
- `--audit-webhook-batch-throttle-enable` defines whether batching throttling is enabled. Throttling is enabled by default.
- `--audit-webhook-batch-throttle-qps` defines the maximum average number of batches generated
  per second. The default value is 10.
- `--audit-webhook-batch-throttle-burst` defines the maximum number of batches generated at the same
  moment if the allowed QPS was underutilized previously. The default value is 15.

- `--audit-log-mode` defines the buffering strategy. One of the following:
  - `batch` - buffer events and asynchronously process them in batches. Batching is not recommended for the `log` backend.
  - `blocking` - block API server responses on processing each individual event. This is the default mode for the `log` backend.
  - `blocking-strict` - Same as blocking, but when there is a failure during audit logging at the
    RequestReceived stage, the whole request to the kube-apiserver fails.

The following flags are used only in the `batch` mode (batching is **disabled** by default for the `log` backend, and when batching is disabled, all batching-related flags are ignored):

- `--audit-log-batch-buffer-size` defines the number of events to buffer before batching.
  If the rate of incoming events overflows the buffer, events are dropped.
- `--audit-log-batch-max-size` defines the maximum number of events in one batch.
- `--audit-log-batch-max-wait` defines the maximum amount of time to wait before unconditionally
  batching events in the queue.
- `--audit-log-batch-throttle-enable` defines whether batching throttling is enabled.
- `--audit-log-batch-throttle-qps` defines the maximum average number of batches generated
  per second.
- `--audit-log-batch-throttle-burst` defines the maximum number of batches generated at the same
  moment if the allowed QPS was underutilized previously.
