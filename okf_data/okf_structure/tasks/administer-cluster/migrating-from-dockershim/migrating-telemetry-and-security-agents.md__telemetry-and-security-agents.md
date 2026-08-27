---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#telemetry-and-security-agents
kind: section
title: Telemetry and security agents
source: tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/
heading: Telemetry and security agents
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents.md#migration-from-dockershim
word_count: 483
---

Within a Kubernetes cluster there are a few different ways to run telemetry or
security agents.  Some agents have a direct dependency on Docker Engine when
they run as DaemonSets or directly on nodes.

### Why do some telemetry agents communicate with Docker Engine?

Historically, Kubernetes was written to work specifically with Docker Engine.
Kubernetes took care of networking and scheduling, relying on Docker Engine for
launching and running containers (within Pods) on a node. Some information that
is relevant to telemetry, such as a pod name, is only available from Kubernetes
components. Other data, such as container metrics, is not the responsibility of
the container runtime. Early telemetry agents needed to query the container
runtime *and* Kubernetes to report an accurate picture. Over time, Kubernetes
gained the ability to support multiple runtimes, and now supports any runtime
that is compatible with the container runtime interface.

Some telemetry agents rely specifically on Docker Engine tooling. For example, an agent
might run a command such as
`docker ps`
or `docker top` to list
containers and processes or `docker logs`
to receive streamed logs. If nodes in your existing cluster use
Docker Engine, and you switch to a different container runtime,
these commands will not work any longer.

### Identify DaemonSets that depend on Docker Engine {#identify-docker-dependency}

If a pod wants to make calls to the `dockerd` running on the node, the pod must either:

- mount the filesystem containing the Docker daemon's privileged socket, as a
  volume; or
- mount the specific path of the Docker daemon's privileged socket directly, also as a volume.

For example: on COS images, Docker exposes its Unix domain socket at
`/var/run/docker.sock` This means that the pod spec will include a
`hostPath` volume mount of `/var/run/docker.sock`.

Here's a sample shell script to find Pods that have a mount directly mapping the
Docker socket. This script outputs the namespace and name of the pod. You can
remove the `grep '/var/run/docker.sock'` to review other mounts.

```bash
kubectl get pods --all-namespaces \
-o=jsonpath='{range .items[*]}{"\n"}{.metadata.namespace}{":\t"}{.metadata.name}{":\t"}{range .spec.volumes[*]}{.hostPath.path}{", "}{end}{end}' \
| sort \
| grep '/var/run/docker.sock'
```

There are alternative ways for a pod to access Docker on the host. For instance, the parent
directory `/var/run` may be mounted instead of the full path (like in this
example).
The script above only detects the most common uses.

### Detecting Docker dependency from node agents

If your cluster nodes are customized and install additional security and
telemetry agents on the node, check with the agent vendor
to verify whether it has any dependency on Docker.

### Telemetry and security agent vendors

This section is intended to aggregate information about various telemetry and
security agents that may have a dependency on container runtimes.

We keep the work in progress version of migration instructions for various telemetry and security agent vendors
in Google doc.
Please contact the vendor to get up to date instructions for migrating from dockershim.
