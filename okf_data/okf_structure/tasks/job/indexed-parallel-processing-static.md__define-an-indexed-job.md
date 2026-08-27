---
id: okf-structure/tasks/job/indexed-parallel-processing-static.md#define-an-indexed-job
kind: section
title: Define an Indexed Job
source: tasks/job/indexed-parallel-processing-static.md
url: https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/
heading: Define an Indexed Job
parent: okf-structure/tasks/job/indexed-parallel-processing-static
children: []
prev_sibling: okf-structure/tasks/job/indexed-parallel-processing-static.md#choose-an-approach
next_sibling: okf-structure/tasks/job/indexed-parallel-processing-static.md#running-the-job
word_count: 119
---

Here is a sample Job manifest that uses `Indexed` completion mode:

In the example above, you use the builtin `JOB_COMPLETION_INDEX` environment
variable set by the Job controller for all containers. An init container
maps the index to a static value and writes it to a file that is shared with the
container running the worker through an emptyDir volume.
Optionally, you can define your own environment variable through the downward
API
to publish the index to containers. You can also choose to load a list of values
from a ConfigMap as an environment variable or file.

Alternatively, you can directly use the downward API to pass the annotation
value as a volume file,
like shown in the following example:
