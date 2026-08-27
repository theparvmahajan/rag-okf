---
id: okf-structure/concepts/cluster-administration/system-metrics.md#metric-lifecycle
kind: section
title: Metric lifecycle
source: concepts/cluster-administration/system-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/
heading: Metric lifecycle
parent: okf-structure/concepts/cluster-administration/system-metrics
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#metrics-in-kubernetes
next_sibling: okf-structure/concepts/cluster-administration/system-metrics.md#show-hidden-metrics
word_count: 275
---

Alpha metric → Beta metric → Stable metric →  Deprecated metric →  Hidden metric → Deleted metric

Alpha metrics have no stability guarantees. These metrics can be modified or deleted at any time.

Beta metrics observe a looser API contract than its stable counterparts. No labels can be removed from beta metrics during their lifetime, however, labels can be added while the metric is in the beta stage.

Stable metrics are guaranteed to not change. This means:

* A stable metric without a deprecated signature will not be deleted or renamed
* A stable metric's type will not be modified

Deprecated metrics are slated for deletion, but are still available for use.
These metrics include an annotation about the version in which they became deprecated.

For example:

* Before deprecation

  ```
  # HELP some_counter this counts things
  # TYPE some_counter counter
  some_counter 0
  ```

* After deprecation

  ```
  # HELP some_counter (Deprecated since 1.15.0) this counts things
  # TYPE some_counter counter
  some_counter 0
  ```

Hidden metrics are no longer published for scraping, but are still available for use.
A deprecated metric becomes a hidden metric after a period of time, based on its stability level:
* **STABLE** metrics become hidden after a minimum of 3 releases or 9 months, whichever is longer.
* **BETA** metrics become hidden after a minimum of 1 release or 4 months, whichever is longer.
* **ALPHA** metrics can be hidden or removed in the same release in which they are deprecated.

To use a hidden metric, you must enable it. For more details, refer to the Show hidden metrics section. 

Deleted metrics are no longer published and cannot be used.
