---
id: okf-structure/tasks/job/parallel-processing-expansion.md#use-advanced-template-parameters
kind: section
title: Use advanced template parameters
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Use advanced template parameters
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#create-jobs-based-on-a-template
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#using-jobs-in-real-workloads
word_count: 385
---

In the first example, each instance of the template had one
parameter, and that parameter was also used in the Job's name. However,
names are restricted
to contain only certain characters.

This slightly more complex example uses the
Jinja template language to generate manifests
and then objects from those manifests, with a multiple parameters for each Job.

For this part of the task, you are going to use a one-line Python script to
convert the template to a set of manifests.

First, copy and paste the following template of a Job object, into a file called `job.yaml.jinja2`:

```liquid
{% set params = [{ "name": "apple", "url": "http://dbpedia.org/resource/Apple", },
                  { "name": "banana", "url": "http://dbpedia.org/resource/Banana", },
                  { "name": "cherry", "url": "http://dbpedia.org/resource/Cherry" }]
%}
{% for p in params %}
{% set name = p["name"] %}
{% set url = p["url"] %}
---
apiVersion: batch/v1
kind: Job
metadata:
  name: jobexample-{{ name }}
  labels:
    jobgroup: jobexample
spec:
  template:
    metadata:
      name: jobexample
      labels:
        jobgroup: jobexample
    spec:
      containers:
      - name: c
        image: busybox:1.28
        command: ["sh", "-c", "echo Processing URL {{ url }} && sleep 5"]
      restartPolicy: Never
{% endfor %}
```

The above template defines two parameters for each Job object using a list of
python dicts (lines 1-4). A `for` loop emits one Job manifest for each
set of parameters (remaining lines).

This example relies on a feature of YAML. One YAML file can contain multiple
documents (Kubernetes manifests, in this case), separated by `---` on a line
by itself.
You can pipe the output directly to `kubectl` to create the Jobs.

Next, use this one-line Python program to expand the template:

```shell
alias render_template='python -c "from jinja2 import Template; import sys; print(Template(sys.stdin.read()).render());"'
```

Use `render_template` to convert the parameters and template into a single
YAML file containing Kubernetes manifests:

```shell
# This requires the alias you defined earlier
cat job.yaml.jinja2 | render_template > jobs.yaml
```

You can view `jobs.yaml` to verify that the `render_template` script worked
correctly.

Once you are happy that `render_template` is working how you intend,
you can pipe its output into `kubectl`:

```shell
cat job.yaml.jinja2 | render_template | kubectl apply -f -
```

Kubernetes accepts and runs the Jobs you created.

### Clean up {#cleanup-2}

```shell
# Remove the Jobs you created
# Your cluster automatically cleans up their Pods
kubectl delete job -l jobgroup=jobexample
```
