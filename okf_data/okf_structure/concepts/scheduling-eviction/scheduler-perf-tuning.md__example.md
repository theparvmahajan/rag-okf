---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#example
kind: section
title: Example
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: Example
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#node-scoring-threshold-percentage-of-nodes-to-score
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#tuning-percentageofnodestoscore
word_count: 22
---

Below is an example configuration that sets `percentageOfNodesToScore` to 50%.

```yaml
apiVersion: kubescheduler.config.k8s.io/v1alpha1
kind: KubeSchedulerConfiguration
algorithmSource:
  provider: DefaultProvider

...

percentageOfNodesToScore: 50
```
