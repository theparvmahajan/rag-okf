---
id: okf-structure/tasks/inject-data-application/define-command-argument-container.md#run-a-command-in-a-shell
kind: section
title: Run a command in a shell
source: tasks/inject-data-application/define-command-argument-container.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/
heading: Run a command in a shell
parent: okf-structure/tasks/inject-data-application/define-command-argument-container
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#use-environment-variables-to-define-arguments
next_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#whatsnext
word_count: 54
---

In some cases, you need your command to run in a shell. For example, your
command might consist of several commands piped together, or it might be a shell
script. To run your command in a shell, wrap it like this:

```shell
command: ["/bin/sh"]
args: ["-c", "while true; do echo hello; sleep 10;done"]
```
