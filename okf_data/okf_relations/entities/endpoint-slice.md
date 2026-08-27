---
id: okf-relations/entities/endpoint-slice
kind: entity
title: EndpointSlice
description: Tracks the actual set of network endpoints (Pod IPs and ports) that currently
  match a Service's selector.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/008-service-endpoint-slice
primary_sources:
- concepts/services-networking/endpoint-slices.md
source: concepts/services-networking/endpoint-slices.md
word_count: 22
---

EndpointSlice: Tracks the actual set of network endpoints (Pod IPs and ports) that currently match a Service's selector. Service backed by EndpointSlice.
