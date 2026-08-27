---
id: okf-structure/tasks/job/parallel-processing-expansion.md#create-jobs-based-on-a-template
kind: section
title: Create Jobs based on a template
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Create Jobs based on a template
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#prerequisites
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#use-advanced-template-parameters
word_count: 386
---

First, download the following template of a Job to a file called `job-tmpl.yaml`.
Here's what you'll download:

```shell
# Use curl to download job-tmpl.yaml
curl -L -s -O https://k8s.io/examples/application/job/job-tmpl.yaml
```

The file you downloaded is not yet a valid Kubernetes
manifest.
Instead that template is a YAML representation of a Job object with some placeholders
that need to be filled in before it can be used.  The `$ITEM` syntax is not meaningful to Kubernetes.

### Create manifests from the template

The following shell snippet uses `sed` to replace the string `$ITEM` with the loop
variable, writing into a temporary directory named `jobs`. Run this now:

```shell
# Expand the template into multiple files, one for each item to be processed.
mkdir ./jobs
for i in apple banana cherry
do
  cat job-tmpl.yaml | sed "s/\$ITEM/$i/" > ./jobs/job-$i.yaml
done
```

Check if it worked:

```shell
ls jobs/
```

The output is similar to this:

```
job-apple.yaml
job-banana.yaml
job-cherry.yaml
```

You could use any type of template language (for example: Jinja2; ERB), or
write a program to generate the Job manifests.

### Create Jobs from the manifests

Next, create all the Jobs with one kubectl command:

```shell
kubectl create -f ./jobs
```

The output is similar to this:

```
job.batch/process-item-apple created
job.batch/process-item-banana created
job.batch/process-item-cherry created
```

Now, check on the jobs:

```shell
kubectl get jobs -l jobgroup=jobexample
```

The output is similar to this:

```
NAME                  COMPLETIONS   DURATION   AGE
process-item-apple    1/1           14s        22s
process-item-banana   1/1           12s        21s
process-item-cherry   1/1           12s        20s
```

Using the `-l` option to kubectl selects only the Jobs that are part
of this group of jobs (there might be other unrelated jobs in the system).

You can check on the Pods as well using the same
label selector:

```shell
kubectl get pods -l jobgroup=jobexample
```

The output is similar to:

```
NAME                        READY     STATUS      RESTARTS   AGE
process-item-apple-kixwv    0/1       Completed   0          4m
process-item-banana-wrsf7   0/1       Completed   0          4m
process-item-cherry-dnfu9   0/1       Completed   0          4m
```

We can use this single command to check on the output of all jobs at once:

```shell
kubectl logs -f -l jobgroup=jobexample
```

The output should be:

```
Processing item apple
Processing item banana
Processing item cherry
```

### Clean up {#cleanup-1}

```shell
# Remove the Jobs you created
# Your cluster automatically cleans up their Pods
kubectl delete job -l jobgroup=jobexample
```
