---
id: okf-structure/concepts/security/api-server-bypass-risks.md#container-runtime-socket-runtime-socket
kind: section
title: Container runtime socket {#runtime-socket}
source: concepts/security/api-server-bypass-risks.md
url: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/
heading: Container runtime socket {#runtime-socket}
parent: okf-structure/concepts/security/api-server-bypass-risks
children: []
prev_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#the-etcd-api
next_sibling: null
word_count: 198
---

On each node in a Kubernetes cluster, access to interact with containers is controlled
by the container runtime (or runtimes, if you have configured more than one). Typically,
the container runtime exposes a Unix socket that the kubelet can access. An attacker with
access to this socket can launch new containers or interact with running containers.

At the cluster level, the impact of this access depends on whether the containers that
run on the compromised node have access to Secrets or other confidential
data that an attacker could use to escalate privileges to other worker nodes or to
control plane components.

### Mitigations {#runtime-socket-mitigations}

- Ensure that you tightly control filesystem access to container runtime sockets.
  When possible, restrict this access to the `root` user.
- Isolate the kubelet from other components running on the node, using
  mechanisms such as Linux kernel namespaces.
- Ensure that you restrict or forbid the use of `hostPath` mounts
  that include the container runtime socket, either directly or by mounting a parent
  directory. Also `hostPath` mounts must be set as read-only to mitigate risks
  of attackers bypassing directory restrictions.
- Restrict user access to nodes, and especially restrict superuser access to nodes.
