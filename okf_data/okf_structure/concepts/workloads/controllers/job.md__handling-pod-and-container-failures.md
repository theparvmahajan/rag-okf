---
id: okf-structure/concepts/workloads/controllers/job.md#handling-pod-and-container-failures
kind: section
title: Handling Pod and container failures
source: concepts/workloads/controllers/job.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
heading: Handling Pod and container failures
parent: okf-structure/concepts/workloads/controllers/job
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/job.md#integrate-with-workload-apis
next_sibling: okf-structure/concepts/workloads/controllers/job.md#success-policy-success-policy
word_count: 1776
---

A container in a Pod may fail for a number of reasons, such as because the process in it exited with
a non-zero exit code, or the container was killed for exceeding a memory limit, etc. If this
happens, and the `.spec.template.spec.restartPolicy = "OnFailure"`, then the Pod stays
on the node, but the container is re-run. Therefore, your program needs to handle the case when it is
restarted locally, or else specify `.spec.template.spec.restartPolicy = "Never"`.
See pod lifecycle for more information on `restartPolicy`.

An entire Pod can also fail, for a number of reasons, such as when the pod is kicked off the node
(node is upgraded, rebooted, deleted, etc.), or if a container of the Pod fails and the
`.spec.template.spec.restartPolicy = "Never"`. When a Pod fails, then the Job controller
starts a new Pod. This means that your application needs to handle the case when it is restarted in a new
pod. In particular, it needs to handle temporary files, locks, incomplete output and the like
caused by previous runs.

By default, each pod failure is counted towards the `.spec.backoffLimit` limit,
see pod backoff failure policy. However, you can
customize handling of pod failures by setting the Job's pod failure policy.

Additionally, you can choose to count the pod failures independently for each
index of an Indexed Job by setting the `.spec.backoffLimitPerIndex` field
(for more information, see backoff limit per index).

Note that even if you specify `.spec.parallelism = 1` and `.spec.completions = 1` and
`.spec.template.spec.restartPolicy = "Never"`, the same program may
sometimes be started twice.

If you do specify `.spec.parallelism` and `.spec.completions` both greater than 1, then there may be
multiple pods running at once. Therefore, your pods must also be tolerant of concurrency.

If you specify the `.spec.podFailurePolicy` field, the Job controller does not consider a terminating
Pod (a pod that has a `.metadata.deletionTimestamp` field set) as a failure until that Pod is
terminal (its `.status.phase` is `Failed` or `Succeeded`). However, the Job controller
creates a replacement Pod as soon as the termination becomes apparent. Once the
pod terminates, the Job controller evaluates `.backoffLimit` and `.podFailurePolicy`
for the relevant Job, taking this now-terminated Pod into consideration.

If either of these requirements is not satisfied, the Job controller counts
a terminating Pod as an immediate failure, even if that Pod later terminates
with `phase: "Succeeded"`.

### Pod backoff failure policy

There are situations where you want to fail a Job after some amount of retries
due to a logical error in configuration etc.
To do so, set `.spec.backoffLimit` to specify the number of retries before
considering a Job as failed.

The `.spec.backoffLimit` is set by default to 6, unless the
backoff limit per index (only Indexed Job) is specified.
When `.spec.backoffLimitPerIndex` is specified, then `.spec.backoffLimit` defaults
to 2147483647 (MaxInt32).

Failed Pods associated with the Job are recreated by the Job controller with an
exponential back-off delay (10s, 20s, 40s ...) capped at six minutes.

The number of retries is calculated in two ways:

- The number of Pods with `.status.phase = "Failed"`.
- When using `restartPolicy = "OnFailure"`, the number of retries in all the
  containers of Pods with `.status.phase` equal to `Pending` or `Running`.

If either of the calculations reaches the `.spec.backoffLimit`, the Job is
considered failed.

If your Job has `restartPolicy = "OnFailure"`, keep in mind that your Pod running the job
will be terminated once the job backoff limit has been reached. This can make debugging
the Job's executable more difficult. We suggest setting
`restartPolicy = "Never"` when debugging the Job or using a logging system to ensure output
from failed Jobs is not lost inadvertently.

### Backoff limit per index {#backoff-limit-per-index}

When you run an indexed Job, you can choose to handle retries
for pod failures independently for each index. To do so, set the
`.spec.backoffLimitPerIndex` to specify the maximal number of pod failures
per index.

When the per-index backoff limit is exceeded for an index, Kubernetes considers the index as failed and adds it to the
`.status.failedIndexes` field. The succeeded indexes, those with a successfully
executed pods, are recorded in the `.status.completedIndexes` field, regardless of whether you set
the `backoffLimitPerIndex` field.

Note that a failing index does not interrupt execution of other indexes.
Once all indexes finish for a Job where you specified a backoff limit per index,
if at least one of those indexes did fail, the Job controller marks the overall
Job as failed, by setting the Failed condition in the status. The Job gets
marked as failed even if some, potentially nearly all, of the indexes were
processed successfully.

You can additionally limit the maximal number of indexes marked failed by
setting the `.spec.maxFailedIndexes` field.
When the number of failed indexes exceeds the `maxFailedIndexes` field, the
Job controller triggers termination of all remaining running Pods for that Job.
Once all pods are terminated, the entire Job is marked failed by the Job
controller, by setting the Failed condition in the Job status.

Here is an example manifest for a Job that defines a `backoffLimitPerIndex`:

