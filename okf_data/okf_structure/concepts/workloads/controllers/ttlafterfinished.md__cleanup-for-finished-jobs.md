---
id: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#cleanup-for-finished-jobs
kind: section
title: Cleanup for finished Jobs
source: concepts/workloads/controllers/ttlafterfinished.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/
heading: Cleanup for finished Jobs
parent: okf-structure/concepts/workloads/controllers/ttlafterfinished
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#caveats
word_count: 286
---

The TTL-after-finished controller is only supported for Jobs. You can use this mechanism to clean
up finished Jobs (either `Complete` or `Failed`) automatically by specifying the
`.spec.ttlSecondsAfterFinished` field of a Job, as in this
example.

The TTL-after-finished controller assumes that a Job is eligible to be cleaned up
TTL seconds after the Job has finished. The timer starts once the
status condition of the Job changes to show that the Job is either `Complete` or `Failed`; once the TTL has
expired, that Job becomes eligible for
cascading removal. When the
TTL-after-finished controller cleans up a job, it will delete it cascadingly, that is to say it will delete
its dependent objects together with it.

Kubernetes honors object lifecycle guarantees on the Job, such as waiting for
finalizers.

You can set the TTL seconds at any time. Here are some examples for setting the
`.spec.ttlSecondsAfterFinished` field of a Job:

* Specify this field in the Job manifest, so that a Job can be cleaned up
  automatically some time after it finishes.
* Manually set this field of existing, already finished Jobs, so that they become eligible
  for cleanup.
* Use a
  mutating admission webhook
  to set this field dynamically at Job creation time. Cluster administrators can
  use this to enforce a TTL policy for finished jobs.
* Use a
  mutating admission webhook
  to set this field dynamically after the Job has finished, and choose
  different TTL values based on job status, labels. For this case, the webhook needs
  to detect changes to the `.status` of the Job and only set a TTL when the Job
  is being marked as completed.
* Write your own controller to manage the cleanup TTL for Jobs that match a particular
  selector.
