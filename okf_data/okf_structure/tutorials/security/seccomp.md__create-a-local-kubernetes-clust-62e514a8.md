---
id: okf-structure/tutorials/security/seccomp.md#create-a-local-kubernetes-cluster-with-kind
kind: section
title: Create a local Kubernetes cluster with kind
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Create a local Kubernetes cluster with kind
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#download-example-seccomp-profiles-download-profiles
next_sibling: okf-structure/tutorials/security/seccomp.md#create-a-pod-that-uses-the-container-runtime-default-seccomp-profile
word_count: 297
---

For simplicity, kind can be used to create a single
node cluster with the seccomp profiles loaded. Kind runs Kubernetes in Docker,
so each node of the cluster is a container. This allows for files
to be mounted in the filesystem of each container similar to loading files
onto a node.

Download that example kind configuration, and save it to a file named `kind.yaml`:
```shell
curl -L -O https://k8s.io/examples/pods/security/seccomp/kind.yaml
```

You can set a specific Kubernetes version by setting the node's container image.
See Nodes within the
kind documentation about configuration for more details on this.
This tutorial assumes you are using Kubernetes .

As a beta feature, you can configure Kubernetes to use the profile that the
container runtime
prefers by default, rather than falling back to `Unconfined`.
If you want to try that, see
enable the use of `RuntimeDefault` as the default seccomp profile for all workloads
before you continue.

Once you have a kind configuration in place, create the kind cluster with
that configuration:

```shell
kind create cluster --config=kind.yaml
```

After the new Kubernetes cluster is ready, identify the Docker container running
as the single node cluster:

```shell
docker ps
```

You should see output indicating that a container is running with name
`kind-control-plane`. The output is similar to:

```
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                       NAMES
6a96207fed4b        kindest/node:v1.18.2   "/usr/local/bin/entr…"   27 seconds ago      Up 24 seconds       127.0.0.1:42223->6443/tcp   kind-control-plane
```

If observing the filesystem of that container, you should see that the
`profiles/` directory has been successfully loaded into the default seccomp path
of the kubelet. Use `docker exec` to run a command in the Pod:

```shell
docker exec -it kind-control-plane ls /var/lib/kubelet/seccomp/profiles
```

```
audit.json  fine-grained.json  violation.json
```

You have verified that these seccomp profiles are available to the kubelet
running within kind.
