---
id: okf-structure/concepts/workloads/controllers/cron-jobs.md#cronjob-limitations-cron-job-limitations
kind: section
title: CronJob limitations {#cron-job-limitations}
source: concepts/workloads/controllers/cron-jobs.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
heading: CronJob limitations {#cron-job-limitations}
parent: okf-structure/concepts/workloads/controllers/cron-jobs
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/cron-jobs.md#writing-a-cronjob-spec
next_sibling: okf-structure/concepts/workloads/controllers/cron-jobs.md#whatsnext
word_count: 640
---

### Unsupported TimeZone specification

Specifying a timezone using `CRON_TZ` or `TZ` variables inside `.spec.schedule`
is **not officially supported** (and never has been). If you try to set a schedule
that includes `TZ` or `CRON_TZ` timezone specification, Kubernetes will fail to
create or update the resource with a validation error. You should specify time zones
using the time zone field, instead.

### Modifying a CronJob

By design, a CronJob contains a template for _new_ Jobs.
If you modify an existing CronJob, the changes you make will apply to new Jobs that
start to run after your modification is complete. Jobs (and their Pods) that have already
started continue to run without changes.
That is, the CronJob does _not_ update existing Jobs, even if those remain running.

### Job creation

A CronJob creates a Job object approximately once per execution time of its schedule.
The scheduling is approximate because there
are certain circumstances where two Jobs might be created, or no Job might be created.
Kubernetes tries to avoid those situations, but does not completely prevent them. Therefore,
the Jobs that you define should be _idempotent_.

Starting with Kubernetes v1.32, CronJobs apply an annotation
`batch.kubernetes.io/cronjob-scheduled-timestamp` to their created Jobs. This annotation
indicates the originally scheduled creation time for the Job and is formatted in RFC3339.

If `startingDeadlineSeconds` is set to a large value or left unset (the default)
and if `concurrencyPolicy` is set to `Allow`, the Jobs will always run
at least once.

If `startingDeadlineSeconds` is set to a value less than 10 seconds, the CronJob may not be scheduled. This is because the CronJob controller checks things every 10 seconds.

For every CronJob, the CronJob controller checks how many schedules it missed in the duration from its last scheduled time until now. If there are more than 100 missed schedules, then it does not start the Job and logs the error.

```
too many missed start times. Set or decrease .spec.startingDeadlineSeconds or check clock skew
```
This behavior is applicable for catch-up scheduling and does not mean the CronJob will stop running.  

For example, when using `concurrencyPolicy: Forbid`, long-running Jobs may cause scheduled times to be skipped, but a new Job can be created once the previous Job completes.

It is important to note that if the `startingDeadlineSeconds` field is set (not `nil`), the controller counts how many missed Jobs occurred from the value of `startingDeadlineSeconds` until now rather than from the last scheduled time until now. For example, if `startingDeadlineSeconds` is `200`, the controller counts how many missed Jobs occurred in the last 200 seconds.

A CronJob is counted as missed if it has failed to be created at its scheduled time. For example, if `concurrencyPolicy` is set to `Forbid` and a CronJob was attempted to be scheduled when there was a previous schedule still running, then it would count as missed.

For example, suppose a CronJob is set to schedule a new Job every one minute beginning at `08:30:00`, and its
`startingDeadlineSeconds` field is not set. If the CronJob controller happens to
be down from `08:29:00` to `10:21:00`, the Job will not start as the number of missed Jobs which missed their schedule is greater than 100.

To illustrate this concept further, suppose a CronJob is set to schedule a new Job every one minute beginning at `08:30:00`, and its
`startingDeadlineSeconds` is set to 200 seconds. If the CronJob controller happens to
be down for the same period as the previous example (`08:29:00` to `10:21:00`,) the Job will still start at 10:22:00. This happens as the controller now checks how many missed schedules happened in the last 200 seconds (i.e., 3 missed schedules), rather than from the last scheduled time until now.

The CronJob is only responsible for creating Jobs that match its schedule, and
the Job in turn is responsible for the management of the Pods it represents.
