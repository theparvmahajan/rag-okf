---
id: okf-structure/tasks/job/automated-tasks-with-cron-jobs.md#deleting-a-cronjob-deleting-a-cron-job
kind: section
title: Deleting a CronJob {#deleting-a-cron-job}
source: tasks/job/automated-tasks-with-cron-jobs.md
url: https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/
heading: Deleting a CronJob {#deleting-a-cron-job}
parent: okf-structure/tasks/job/automated-tasks-with-cron-jobs
children: []
prev_sibling: okf-structure/tasks/job/automated-tasks-with-cron-jobs.md#creating-a-cronjob-creating-a-cron-job
next_sibling: null
word_count: 52
---

When you don't need a cron job any more, delete it with `kubectl delete cronjob <cronjob name>`:

```shell
kubectl delete cronjob hello
```

Deleting the cron job removes all the jobs and pods it created and stops it from creating additional jobs.
You can read more about removing jobs in garbage collection.
