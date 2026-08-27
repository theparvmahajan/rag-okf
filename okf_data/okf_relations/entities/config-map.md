---
id: okf-relations/entities/config-map
kind: entity
title: ConfigMap
description: Holds non-secret configuration data as key/value pairs that can be injected
  into Pods as env vars, files, or CLI args.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/012-pod-config-map
primary_sources:
- concepts/configuration/configmap.md
- tasks/configure-pod-container/configure-pod-configmap.md
source: concepts/configuration/configmap.md
word_count: 24
---

ConfigMap: Holds non-secret configuration data as key/value pairs that can be injected into Pods as env vars, files, or CLI args. Pod mounts ConfigMap.
