---
id: okf-structure/tasks/inject-data-application/define-command-argument-container.md#use-environment-variables-to-define-arguments
kind: section
title: Use environment variables to define arguments
source: tasks/inject-data-application/define-command-argument-container.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/
heading: Use environment variables to define arguments
parent: okf-structure/tasks/inject-data-application/define-command-argument-container
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#define-a-command-and-arguments-when-you-create-a-pod
next_sibling: okf-structure/tasks/inject-data-application/define-command-argument-container.md#run-a-command-in-a-shell
word_count: 86
---

In the preceding example, you defined the arguments directly by
providing strings. As an alternative to providing strings directly,
you can define arguments by using environment variables:

```yaml
env:
- name: MESSAGE
  value: "hello world"
command: ["/bin/echo"]
args: ["$(MESSAGE)"]
```

This means you can define an argument for a Pod using any of
the techniques available for defining environment variables, including
ConfigMaps
and
Secrets.

The environment variable appears in parentheses, `"$(VAR)"`. This is
required for the variable to be expanded in the `command` or `args` field.
