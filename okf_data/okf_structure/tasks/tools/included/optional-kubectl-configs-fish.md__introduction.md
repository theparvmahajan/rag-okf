---
id: okf-structure/tasks/tools/included/optional-kubectl-configs-fish.md#introduction
kind: section
title: fish auto-completion
source: tasks/tools/included/optional-kubectl-configs-fish.md
url: https://kubernetes.io/docs/tasks/tools/included/optional-kubectl-configs-fish/
heading: null
parent: okf-structure/tasks/tools/included/optional-kubectl-configs-fish
children: []
prev_sibling: null
next_sibling: null
word_count: 65
---

Autocomplete for Fish requires kubectl 1.23 or later.

The kubectl completion script for Fish can be generated with the command `kubectl completion fish`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following line to your `~/.config/fish/config.fish` file:

```shell
kubectl completion fish | source
```

After reloading your shell, kubectl autocompletion should be working.
