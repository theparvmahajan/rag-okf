---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#starting-etcd-clusters
kind: section
title: Starting etcd clusters
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Starting etcd clusters
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#understanding-etcdctl-and-etcdutl
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#securing-etcd-clusters
word_count: 277
---

This section covers starting a single-node and multi-node etcd cluster.

This guide assumes that `etcd` is already installed.

### Single-node etcd cluster

Use a single-node etcd cluster only for testing purposes.

1. Run the following:

   ```sh
   etcd --listen-client-urls=http://$PRIVATE_IP:2379 \
      --advertise-client-urls=http://$PRIVATE_IP:2379
   ```

2. Start the Kubernetes API server with the flag
   `--etcd-servers=$PRIVATE_IP:2379`.

   Make sure `PRIVATE_IP` is set to your etcd client IP.

### Multi-node etcd cluster

For durability and high availability, run etcd as a multi-node cluster in
production and back it up periodically. A five-member cluster is recommended
in production. For more information, see
FAQ documentation.

As you're using Kubernetes, you have the option to run etcd as a container inside
one or more Pods. The `kubeadm` tool sets up etcd
static pods by default, or
you can deploy a
separate cluster
and instruct kubeadm to use that etcd cluster as the control plane's backing store.

You configure an etcd cluster either by static member information or by dynamic
discovery. For more information on clustering, see
etcd clustering documentation.

For an example, consider a five-member etcd cluster running with the following
client URLs: `http://$IP1:2379`, `http://$IP2:2379`, `http://$IP3:2379`,
`http://$IP4:2379`, and `http://$IP5:2379`. To start a Kubernetes API server:

1. Run the following:

   ```shell
   etcd --listen-client-urls=http://$IP1:2379,http://$IP2:2379,http://$IP3:2379,http://$IP4:2379,http://$IP5:2379 --advertise-client-urls=http://$IP1:2379,http://$IP2:2379,http://$IP3:2379,http://$IP4:2379,http://$IP5:2379
   ```

2. Start the Kubernetes API servers with the flag
   `--etcd-servers=$IP1:2379,$IP2:2379,$IP3:2379,$IP4:2379,$IP5:2379`.

   Make sure the `IP<n>` variables are set to your client IP addresses.

### Multi-node etcd cluster with load balancer

To run a load balancing etcd cluster:

1. Set up an etcd cluster.
2. Configure a load balancer in front of the etcd cluster.
   For example, let the address of the load balancer be `$LB`.
3. Start Kubernetes API Servers with the flag `--etcd-servers=$LB:2379`.
