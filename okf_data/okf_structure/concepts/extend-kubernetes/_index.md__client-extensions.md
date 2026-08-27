---
id: okf-structure/concepts/extend-kubernetes/_index.md#client-extensions
kind: section
title: Client extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: Client extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#extensions
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#api-extensions
word_count: 52
---

Plugins for kubectl are separate binaries that add or replace the behavior of specific subcommands.
The `kubectl` tool can also integrate with credential plugins
These extensions only affect a individual user's local environment, and so cannot enforce site-wide policies.

If you want to extend the `kubectl` tool, read Extend kubectl with plugins.
