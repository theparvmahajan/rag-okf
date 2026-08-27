---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#introduction
kind: section
title: Migrating telemetry and security agents from dockershim
source: tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/
heading: null
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#telemetry-and-security-agents
word_count: 77
---

Kubernetes' support for direct integration with Docker Engine is deprecated and
has been removed. Most apps do not have a direct dependency on runtime hosting
containers. However, there are still a lot of telemetry and monitoring agents
that have a dependency on Docker to collect containers metadata, logs, and
metrics. This document aggregates information on how to detect these
dependencies as well as links on how to migrate these agents to use generic tools or
alternative runtimes.
