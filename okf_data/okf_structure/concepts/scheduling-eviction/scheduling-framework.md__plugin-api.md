---
id: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#plugin-api
kind: section
title: Plugin API
source: concepts/scheduling-eviction/scheduling-framework.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
heading: Plugin API
parent: okf-structure/concepts/scheduling-eviction/scheduling-framework
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#interfaces
next_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#plugin-configuration
word_count: 59
---

There are two steps to the plugin API. First, plugins must register and get
configured, then they use the extension point interfaces. Extension point
interfaces have the following form.

```go
type Plugin interface {
    Name() string
}

type QueueSortPlugin interface {
    Plugin
    Less(*v1.pod, *v1.pod) bool
}

type PreFilterPlugin interface {
    Plugin
    PreFilter(context.Context, *framework.CycleState, *v1.pod) error
}

// ...
```
