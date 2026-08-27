---
id: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#using-environment-variables-inside-of-your-config
kind: section
title: Using environment variables inside of your config
source: tasks/inject-data-application/define-environment-variable-container.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/
heading: Using environment variables inside of your config
parent: okf-structure/tasks/inject-data-application/define-environment-variable-container
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#define-an-environment-variable-for-a-container
next_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#whatsnext
word_count: 156
---

Environment variables that you define in a Pod's configuration under 
`.spec.containers[*].env[*]` can be used elsewhere in the configuration, for 
example in commands and arguments that you set for the Pod's containers.
In the example configuration below, the `GREETING`, `HONORIFIC`, and
`NAME` environment variables are set to `Warm greetings to`, `The Most
Honorable`, and `Kubernetes`, respectively. The environment variable 
`MESSAGE` combines the set of all these environment variables and then uses it 
as a CLI argument passed to the `env-print-demo` container.

Environment variable names may consist of any printable ASCII characters except '='.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: print-greeting
spec:
  containers:
  - name: env-print-demo
    image: bash
    env:
    - name: GREETING
      value: "Warm greetings to"
    - name: HONORIFIC
      value: "The Most Honorable"
    - name: NAME
      value: "Kubernetes"
    - name: MESSAGE
      value: "$(GREETING) $(HONORIFIC) $(NAME)"
    command: ["echo"]
    args: ["$(MESSAGE)"]
```

Upon creation, the command `echo Warm greetings to The Most Honorable Kubernetes` is run on the container.
