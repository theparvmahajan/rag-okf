---
id: okf-structure/concepts/cluster-administration/dra.md#separate-permissions-to-dra-related-apis
kind: section
title: Separate permissions to DRA related APIs
source: concepts/cluster-administration/dra.md
url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
heading: Separate permissions to DRA related APIs
parent: okf-structure/concepts/cluster-administration/dra
children: []
prev_sibling: okf-structure/concepts/cluster-administration/dra.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/dra.md#dra-driver-deployment-and-maintenance
word_count: 69
---

DRA is orchestrated through a number of different APIs. Use authorization tools
(like RBAC, or another solution) to control access to the right APIs depending
on the persona of your user.

In general, DeviceClasses and ResourceSlices should be restricted to admins and
the DRA drivers. Cluster operators that will be deploying Pods with claims will
need access to ResourceClaim and ResourceClaimTemplate APIs; both of these APIs
are namespace scoped.
