---
id: okf-relations/entities/pod
kind: entity
title: Pod
description: The smallest deployable unit - one or more containers that share network
  and storage, scheduled together onto a single Node.
outgoing_relations:
- okf-relations/edges/012-pod-config-map
- okf-relations/edges/013-pod-secret
- okf-relations/edges/014-pod-persistent-volume-claim
- okf-relations/edges/017-pod-node
- okf-relations/edges/018-pod-service-account
- okf-relations/edges/026-pod-container
incoming_relations:
- okf-relations/edges/001-replica-set-pod
- okf-relations/edges/003-stateful-set-pod
- okf-relations/edges/004-daemon-set-pod
- okf-relations/edges/005-job-pod
- okf-relations/edges/007-service-pod
- okf-relations/edges/011-network-policy-pod
- okf-relations/edges/022-pod-disruption-budget-pod
- okf-relations/edges/025-priority-class-pod
- okf-relations/edges/027-namespace-pod
primary_sources:
- concepts/configuration/manage-resources-containers.md
- concepts/scheduling-eviction/assign-pod-node.md
source: concepts/configuration/manage-resources-containers.md
word_count: 72
---

Pod: The smallest deployable unit - one or more containers that share network and storage, scheduled together onto a single Node. Pod mounts ConfigMap. Pod mounts Secret. Pod claims storage via PersistentVolumeClaim. Pod scheduled onto Node. Pod authenticates as ServiceAccount. Pod contains Container. ReplicaSet owns Pod. StatefulSet owns Pod. DaemonSet owns Pod. Job owns Pod. Service selects Pod. NetworkPolicy selects Pod. PodDisruptionBudget protects Pod. PriorityClass assigns priority to Pod. Namespace scopes Pod.
