---
id: okf-relations/entities/ingress
kind: entity
title: Ingress
description: Routes external HTTP/HTTPS traffic to Services inside the cluster based
  on host/path rules.
outgoing_relations:
- okf-relations/edges/009-ingress-service
- okf-relations/edges/010-ingress-ingress-class
incoming_relations: []
primary_sources:
- concepts/services-networking/ingress-controllers.md
- concepts/services-networking/ingress.md
source: concepts/services-networking/ingress-controllers.md
word_count: 22
---

Ingress: Routes external HTTP/HTTPS traffic to Services inside the cluster based on host/path rules. Ingress routes to Service. Ingress implemented by IngressClass.
