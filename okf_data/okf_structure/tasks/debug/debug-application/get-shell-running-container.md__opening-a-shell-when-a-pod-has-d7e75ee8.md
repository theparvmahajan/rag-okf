---
id: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#opening-a-shell-when-a-pod-has-more-than-one-container
kind: section
title: Opening a shell when a Pod has more than one container
source: tasks/debug/debug-application/get-shell-running-container.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/
heading: Opening a shell when a Pod has more than one container
parent: okf-structure/tasks/debug/debug-application/get-shell-running-container
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#running-individual-commands-in-a-container
next_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#whatsnext
word_count: 78
---

If a Pod has more than one container, use `--container` or `-c` to
specify a container in the `kubectl exec` command. For example,
suppose you have a Pod named my-pod, and the Pod has two containers
named _main-app_ and _helper-app_. The following command would open a
shell to the _main-app_ container.

```shell
kubectl exec -i -t my-pod --container main-app -- /bin/bash
```

The short options `-i` and `-t` are the same as the long options `--stdin` and `--tty`