In the example above, the Job controller allows for one restart for each
of the indexes. When the total number of failed indexes exceeds 5, then
the entire Job is terminated.

Once the job is finished, the Job status looks as follows:

```sh
kubectl get -o yaml job job-backoff-limit-per-index-example
```

```yaml
  status:
    completedIndexes: 1,3,5,7,9
    failedIndexes: 0,2,4,6,8
    succeeded: 5          # 1 succeeded pod for each of 5 succeeded indexes
    failed: 10            # 2 failed pods (1 retry) for each of 5 failed indexes
    conditions:
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: FailureTarget
    - message: Job has failed indexes
      reason: FailedIndexes
      status: "True"
      type: Failed
```

The Job controller adds the `FailureTarget` Job condition to trigger
Job termination and cleanup. When all of the
Job Pods are terminated, the Job controller adds the `Failed` condition
with the same values for `reason` and `message` as the `FailureTarget` Job
condition. For details, see Termination of Job Pods.

Additionally, you may want to use the per-index backoff along with a
pod failure policy. When using
per-index backoff, there is a new `FailIndex` action available which allows you to
avoid unnecessary retries within an index.

### Pod failure policy {#pod-failure-policy}

A Pod failure policy, defined with the `.spec.podFailurePolicy` field, enables
your cluster to handle Pod failures based on the container exit codes and the
Pod conditions.

In some situations, you  may want to have a better control when handling Pod
failures than the control provided by the Pod backoff failure policy,
which is based on the Job's `.spec.backoffLimit`. These are some examples of use cases:

* To optimize costs of running workloads by avoiding unnecessary Pod restarts,
  you can terminate a Job as soon as one of its Pods fails with an exit code
  indicating a software bug.
* To guarantee that your Job finishes even if there are disruptions, you can
  ignore Pod failures caused by disruptions (such as preemption,
  API-initiated eviction
  or taint-based eviction) so
  that they don't count towards the `.spec.backoffLimit` limit of retries.

You can configure a Pod failure policy, in the `.spec.podFailurePolicy` field,
to meet the above use cases. This policy can handle Pod failures based on the
container exit codes and the Pod conditions.

Here is a manifest for a Job that defines a `podFailurePolicy`:

In the example above, the first rule of the Pod failure policy specifies that
the Job should be marked failed if the `main` container fails with the 42 exit
code. The following are the rules for the `main` container specifically:

- an exit code of 0 means that the container succeeded
- an exit code of 42 means that the **entire Job** failed
- any other exit code represents that the container failed, and hence the entire
  Pod. The Pod will be re-created if the total number of restarts is
  below `backoffLimit`. If the `backoffLimit` is reached the **entire Job** failed.

Because the Pod template specifies a `restartPolicy: Never`,
the kubelet does not restart the `main` container in that particular Pod.

The second rule of the Pod failure policy, specifying the `Ignore` action for
failed Pods with condition `DisruptionTarget` excludes Pod disruptions from
being counted towards the `.spec.backoffLimit` limit of retries.

If the Job failed, either by the Pod failure policy or Pod backoff
failure policy, and the Job is running multiple Pods, Kubernetes terminates all
the Pods in that Job that are still Pending or Running.

These are some requirements and semantics of the API:

- if you want to use a `.spec.podFailurePolicy` field for a Job, you must
  also define that Job's pod template with `.spec.restartPolicy` set to `Never`.
- the Pod failure policy rules you specify under `spec.podFailurePolicy.rules`
  are evaluated in order. Once a rule matches a Pod failure, the remaining rules
  are ignored. When no rule matches the Pod failure, the default
  handling applies.
- you may want to restrict a rule to a specific container by specifying its name
  in`spec.podFailurePolicy.rules[*].onExitCodes.containerName`. When not specified the rule
  applies to all containers. When specified, it should match one the container
  or `initContainer` names in the Pod template.
- you may specify the action taken when a Pod failure policy is matched by
  `spec.podFailurePolicy.rules[*].action`. Possible values are:
  - `FailJob`: use to indicate that the Pod's job should be marked as Failed and
     all running Pods should be terminated.
  - `Ignore`: use to indicate that the counter towards the `.spec.backoffLimit`
     should not be incremented and a replacement Pod should be created.
  - `Count`: use to indicate that the Pod should be handled in the default way.
     The counter towards the `.spec.backoffLimit` should be incremented.
  - `FailIndex`: use this action along with backoff limit per index
     to avoid unnecessary retries within the index of a failed pod.

When you use a `podFailurePolicy`, the job controller only matches Pods in the
`Failed` phase. Pods with a deletion timestamp that are not in a terminal phase
(`Failed` or `Succeeded`) are considered still terminating. This implies that
terminating pods retain a tracking finalizer
until they reach a terminal phase.
Since Kubernetes 1.27, Kubelet transitions deleted pods to a terminal phase
(see: Pod Phase). This
ensures that deleted pods have their finalizers removed by the Job controller.

Starting with Kubernetes v1.28, when Pod failure policy is used, the Job controller recreates
terminating Pods only once these Pods reach the terminal `Failed` phase. This behavior is similar
to `podReplacementPolicy: Failed`. For more information, see Pod replacement policy.

When you use the `podFailurePolicy`, and the Job fails due to the pod
matching the rule with the `FailJob` action, then the Job controller triggers
the Job termination process by adding the `FailureTarget` condition.
For more details, see Job termination and cleanup.
