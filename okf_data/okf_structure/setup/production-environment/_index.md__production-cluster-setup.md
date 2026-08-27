---
id: okf-structure/setup/production-environment/_index.md#production-cluster-setup
kind: section
title: Production cluster setup
source: setup/production-environment/_index.md
url: https://kubernetes.io/docs/setup/production-environment/
heading: Production cluster setup
parent: okf-structure/setup/production-environment/_index
children: []
prev_sibling: okf-structure/setup/production-environment/_index.md#production-considerations
next_sibling: okf-structure/setup/production-environment/_index.md#production-user-management
word_count: 985
---

In a production-quality Kubernetes cluster, the control plane manages the
cluster from services that can be spread across multiple computers
in different ways. Each worker node, however, represents a single entity that
is configured to run Kubernetes pods.

### Production control plane

The simplest Kubernetes cluster has the entire control plane and worker node
services running on the same machine. You can grow that environment by adding
worker nodes, as reflected in the diagram illustrated in
Kubernetes Components.
If the cluster is meant to be available for a short period of time, or can be
discarded if something goes seriously wrong, this might meet your needs.

If you need a more permanent, highly available cluster, however, you should
consider ways of extending the control plane. By design, one-machine control
plane services running on a single machine are not highly available.
If keeping the cluster up and running
and ensuring that it can be repaired if something goes wrong is important,
consider these steps:

- *Choose deployment tools*: You can deploy a control plane using tools such
  as kubeadm, kops, and kubespray. See
  Installing Kubernetes with deployment tools
  to learn tips for production-quality deployments using each of those deployment
  methods. Different Container Runtimes
  are available to use with your deployments.
- *Manage certificates*: Secure communications between control plane services
  are implemented using certificates. Certificates are automatically generated
  during deployment or you can generate them using your own certificate authority.
  See PKI certificates and requirements for details.
- *Configure load balancer for apiserver*: Configure a load balancer
  to distribute external API requests to the apiserver service instances running on different nodes. See 
  Create an External Load Balancer
  for details.
- *Separate and backup etcd service*: The etcd services can either run on the
  same machines as other control plane services or run on separate machines, for
  extra security and availability. Because etcd stores cluster configuration data,
  backing up the etcd database should be done regularly to ensure that you can
  repair that database if needed.
  See the etcd FAQ for details on configuring and using etcd.
  See Operating etcd clusters for Kubernetes
  and Set up a High Availability etcd cluster with kubeadm
  for details.
- *Create multiple control plane systems*: For high availability, the
  control plane should not be limited to a single machine. If the control plane
  services are run by an init service (such as systemd), each service should run on at
  least three machines. However, running control plane services as pods in
  Kubernetes ensures that the replicated number of services that you request
  will always be available.
  The scheduler should be fault tolerant,
  but not highly available. Some deployment tools set up Raft
  consensus algorithm to do leader election of Kubernetes services. If the
  primary goes away, another service elects itself and take over. 
- *Span multiple zones*: If keeping your cluster available at all times is
  critical, consider creating a cluster that runs across multiple data centers,
  referred to as zones in cloud environments. Groups of zones are referred to as regions.
  By spreading a cluster across
  multiple zones in the same region, it can improve the chances that your
  cluster will continue to function even if one zone becomes unavailable.
  See Running in multiple zones for details.
- *Manage on-going features*: If you plan to keep your cluster over time,
  there are tasks you need to do to maintain its health and security. For example,
  if you installed with kubeadm, there are instructions to help you with
  Certificate Management
  and Upgrading kubeadm clusters.
  See Administer a Cluster
  for a longer list of Kubernetes administrative tasks.

To learn about available options when you run control plane services, see
kube-apiserver,
kube-controller-manager,
and kube-scheduler
component pages. For highly available control plane examples, see
Options for Highly Available topology,
Creating Highly Available clusters with kubeadm,
and Operating etcd clusters for Kubernetes.
See Backing up an etcd cluster
for information on making an etcd backup plan.

### Production worker nodes

Production-quality workloads need to be resilient and anything they rely
on needs to be resilient (such as CoreDNS). Whether you manage your own
control plane or have a cloud provider do it for you, you still need to
consider how you want to manage your worker nodes (also referred to
simply as *nodes*).  

- *Configure nodes*: Nodes can be physical or virtual machines. If you want to
  create and manage your own nodes, you can install a supported operating system,
  then add and run the appropriate
  Node services. Consider:
  - The demands of your workloads when you set up nodes by having appropriate memory, CPU, and disk speed and storage capacity available.
  - Whether generic computer systems will do or you have workloads that need GPU processors, Windows nodes, or VM isolation.
- *Validate nodes*: See Valid node setup
  for information on how to ensure that a node meets the requirements to join
  a Kubernetes cluster.
- *Add nodes to the cluster*: If you are managing your own cluster you can
  add nodes by setting up your own machines and either adding them manually or
  having them register themselves to the cluster’s apiserver. See the
  Nodes section for information on how to set up Kubernetes to add nodes in these ways.
- *Scale nodes*: Have a plan for expanding the capacity your cluster will
  eventually need. See Considerations for large clusters
  to help determine how many nodes you need, based on the number of pods and
  containers you need to run. If you are managing nodes yourself, this can mean
  purchasing and installing your own physical equipment.
- *Autoscale nodes*: Read Node Autoscaling to learn about the
  tools available to automatically manage your nodes and the capacity they
  provide.
- *Set up node health checks*: For important workloads, you want to make sure
  that the nodes and pods running on those nodes are healthy. Using the
  Node Problem Detector
  daemon, you can ensure your nodes are healthy.
