---
id: okf-structure/concepts/workloads/controllers/cron-jobs.md#introduction
kind: section
title: CronJob
source: concepts/workloads/controllers/cron-jobs.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/
heading: null
parent: okf-structure/concepts/workloads/controllers/cron-jobs
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/controllers/cron-jobs.md#example
word_count: 191
---

A _CronJob_ creates Jobs on a repeating schedule.

CronJob is meant for performing regular scheduled actions such as backups, report generation,
and so on. One CronJob object is like one line of a _crontab_ (cron table) file on a
Unix system. It runs a Job periodically on a given schedule, written in
Cron format.

CronJobs have limitations and idiosyncrasies.
For example, in certain circumstances, a single CronJob can create multiple concurrent Jobs. See the limitations below.

When the control plane creates new Jobs and (indirectly) Pods for a CronJob, the `.metadata.name`
of the CronJob is part of the basis for naming those Pods.  The name of a CronJob must be a valid
DNS subdomain
value, but this can produce unexpected results for the Pod hostnames.  For best compatibility,
the name should follow the more restrictive rules for a
DNS label.
Even when the name is a DNS subdomain, the name must be no longer than 52
characters.  This is because the CronJob controller will automatically append
11 characters to the name you provide and there is a constraint that the
length of a Job name is no more than 63 characters.
