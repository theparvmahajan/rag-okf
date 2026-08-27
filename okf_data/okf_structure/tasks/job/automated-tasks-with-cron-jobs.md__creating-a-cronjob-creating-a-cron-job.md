---
id: okf-structure/tasks/job/automated-tasks-with-cron-jobs.md#creating-a-cronjob-creating-a-cron-job
kind: section
title: Creating a CronJob {#creating-a-cron-job}
source: tasks/job/automated-tasks-with-cron-jobs.md
url: https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/
heading: Creating a CronJob {#creating-a-cron-job}
parent: okf-structure/tasks/job/automated-tasks-with-cron-jobs
children: []
prev_sibling: okf-structure/tasks/job/automated-tasks-with-cron-jobs.md#prerequisites
next_sibling: okf-structure/tasks/job/automated-tasks-with-cron-jobs.md#deleting-a-cronjob-deleting-a-cron-job
word_count: 317
---

Cron jobs require a config file.
Here is a manifest for a CronJob that runs a simple demonstration task every minute:

Run the example CronJob by using this command:

```shell
kubectl create -f https://k8s.io/examples/application/job/cronjob.yaml
```
The output is similar to this:

```
cronjob.batch/hello created
```

After creating the cron job, get its status using this command:

```shell
kubectl get cronjob hello
```

The output is similar to this:

```
NAME    SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
hello   */1 * * * *   False     0        <none>          10s
```

As you can see from the results of the command, the cron job has not scheduled or run any jobs yet.
Watch for the job to be created in around one minute:

```shell
kubectl get jobs --watch
```
The output is similar to this:

```
NAME               COMPLETIONS   DURATION   AGE
hello-4111706356   0/1                      0s
hello-4111706356   0/1           0s         0s
hello-4111706356   1/1           5s         5s
```

Now you've seen one running job scheduled by the "hello" cron job.
You can stop watching the job and view the cron job again to see that it scheduled the job:

```shell
kubectl get cronjob hello
```

The output is similar to this:

```
NAME    SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
hello   */1 * * * *   False     0        50s             75s
```

You should see that the cron job `hello` successfully scheduled a job at the time specified in
`LAST SCHEDULE`. There are currently 0 active jobs, meaning that the job has completed or failed.

Now, find the pods that the last scheduled job created and view the standard output of one of the pods.

The job name is different from the pod name.

```shell
# Replace "hello-4111706356" with the job name in your system
pods=$(kubectl get pods --selector=job-name=hello-4111706356 --output=jsonpath={.items[*].metadata.name})
```
Show the pod log:

```shell
kubectl logs $pods
```
The output is similar to this:

```
Fri Feb 22 11:02:09 UTC 2019
Hello from the Kubernetes cluster
```
