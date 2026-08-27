---
id: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#prerequisites
kind: section
title: Prerequisites
source: setup/production-environment/tools/kubeadm/high-availability.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
heading: Prerequisites
parent: okf-structure/setup/production-environment/tools/kubeadm/high-availability
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#first-steps-for-both-methods
word_count: 441
---

The prerequisites depend on which topology you have selected for your cluster's
control plane:

You need:

- Three or more machines that meet kubeadm's minimum requirements for
  the control-plane nodes. Having an odd number of control plane nodes can help
  with leader selection in the case of machine or zone failure.
  - including a container runtime, already set up and working
- Three or more machines that meet kubeadm's minimum
  requirements for the workers
  - including a container runtime, already set up and working
- Full network connectivity between all machines in the cluster (public or
  private network)
- Superuser privileges on all machines using `sudo`
  - You can use a different tool; this guide uses `sudo` in the examples.
- SSH access from one device to all nodes in the system
- `kubeadm` and `kubelet` already installed on all machines.

_See Stacked etcd topology for context._

You need:

- Three or more machines that meet kubeadm's minimum requirements for
  the control-plane nodes. Having an odd number of control plane nodes can help
  with leader selection in the case of machine or zone failure.
  - including a container runtime, already set up and working
- Three or more machines that meet kubeadm's minimum
  requirements for the workers
  - including a container runtime, already set up and working
- Full network connectivity between all machines in the cluster (public or
  private network)
- Superuser privileges on all machines using `sudo`
  - You can use a different tool; this guide uses `sudo` in the examples.
- SSH access from one device to all nodes in the system
- `kubeadm` and `kubelet` already installed on all machines.

And you also need:

- Three or more additional machines, that will become etcd cluster members.
  Having an odd number of members in the etcd cluster is a requirement for achieving
  optimal voting quorum.
  - These machines again need to have `kubeadm` and `kubelet` installed.
  - These machines also require a container runtime, that is already set up and working.

_See External etcd topology for context._

### Container images

Each host should have access read and fetch images from the Kubernetes container image registry,
`registry.k8s.io`. If you want to deploy a highly-available cluster where the hosts do not have
access to pull images, this is possible. You must ensure by some other means that the correct
container images are already available on the relevant hosts.

### Command line interface {#kubectl}

To manage Kubernetes once your cluster is set up, you should
install kubectl on your PC. It is also useful
to install the `kubectl` tool on each control plane node, as this can be
helpful for troubleshooting.
