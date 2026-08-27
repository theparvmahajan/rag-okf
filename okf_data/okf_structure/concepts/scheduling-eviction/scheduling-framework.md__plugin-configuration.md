---
id: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#plugin-configuration
kind: section
title: Plugin configuration
source: concepts/scheduling-eviction/scheduling-framework.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
heading: Plugin configuration
parent: okf-structure/concepts/scheduling-eviction/scheduling-framework
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduling-framework.md#plugin-api
next_sibling: null
word_count: 91
---

You can enable or disable plugins in the scheduler configuration. If you are using
Kubernetes v1.18 or later, most scheduling
plugins are in use and
enabled by default.

In addition to default plugins, you can also implement your own scheduling
plugins and get them configured along with default plugins. You can visit
scheduler-plugins for more details.

If you are using Kubernetes v1.18 or later, you can configure a set of plugins as
a scheduler profile and then define multiple profiles to fit various kinds of workload.
Learn more at multiple profiles.
