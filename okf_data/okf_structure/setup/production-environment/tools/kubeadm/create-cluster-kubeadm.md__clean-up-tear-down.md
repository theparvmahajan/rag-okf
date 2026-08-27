---
id: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#clean-up-tear-down
kind: section
title: Clean up {#tear-down}
source: setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
heading: Clean up {#tear-down}
parent: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#instructions
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#version-skew-policy-version-skew-policy
word_count: 224
---

If you used disposable servers for your cluster, for testing, you can
switch those off and do no further clean up. You can use
`kubectl config delete-cluster` to delete your local references to the
cluster.

However, if you want to deprovision your cluster more cleanly, you should
first drain the node
and make sure that the node is empty, then deconfigure the node.

### Remove the node

Talking to the control-plane node with the appropriate credentials, run:

```bash
kubectl drain <node name> --delete-emptydir-data --force --ignore-daemonsets
```

Before removing the node, reset the state installed by `kubeadm`:

```bash
kubeadm reset
```

The reset process does not reset or clean up iptables rules or IPVS tables.
If you wish to reset iptables, you must do so manually:

```bash
iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X
```

If you want to reset the IPVS tables, you must run the following command:

```bash
ipvsadm -C
```

Now remove the node:

```bash
kubectl delete node <node name>
```

If you wish to start over, run `kubeadm init` or `kubeadm join` with the
appropriate arguments.

### Clean up the control plane

You can use `kubeadm reset` on the control plane host to trigger a best-effort
clean up.

See the `kubeadm reset`
reference documentation for more information about this subcommand and its
options.
