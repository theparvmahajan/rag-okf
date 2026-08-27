---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#running-the-job
kind: section
title: Running the Job
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Running the Job
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#defining-a-job
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#alternatives
word_count: 181
---

So, now run the Job:

```shell
# this assumes you downloaded and then edited the manifest already
kubectl apply -f ./job.yaml
```

Now wait a bit, then check on the Job:

```shell
kubectl describe jobs/job-wq-2
```
```
Name:             job-wq-2
Namespace:        default
Selector:         controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
Labels:           controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
                  job-name=job-wq-2
Annotations:      <none>
Parallelism:      2
Completions:      <unset>
Start Time:       Mon, 11 Jan 2022 17:07:59 +0000
Pods Statuses:    1 Running / 0 Succeeded / 0 Failed
Pod Template:
  Labels:       controller-uid=b1c7e4e3-92e1-11e7-b85e-fa163ee3c11f
                job-name=job-wq-2
  Containers:
   c:
    Image:              container-registry.example/exampleproject/job-wq-2
    Port:
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Events:
  FirstSeen    LastSeen    Count    From            SubobjectPath    Type        Reason            Message
  ---------    --------    -----    ----            -------------    --------    ------            -------
  33s          33s         1        {job-controller }                Normal      SuccessfulCreate  Created pod: job-wq-2-lglf8
```

You can wait for the Job to succeed, with a timeout:
```shell
# The check for condition name is case insensitive
kubectl wait --for=condition=complete --timeout=300s job/job-wq-2
```

```shell
kubectl logs pods/job-wq-2-7r7b2
```
```
Worker with sessionID: bbd72d0a-9e5c-4dd6-abf6-416cc267991f
Initial queue state: empty=False
Working on banana
Working on date
Working on lemon
```

As you can see, one of the pods for this Job worked on several work units.
