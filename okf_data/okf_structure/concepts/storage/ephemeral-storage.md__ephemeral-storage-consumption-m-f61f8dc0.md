---
id: okf-structure/concepts/storage/ephemeral-storage.md#ephemeral-storage-consumption-management-resource-emphemeralstorage-consumption
kind: section
title: Ephemeral storage consumption management {#resource-emphemeralstorage-consumption}
source: concepts/storage/ephemeral-storage.md
url: https://kubernetes.io/docs/concepts/storage/ephemeral-storage/
heading: Ephemeral storage consumption management {#resource-emphemeralstorage-consumption}
parent: okf-structure/concepts/storage/ephemeral-storage
children: []
prev_sibling: okf-structure/concepts/storage/ephemeral-storage.md#how-pods-with-ephemeral-storage-requests-are-scheduled
next_sibling: okf-structure/concepts/storage/ephemeral-storage.md#whatsnext
word_count: 689
---

If the kubelet is managing local ephemeral storage as a resource, then the
kubelet measures storage use in:

- `emptyDir` volumes, except _tmpfs_ `emptyDir` volumes
- directories holding node-level logs
- writeable container layers

If a Pod is using more ephemeral storage than you allow it to, the kubelet
sets an eviction signal that triggers Pod eviction.

For container-level isolation, if a container's writable layer and log
usage exceeds its storage limit, the kubelet marks the Pod for eviction.

For pod-level isolation the kubelet works out an overall Pod storage limit by
summing the limits for the containers in that Pod. In this case, if the sum of
the local ephemeral storage usage from all containers and also the Pod's `emptyDir`
volumes exceeds the overall Pod storage limit, then the kubelet also marks the Pod
for eviction.

If the kubelet is not measuring local ephemeral storage, then a Pod
that exceeds its local storage limit will not be evicted for breaching
local storage resource limits.

However, if the filesystem space for writeable container layers, node-level logs,
or `emptyDir` volumes falls low, the node
taints itself as short on local storage
and this taint triggers eviction for any Pods that don't specifically tolerate the taint.

See the supported configurations for ephemeral local storage.

The kubelet supports different ways to measure Pod storage use:

The kubelet performs regular, scheduled checks that scan each `emptyDir` volume,
container log directory, and writeable container layer.

The scan measures how much space is used.

In this mode, the kubelet does not track open file descriptors
for deleted files.

If you (or a container) create a file inside an `emptyDir` volume,
something then opens that file, and you delete the file while it is still open,
then the inode for the deleted file stays until you close that file
but the kubelet does not categorize the space as in use.

Project quotas are an operating-system level feature for managing
storage use on filesystems. With Kubernetes, you can enable project
quotas for monitoring storage use. Make sure that the filesystem
backing the `emptyDir` volumes, on the node, provides project quota support.
For example, XFS and ext4fs offer project quotas.

Project quotas let you monitor storage use; they do not enforce limits.

Kubernetes uses project IDs starting from `1048576`. The IDs in use are
registered in `/etc/projects` and `/etc/projid`. If project IDs in
this range are used for other purposes on the system, those project
IDs must be registered in `/etc/projects` and `/etc/projid` so that
Kubernetes does not use them.

Quotas are faster and more accurate than directory scanning.
When a directory is assigned to a project, all files created under a directory
are created in that project, and the kernel merely has to keep track of
how many blocks are in use by files in that project.
If a file is created and deleted, but has an open file descriptor,
it continues to consume space. Quota tracking records that space accurately
whereas directory scans overlook the storage used by deleted files.

To use quotas to track a pod's resource usage, the pod must be in 
a user namespace. Within user namespaces, the kernel restricts changes 
to projectIDs on the filesystem, ensuring the reliability of storage 
metrics calculated by quotas.

If you want to use project quotas, you should:

* Enable the `LocalStorageCapacityIsolationFSQuotaMonitoring=true`
  feature gate
  using the `featureGates` field in the
  kubelet configuration.

* Ensure the `UserNamespacesSupport` 
  feature gate
  is enabled, and that the kernel, CRI implementation and OCI runtime support user namespaces.

* Ensure that the root filesystem (or optional runtime filesystem)
  has project quotas enabled. All XFS filesystems support project quotas.
  For ext4 filesystems, you need to enable the project quota tracking feature
  while the filesystem is not mounted.

  ```bash
  # For ext4, with /dev/block-device not mounted
  sudo tune2fs -O project -Q prjquota /dev/block-device
  ```

* Ensure that the root filesystem (or optional runtime filesystem) is
  mounted with project quotas enabled. For both XFS and ext4fs, the
  mount option is named `prjquota`.

If you don't want to use project quotas, you should:

* Disable the `LocalStorageCapacityIsolationFSQuotaMonitoring`
  feature gate
  using the `featureGates` field in the
  kubelet configuration.
