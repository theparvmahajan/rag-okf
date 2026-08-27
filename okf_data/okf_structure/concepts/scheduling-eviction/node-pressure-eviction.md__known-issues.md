---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#known-issues
kind: section
title: Known issues
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Known issues
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#good-practices-node-pressure-eviction-good-practices
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#whatsnext
word_count: 275
---

The following sections describe known issues related to out of resource handling.

### kubelet may not observe memory pressure right away

By default, the kubelet polls cAdvisor to collect memory usage stats at a
regular interval. If memory usage increases within that window rapidly, the
kubelet may not observe `MemoryPressure` fast enough, and the OOM killer
will still be invoked.

You can use the `--kernel-memcg-notification` flag to enable the `memcg`
notification API on the kubelet to get notified immediately when a threshold
is crossed.

If you are not trying to achieve extreme utilization, but a sensible measure of
overcommit, a viable workaround for this issue is to use the `--kube-reserved`
and `--system-reserved` flags to allocate memory for the system.

### active_file memory is not considered as available memory

On Linux, the kernel tracks the number of bytes of file-backed memory on active
least recently used (LRU) list as the `active_file` statistic. The kubelet treats `active_file` memory
areas as not reclaimable. For workloads that make intensive use of block-backed
local storage, including ephemeral local storage, kernel-level caches of file
and block data means that many recently accessed cache pages are likely to be
counted as `active_file`. If enough of these kernel block buffers are on the
active LRU list, the kubelet is liable to observe this as high resource use and
taint the node as experiencing memory pressure - triggering pod eviction.

For more details, see https://github.com/kubernetes/kubernetes/issues/43916

You can work around that behavior by setting the memory limit and memory request
the same for containers likely to perform intensive I/O activity. You will need
to estimate or measure an optimal memory limit value for that container.
