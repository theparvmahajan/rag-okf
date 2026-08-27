---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#replacing-a-failed-etcd-member
kind: section
title: Replacing a failed etcd member
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Replacing a failed etcd member
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#securing-etcd-clusters
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#backing-up-an-etcd-cluster
word_count: 394
---

etcd cluster achieves high availability by tolerating minor member failures.
However, to improve the overall health of the cluster, replace failed members
immediately. When multiple members fail, replace them one by one. Replacing a
failed member involves two steps: removing the failed member and adding a new
member.

Though etcd keeps unique member IDs internally, it is recommended to use a
unique name for each member to avoid human errors. For example, consider a
three-member etcd cluster. Let the URLs be, `member1=http://10.0.0.1`,
`member2=http://10.0.0.2`, and `member3=http://10.0.0.3`. When `member1` fails,
replace it with `member4=http://10.0.0.4`.

1. Get the member ID of the failed `member1`:

   ```shell
   etcdctl --endpoints=http://10.0.0.2,http://10.0.0.3 member list
   ```

   The following message is displayed:

   ```console
   8211f1d0f64f3269, started, member1, http://10.0.0.1:2380, http://10.0.0.1:2379
   91bc3c398fb3c146, started, member2, http://10.0.0.2:2380, http://10.0.0.2:2379
   fd422379fda50e48, started, member3, http://10.0.0.3:2380, http://10.0.0.3:2379
   ```

1. Do either of the following:

   1. If each Kubernetes API server is configured to communicate with all etcd
      members, remove the failed member from the `--etcd-servers` flag, then
      restart each Kubernetes API server.
   1. If each Kubernetes API server communicates with a single etcd member,
      then stop the Kubernetes API server that communicates with the failed
      etcd.

1. Stop the etcd server on the broken node. It is possible that other 
   clients besides the Kubernetes API server are causing traffic to etcd 
   and it is desirable to stop all traffic to prevent writes to the data
   directory.

1. Remove the failed member:

   ```shell
   etcdctl member remove 8211f1d0f64f3269
   ```

   The following message is displayed:

   ```console
   Removed member 8211f1d0f64f3269 from cluster
   ```

1. Add the new member:

   ```shell
   etcdctl member add member4 --peer-urls=http://10.0.0.4:2380
   ```

   The following message is displayed:

   ```console
   Member 2be1eb8f84b7f63e added to cluster ef37ad9dc622a7c4
   ```

1. Start the newly added member on a machine with the IP `10.0.0.4`:

   ```shell
   export ETCD_NAME="member4"
   export ETCD_INITIAL_CLUSTER="member2=http://10.0.0.2:2380,member3=http://10.0.0.3:2380,member4=http://10.0.0.4:2380"
   export ETCD_INITIAL_CLUSTER_STATE=existing
   etcd [flags]
   ```

1. Do either of the following:

   1. If each Kubernetes API server is configured to communicate with all etcd
      members, add the newly added member to the `--etcd-servers` flag, then
      restart each Kubernetes API server.
   1. If each Kubernetes API server communicates with a single etcd member,
      start the Kubernetes API server that was stopped in step 2. Then
      configure Kubernetes API server clients to again route requests to the
      Kubernetes API server that was stopped. This can often be done by
      configuring a load balancer.

For more information on cluster reconfiguration, see
etcd reconfiguration documentation.
