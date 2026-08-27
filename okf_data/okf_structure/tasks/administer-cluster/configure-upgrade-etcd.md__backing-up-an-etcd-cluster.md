---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#backing-up-an-etcd-cluster
kind: section
title: Backing up an etcd cluster
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Backing up an etcd cluster
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#replacing-a-failed-etcd-member
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#scaling-out-etcd-clusters
word_count: 412
---

All Kubernetes objects are stored in etcd. Periodically backing up the etcd
cluster data is important to recover Kubernetes clusters under disaster
scenarios, such as losing all control plane nodes. The snapshot file contains
all the Kubernetes state and critical information. In order to keep the
sensitive Kubernetes data safe, encrypt the snapshot files.

Backing up an etcd cluster can be accomplished in two ways: etcd built-in
snapshot and volume snapshot.

### Built-in snapshot

etcd supports built-in snapshot. A snapshot may either be created from a live
member with the `etcdctl snapshot save` command or by copying the
`member/snap/db` file from an etcd
data directory
that is not currently used by an etcd process. Creating the snapshot will
not affect the performance of the member.

Below is an example for creating a snapshot of the keyspace served by
`$ENDPOINT` to the file `snapshot.db`:

```shell
ETCDCTL_API=3 etcdctl --endpoints $ENDPOINT snapshot save snapshot.db
```

Verify the snapshot:

   The below example depicts the usage of the `etcdutl` tool for verifying a snapshot:

   ```shell
   etcdutl --write-out=table snapshot status snapshot.db 
   ```

   This should generate an output resembling the example provided below:

   ```console
   +----------+----------+------------+------------+
   |   HASH   | REVISION | TOTAL KEYS | TOTAL SIZE |
   +----------+----------+------------+------------+
   | fe01cf57 |       10 |          7 | 2.1 MB     |
   +----------+----------+------------+------------+
   ```

   
   The usage of `etcdctl snapshot status` has been **deprecated** since etcd v3.5.x and is slated for removal from etcd v3.6.
   It is recommended to utilize `etcdutl` instead.
   

   The below example depicts the usage of the `etcdctl` tool for verifying a snapshot:

   ```shell
   export ETCDCTL_API=3
   etcdctl --write-out=table snapshot status snapshot.db
   ```

   This should generate an output resembling the example provided below:

   ```console
   Deprecated: Use `etcdutl snapshot status` instead.

   +----------+----------+------------+------------+
   |   HASH   | REVISION | TOTAL KEYS | TOTAL SIZE |
   +----------+----------+------------+------------+
   | fe01cf57 |       10 |          7 | 2.1 MB     |
   +----------+----------+------------+------------+
   ```

### Volume snapshot

If etcd is running on a storage volume that supports backup, such as Amazon
Elastic Block Store, back up etcd data by creating a snapshot of the storage
volume.

### Snapshot using etcdctl options

We can also create the snapshot using various options given by etcdctl. For example: 

```shell
ETCDCTL_API=3 etcdctl -h 
``` 

will list various options available from etcdctl. For example, you can create a snapshot by specifying
the endpoint, certificates and key as shown below:

```shell
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=<trusted-ca-file> --cert=<cert-file> --key=<key-file> \
  snapshot save <backup-file-location>
```
where `trusted-ca-file`, `cert-file` and `key-file` can be obtained from the description of the etcd Pod.
