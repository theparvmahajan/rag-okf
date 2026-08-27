---
id: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#first-steps-for-both-methods
kind: section
title: First steps for both methods
source: setup/production-environment/tools/kubeadm/high-availability.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
heading: First steps for both methods
parent: okf-structure/setup/production-environment/tools/kubeadm/high-availability
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#prerequisites
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#stacked-control-plane-and-etcd-nodes
word_count: 244
---

### Create load balancer for kube-apiserver

There are many configurations for load balancers. The following example is only one
option. Your cluster requirements may need a different configuration.

1. Create a kube-apiserver load balancer with a name that resolves to DNS.

   - In a cloud environment you should place your control plane nodes behind a TCP
     forwarding load balancer. This load balancer distributes traffic to all
     healthy control plane nodes in its target list. The health check for
     an apiserver is a TCP check on the port the kube-apiserver listens on
     (default value `:6443`).

   - It is not recommended to use an IP address directly in a cloud environment.

   - The load balancer must be able to communicate with all control plane nodes
     on the apiserver port. It must also allow incoming traffic on its
     listening port.

   - Make sure the address of the load balancer always matches
     the address of kubeadm's `ControlPlaneEndpoint`.

   - Read the Options for Software Load Balancing
     guide for more details.

1. Add the first control plane node to the load balancer, and test the
   connection:

   ```shell
   nc -zv -w 2 <LOAD_BALANCER_IP> <PORT>
   ```

   A connection refused error is expected because the API server is not yet
   running. A timeout, however, means the load balancer cannot communicate
   with the control plane node. If a timeout occurs, reconfigure the load
   balancer to communicate with the control plane node.

1. Add the remaining control plane nodes to the load balancer target group.
