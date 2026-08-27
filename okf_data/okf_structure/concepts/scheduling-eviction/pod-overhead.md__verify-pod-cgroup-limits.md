---
id: okf-structure/concepts/scheduling-eviction/pod-overhead.md#verify-pod-cgroup-limits
kind: section
title: Verify Pod cgroup limits
source: concepts/scheduling-eviction/pod-overhead.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
heading: Verify Pod cgroup limits
parent: okf-structure/concepts/scheduling-eviction/pod-overhead
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-overhead.md#usage-example
next_sibling: okf-structure/concepts/scheduling-eviction/pod-overhead.md#whatsnext
word_count: 226
---

Check the Pod's memory cgroups on the node where the workload is running. In the following example,
`crictl`
is used on the node, which provides a CLI for CRI-compatible container runtimes. This is an
advanced example to show Pod overhead behavior, and it is not expected that users should need to check
cgroups directly on the node.

First, on the particular node, determine the Pod identifier:

```bash
# Run this on the node where the Pod is scheduled
POD_ID="$(sudo crictl pods --name test-pod -q)"
```

From this, you can determine the cgroup path for the Pod:

```bash
# Run this on the node where the Pod is scheduled
sudo crictl inspectp -o=json $POD_ID | grep cgroupsPath
```

The resulting cgroup path includes the Pod's `pause` container. The Pod level cgroup is one directory above.

```
  "cgroupsPath": "/kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2/7ccf55aee35dd16aca4189c952d83487297f3cd760f1bbf09620e206e7d0c27a"
```

In this specific case, the pod cgroup path is `kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2`.
Verify the Pod level cgroup setting for memory:

```bash
# Run this on the node where the Pod is scheduled.
# Also, change the name of the cgroup to match the cgroup allocated for your pod.
 cat /sys/fs/cgroup/memory/kubepods/podd7f4b509-cf94-4951-9417-d1087c92a5b2/memory.limit_in_bytes
```

This is 320 MiB, as expected:

```
335544320
```

### Observability

Some `kube_pod_overhead_*` metrics are available in kube-state-metrics
to help identify when Pod overhead is being utilized and to help observe stability of workloads
running with a defined overhead.
