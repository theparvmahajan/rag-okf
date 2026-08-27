---
id: okf-structure/tasks/administer-cluster/nodelocaldns.md#setting-memory-limits
kind: section
title: Setting memory limits
source: tasks/administer-cluster/nodelocaldns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/
heading: Setting memory limits
parent: okf-structure/tasks/administer-cluster/nodelocaldns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#stubdomains-and-upstream-server-configuration
next_sibling: null
word_count: 263
---

The `node-local-dns` Pods use memory for storing cache entries and processing queries.
Since they do not watch Kubernetes objects, the cluster size or the number of Services / EndpointSlices do not directly affect memory usage. Memory usage is influenced by the DNS query pattern.
From CoreDNS docs,
> The default cache size is 10000 entries, which uses about 30 MB when completely filled.

This would be the memory usage for each server block (if the cache gets completely filled).
Memory usage can be reduced by specifying smaller cache sizes.

The number of concurrent queries is linked to the memory demand, because each extra
goroutine used for handling a query requires an amount of memory. You can set an upper limit
using the `max_concurrent` option in the forward plugin.

If a `node-local-dns` Pod attempts to use more memory than is available (because of total system
resources, or because of a configured
resource limit), the operating system
may shut down that pod's container.
If this happens, the container that is terminated (“OOMKilled”) does not clean up the custom
packet filtering rules that it previously added during startup.
The `node-local-dns` container should get restarted (since managed as part of a DaemonSet), but this
will lead to a brief DNS downtime each time that the container fails: the packet filtering rules direct
DNS queries to a local Pod that is unhealthy.

You can determine a suitable memory limit by running node-local-dns pods without a limit and
measuring the peak usage. You can also set up and use a
VerticalPodAutoscaler
in _recommender mode_, and then check its recommendations.
