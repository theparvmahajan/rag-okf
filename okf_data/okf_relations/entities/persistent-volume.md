---
id: okf-relations/entities/persistent-volume
kind: entity
title: PersistentVolume
description: A piece of storage provisioned in the cluster, independent of any single
  Pod's lifecycle.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/015-persistent-volume-claim-persistent-volume
primary_sources:
- tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md
- tasks/administer-cluster/change-pv-reclaim-policy.md
source: tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md
word_count: 18
---

PersistentVolume: A piece of storage provisioned in the cluster, independent of any single Pod's lifecycle. PersistentVolumeClaim binds PersistentVolume.
