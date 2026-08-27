---
id: okf-relations/entities/secret
kind: entity
title: Secret
description: Like a ConfigMap but for sensitive data (credentials, tokens, keys),
  with extra access and storage conventions.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/013-pod-secret
primary_sources:
- concepts/configuration/secret.md
- concepts/security/secrets-good-practices.md
source: concepts/configuration/secret.md
word_count: 20
---

Secret: Like a ConfigMap but for sensitive data (credentials, tokens, keys), with extra access and storage conventions. Pod mounts Secret.
