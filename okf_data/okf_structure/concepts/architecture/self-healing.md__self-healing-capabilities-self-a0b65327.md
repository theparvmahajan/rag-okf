---
id: okf-structure/concepts/architecture/self-healing.md#self-healing-capabilities-self-healing-capabilities
kind: section
title: Self-Healing capabilities {#self-healing-capabilities}
source: concepts/architecture/self-healing.md
url: https://kubernetes.io/docs/concepts/architecture/self-healing/
heading: Self-Healing capabilities {#self-healing-capabilities}
parent: okf-structure/concepts/architecture/self-healing
children: []
prev_sibling: okf-structure/concepts/architecture/self-healing.md#introduction
next_sibling: okf-structure/concepts/architecture/self-healing.md#considerations-considerations
word_count: 174
---

- **Container-level restarts:** If a container inside a Pod fails, Kubernetes restarts it based on the `restartPolicy`.

- **Replica replacement:** If a Pod in a Deployment or StatefulSet fails, Kubernetes creates a replacement Pod to maintain the specified number of replicas.
  If a Pod that is part of a DaemonSet fails, the control plane
  creates a replacement Pod to run on the same node.
  
- **Persistent storage recovery:** If a node is running a Pod with a PersistentVolume (PV) attached, and the node fails, Kubernetes can reattach the volume to a new Pod on a different node.

- **Load balancing for Services:** If a Pod behind a Service fails, Kubernetes automatically removes it from the Service's endpoints to route traffic only to healthy Pods.

Here are some of the key components that provide Kubernetes self-healing:

- **kubelet:** Ensures that containers are running, and restarts those that fail.

- **Deployment (via ReplicaSet), ReplicaSet, StatefulSet and DaemonSet controllers:** Maintain the desired number of Pod replicas.

- **PersistentVolume controller:** Manages volume attachment and detachment for stateful workloads.
