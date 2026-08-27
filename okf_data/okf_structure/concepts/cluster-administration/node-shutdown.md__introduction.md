---
id: okf-structure/concepts/cluster-administration/node-shutdown.md#introduction
kind: section
title: Node Shutdowns
source: concepts/cluster-administration/node-shutdown.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
heading: null
parent: okf-structure/concepts/cluster-administration/node-shutdown
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/node-shutdown.md#graceful-node-shutdown-graceful-node-shutdown
word_count: 137
---

In a Kubernetes cluster, a node
can be shut down in a planned graceful way or unexpectedly because of reasons such
as a power outage or something else external. A node shutdown could lead to workload
failure if the node is not drained before the shutdown. A node shutdown can be
either **graceful** or **non-graceful**.

The `unattended-upgrades` package from Debian conflicts with node graceful shutdown in
its normal configuration.
If you use the default configuration of `unattended-upgrades`, which customizes the server shutdown
grace period, then the kubelet fails to obtain the necessary lock to handle shutdown events properly.

This happens if the `shutdownGracePeriod` value is greater than 30 seconds.
To avoid this, you can suppress part of the `unattended-upgrades` configuration,
by making `/etc/systemd/logind.conf.d/unattended-upgrades-logind-maxdelay.conf` be a symbolic link
to `/dev/null`.

For more details, refer to the
`logind.conf` documentation.
