---
id: okf-relations/entities/stateful-set
kind: entity
title: StatefulSet
description: Manages Pods that need a stable network identity, stable storage, and
  ordered, sequential deployment/scaling.
outgoing_relations:
- okf-relations/edges/003-stateful-set-pod
incoming_relations: []
primary_sources:
- concepts/workloads/controllers/statefulset.md
- tasks/debug/debug-application/debug-statefulset.md
source: concepts/workloads/controllers/statefulset.md
word_count: 18
---

StatefulSet: Manages Pods that need a stable network identity, stable storage, and ordered, sequential deployment/scaling. StatefulSet owns Pod.
