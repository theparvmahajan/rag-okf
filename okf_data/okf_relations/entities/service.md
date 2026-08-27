---
id: okf-relations/entities/service
kind: entity
title: Service
description: A stable virtual IP and DNS name that load-balances traffic to a dynamic
  set of Pods, found via a label selector.
outgoing_relations:
- okf-relations/edges/007-service-pod
- okf-relations/edges/008-service-endpoint-slice
incoming_relations:
- okf-relations/edges/009-ingress-service
- okf-relations/edges/028-namespace-service
primary_sources:
- concepts/security/service-accounts.md
- concepts/services-networking/_index.md
source: concepts/security/service-accounts.md
word_count: 36
---

Service: A stable virtual IP and DNS name that load-balances traffic to a dynamic set of Pods, found via a label selector. Service selects Pod. Service backed by EndpointSlice. Ingress routes to Service. Namespace scopes Service.
