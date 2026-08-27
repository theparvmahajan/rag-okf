---
id: okf-relations/entities/storage-class
kind: entity
title: StorageClass
description: Describes a class of storage and its provisioner, used to dynamically
  create a PersistentVolume for a claim.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/016-persistent-volume-claim-storage-class
primary_sources:
- tasks/administer-cluster/change-default-storage-class.md
source: tasks/administer-cluster/change-default-storage-class.md
word_count: 22
---

StorageClass: Describes a class of storage and its provisioner, used to dynamically create a PersistentVolume for a claim. PersistentVolumeClaim provisioned via StorageClass.
