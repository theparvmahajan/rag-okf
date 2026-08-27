---
id: okf-relations/entities/persistent-volume-claim
kind: entity
title: PersistentVolumeClaim
description: A Pod's request for storage, bound to a matching PersistentVolume so
  the Pod can mount it.
outgoing_relations:
- okf-relations/edges/015-persistent-volume-claim-persistent-volume
- okf-relations/edges/016-persistent-volume-claim-storage-class
incoming_relations:
- okf-relations/edges/014-pod-persistent-volume-claim
primary_sources: []
source: null
word_count: 29
---

PersistentVolumeClaim: A Pod's request for storage, bound to a matching PersistentVolume so the Pod can mount it. PersistentVolumeClaim binds PersistentVolume. PersistentVolumeClaim provisioned via StorageClass. Pod claims storage via PersistentVolumeClaim.
