---
id: okf-relations/entities/daemon-set
kind: entity
title: DaemonSet
description: Ensures a copy of a Pod runs on every (or every matching) Node in the
  cluster, added or removed as Nodes join or leave.
outgoing_relations:
- okf-relations/edges/004-daemon-set-pod
incoming_relations: []
primary_sources:
- concepts/workloads/controllers/daemonset.md
- tasks/manage-daemon/create-daemon-set.md
source: concepts/workloads/controllers/daemonset.md
word_count: 28
---

DaemonSet: Ensures a copy of a Pod runs on every (or every matching) Node in the cluster, added or removed as Nodes join or leave. DaemonSet owns Pod.
