---
id: okf-structure/concepts/workloads/controllers/cron-jobs.md#writing-a-cronjob-spec
kind: section
title: Writing a CronJob spec
source: concepts/workloads/controllers/cron-jobs.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
heading: Writing a CronJob spec
parent: okf-structure/concepts/workloads/controllers/cron-jobs
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/cron-jobs.md#example
next_sibling: okf-structure/concepts/workloads/controllers/cron-jobs.md#cronjob-limitations-cron-job-limitations
word_count: 1078
---

### Schedule syntax
The `.spec.schedule` field is required. The value of that field follows the Cron syntax:

```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of the month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
# │ │ │ │ │                                   OR sun, mon, tue, wed, thu, fri, sat
# │ │ │ │ │
# │ │ │ │ │
# * * * * *
```

For example, `0 3 * * 1` means this task is scheduled to run weekly on a Monday at 3 AM.

The format also includes extended "Vixie cron" step values. As explained in the
FreeBSD manual:

> Step values can be used in conjunction with ranges. Following a range
> with `/<number>` specifies skips of the number's value through the
> range. For example, `0-23/2` can be used in the hours field to specify
> command execution every other hour (the alternative in the V7 standard is
> `0,2,4,6,8,10,12,14,16,18,20,22`). Steps are also permitted after an
> asterisk, so if you want to say "every two hours", just use `*/2`.

A question mark (`?`) in the schedule has the same meaning as an asterisk `*`, that is,
it stands for any of available value for a given field.

Other than the standard syntax, some macros like `@monthly` can also be used:

| Entry 										| Description																									| Equivalent to |
| ------------- 						| ------------- 																							|-------------  |
| @yearly (or @annually)		| Run once a year at midnight of 1 January										| 0 0 1 1 * 		|
| @monthly 									| Run once a month at midnight of the first day of the month	| 0 0 1 * * 		|
| @weekly 									| Run once a week at midnight on Sunday morning								| 0 0 * * 0 		|
| @daily (or @midnight)			| Run once a day at midnight																	| 0 0 * * * 		|
| @hourly 									| Run once an hour at the beginning of the hour								| 0 * * * * 		|

To generate CronJob schedule expressions, you can also use web tools like crontab.guru.

### Job template

The `.spec.jobTemplate` defines a template for the Jobs that the CronJob creates, and it is required.
It has exactly the same schema as a Job, except that
it is nested and does not have an `apiVersion` or `kind`.
You can specify common metadata for the templated Jobs, such as
labels or
annotations.
For information about writing a Job `.spec`, see Writing a Job Spec.

### Deadline for delayed Job start {#starting-deadline}

The `.spec.startingDeadlineSeconds` field is optional.
This field defines a deadline (in whole seconds) for starting the Job, if that Job misses its scheduled time
for any reason.

After missing the deadline, the CronJob skips that instance of the Job (future occurrences are still scheduled).
For example, if you have a backup Job that runs twice a day, you might allow it to start up to 8 hours late,
but no later, because a backup taken any later wouldn't be useful: you would instead prefer to wait for
the next scheduled run.

For Jobs that miss their configured deadline, Kubernetes treats them as failed Jobs.
If you don't specify `startingDeadlineSeconds` for a CronJob, the Job occurrences have no deadline.

If the `.spec.startingDeadlineSeconds` field is set (not null), the CronJob
controller measures the time between when a Job is expected to be created and
now. If the difference is higher than that limit, it will skip this execution.

For example, if it is set to `200`, it allows a Job to be created for up to 200
seconds after the actual schedule.

### Concurrency policy

The `.spec.concurrencyPolicy` field is also optional.
It specifies how to treat concurrent executions of a Job that is created by this CronJob.
The spec may specify only one of the following concurrency policies:

* `Allow` (default): The CronJob allows concurrently running Jobs
* `Forbid`: The CronJob does not allow concurrent runs; if it is time for a new Job run and the
  previous Job run hasn't finished yet, the CronJob skips the new Job run. Also note that when the
  previous Job run finishes, `.spec.startingDeadlineSeconds` is still taken into account and may
  result in a new Job run.
* `Replace`: If it is time for a new Job run and the previous Job run hasn't finished yet, the
  CronJob replaces the currently running Job run with a new Job run

Note that concurrency policy only applies to the Jobs created by the same CronJob.
If there are multiple CronJobs, their respective Jobs are always allowed to run concurrently.

### Schedule suspension

You can suspend execution of Jobs for a CronJob, by setting the optional `.spec.suspend` field
to true. The field defaults to false.

This setting does _not_ affect Jobs that the CronJob has already started.

If you do set that field to true, all subsequent executions are suspended (they remain
scheduled, but the CronJob controller does not start the Jobs to run the tasks) until
you unsuspend the CronJob.

Executions that are suspended during their scheduled time count as missed Jobs.
When `.spec.suspend` changes from `true` to `false` on an existing CronJob without a
starting deadline, the missed Jobs are scheduled immediately.

### Jobs history limits

The `.spec.successfulJobsHistoryLimit` and `.spec.failedJobsHistoryLimit` fields specify
how many completed and failed Jobs should be kept. Both fields are optional.

* `.spec.successfulJobsHistoryLimit`: This field specifies the number of successful finished
jobs to keep. The default value is `3`. Setting this field to `0` will not keep any successful jobs.

* `.spec.failedJobsHistoryLimit`: This field specifies the number of failed finished jobs to keep.
The default value is `1`. Setting this field to `0` will not keep any failed jobs.

For another way to clean up Jobs automatically, see
Clean up finished Jobs automatically.

### Time zones

For CronJobs with no time zone specified, the kube-controller-manager
interprets schedules relative to its local time zone.

You can specify a time zone for a CronJob by setting `.spec.timeZone` to the name
of a valid time zone.
For example, setting `.spec.timeZone: "Etc/UTC"` instructs Kubernetes to interpret
the schedule relative to Coordinated Universal Time.

A time zone database from the Go standard library is included in the binaries and used as a fallback in case an external database is not available on the system.
