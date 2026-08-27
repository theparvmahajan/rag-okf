---
id: okf-structure/tasks/job/indexed-parallel-processing-static.md#choose-an-approach
kind: section
title: Choose an approach
source: tasks/job/indexed-parallel-processing-static.md
url: https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/
heading: Choose an approach
parent: okf-structure/tasks/job/indexed-parallel-processing-static
children: []
prev_sibling: okf-structure/tasks/job/indexed-parallel-processing-static.md#prerequisites
next_sibling: okf-structure/tasks/job/indexed-parallel-processing-static.md#define-an-indexed-job
word_count: 213
---

To access the work item from the worker program, you have a few options:

1. Read the `JOB_COMPLETION_INDEX` environment variable. The Job
   controller
   automatically links this variable to the annotation containing the completion
   index.
1. Read a file that contains the completion index.
1. Assuming that you can't modify the program, you can wrap it with a script
   that reads the index using any of the methods above and converts it into
   something that the program can use as input.

For this example, imagine that you chose option 3 and you want to run the
rev utility. This
program accepts a file as an argument and prints its content reversed.

```shell
rev data.txt
```

You'll use the `rev` tool from the
`busybox` container image.

As this is only an example, each Pod only does a tiny piece of work (reversing a short
string). In a real workload you might, for example, create a Job that represents
 the
task of producing 60 seconds of video based on scene data.
Each work item in the video rendering Job would be to render a particular
frame of that video clip. Indexed completion would mean that each Pod in
the Job knows which frame to render and publish, by counting frames from
the start of the clip.
