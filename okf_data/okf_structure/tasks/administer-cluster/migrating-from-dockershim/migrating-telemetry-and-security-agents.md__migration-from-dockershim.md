---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#migration-from-dockershim
kind: section
title: Migration from dockershim
source: tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/
heading: Migration from dockershim
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#telemetry-and-security-agents
next_sibling: null
word_count: 299
---

### Aqua

No changes are needed: everything should work seamlessly on the runtime switch.

### Datadog

How to migrate:
Docker deprecation in Kubernetes
The pod that accesses Docker Engine may have a name containing any of:

- `datadog-agent`
- `datadog`
- `dd-agent`

### Dynatrace

How to migrate:
Migrating from Docker-only to generic container metrics in Dynatrace

Containerd support announcement: Get automated full-stack visibility into
containerd-based Kubernetes
environments

CRI-O support announcement: Get automated full-stack visibility into your CRI-O Kubernetes containers (Beta)

The pod accessing Docker may have name containing: 
- `dynatrace-oneagent`

### Falco

How to migrate:

Migrate Falco from dockershim
Falco supports any CRI-compatible runtime (containerd is used in the default configuration); the documentation explains all details.
The pod accessing Docker may have name containing: 
- `falco`

### Prisma Cloud Compute

Check documentation for Prisma Cloud,
under the "Install Prisma Cloud on a CRI (non-Docker) cluster" section.
The pod accessing Docker may be named like:
- `twistlock-defender-ds`

### SignalFx (Splunk)

The SignalFx Smart Agent (deprecated) uses several different monitors for Kubernetes including
`kubernetes-cluster`, `kubelet-stats/kubelet-metrics`, and `docker-container-stats`.
The `kubelet-stats` monitor was previously deprecated by the vendor, in favor of `kubelet-metrics`.
The `docker-container-stats` monitor is the one affected by dockershim removal.
Do not use the `docker-container-stats` with container runtimes other than Docker Engine.

How to migrate from dockershim-dependent agent:
1. Remove `docker-container-stats` from the list of configured monitors.
   Note, keeping this monitor enabled with non-dockershim runtime will result in incorrect metrics
   being reported when docker is installed on node and no metrics when docker is not installed.
2. Enable and configure `kubelet-metrics` monitor.

The set of collected metrics will change. Review your alerting rules and dashboards.

The Pod accessing Docker may be named something like:

- `signalfx-agent`

### Yahoo Kubectl Flame

Flame does not support container runtimes other than Docker. See
https://github.com/yahoo/kubectl-flame/issues/51
