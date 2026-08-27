---
id: okf-structure/tasks/job/parallel-processing-expansion.md#prerequisites
kind: section
title: Prerequisites
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Prerequisites
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#introduction
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#create-jobs-based-on-a-template
word_count: 58
---

You should be familiar with the basic,
non-parallel, use of Job.

For basic templating you need the command-line utility `sed`.

To follow the advanced templating example, you need a working installation of
Python, and the Jinja2 template
library for Python.

Once you have Python set up, you can install Jinja2 by running:

```shell
pip install --user jinja2
```
