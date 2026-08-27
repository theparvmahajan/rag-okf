---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#known-issues
kind: section
title: Known issues
source: tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/
heading: Known issues
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#dependency-on-docker-explained-role-of-dockershim
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you.md#whatsnext
word_count: 176
---

### Some filesystem metrics are missing and the metrics format is different

The Kubelet `/metrics/cadvisor` endpoint provides Prometheus metrics,
as documented in Metrics for Kubernetes system components.
If you install a metrics collector that depends on that endpoint, you might see the following issues:

- The metrics format on the Docker node is `k8s_<container-name>_<pod-name>_<namespace>_<pod-uid>_<restart-count>`
  but the format on other runtime is different. For example, on containerd node it is `<container-id>`.
- Some filesystem metrics are missing, as follows:
  ```
  container_fs_inodes_free
  container_fs_inodes_total
  container_fs_io_current
  container_fs_io_time_seconds_total
  container_fs_io_time_weighted_seconds_total
  container_fs_limit_bytes
  container_fs_read_seconds_total
  container_fs_reads_merged_total
  container_fs_sector_reads_total
  container_fs_sector_writes_total
  container_fs_usage_bytes
  container_fs_write_seconds_total
  container_fs_writes_merged_total
  ```

#### Workaround

You can mitigate this issue by using cAdvisor as a standalone daemonset.

1. Find the latest cAdvisor release
   with the name pattern `vX.Y.Z-containerd-cri` (for example, `v0.42.0-containerd-cri`).
2. Follow the steps in cAdvisor Kubernetes Daemonset to create the daemonset.
3. Point the installed metrics collector to use the cAdvisor `/metrics` endpoint
   which provides the full set of
   Prometheus container metrics.

Alternatives:

- Use alternative third party metrics collection solution.
- Collect metrics from the Kubelet summary API that is served at `/stats/summary`.
