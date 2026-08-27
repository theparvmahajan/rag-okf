---
id: okf-structure/tasks/administer-cluster/sysctl-cluster.md#setting-sysctls-for-a-pod
kind: section
title: Setting Sysctls for a Pod
source: tasks/administer-cluster/sysctl-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/
heading: Setting Sysctls for a Pod
parent: okf-structure/tasks/administer-cluster/sysctl-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/sysctl-cluster.md#safe-and-unsafe-sysctls
next_sibling: null
word_count: 339
---

A number of sysctls are _namespaced_ in today's Linux kernels. This means that
they can be set independently for each pod on a node. Only namespaced sysctls
are configurable via the pod securityContext within Kubernetes.

The following sysctls are known to be namespaced. This list could change
in future versions of the Linux kernel.

- `kernel.shm*`,
- `kernel.msg*`,
- `kernel.sem`,
- `fs.mqueue.*`,
- Those `net.*` that can be set in container networking namespace. However,
  there are exceptions (e.g., `net.netfilter.nf_conntrack_max` and
  `net.netfilter.nf_conntrack_expect_max` can be set in container networking
  namespace but are unnamespaced before Linux 5.12.2).

Sysctls with no namespace are called _node-level_ sysctls. If you need to set
them, you must manually configure them on each node's operating system, or by
using a DaemonSet with privileged containers.

Use the pod securityContext to configure namespaced sysctls. The securityContext
applies to all containers in the same pod.

This example uses the pod securityContext to set a safe sysctl
`kernel.shm_rmid_forced` and two unsafe sysctls `net.core.somaxconn` and
`kernel.msgmax`. There is no distinction between _safe_ and _unsafe_ sysctls in
the specification.

Only modify sysctl parameters after you understand their effects, to avoid
destabilizing your operating system.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sysctl-example
spec:
  securityContext:
    sysctls:
    - name: kernel.shm_rmid_forced
      value: "0"
    - name: net.core.somaxconn
      value: "1024"
    - name: kernel.msgmax
      value: "65536"
  ...
```

Due to their nature of being _unsafe_, the use of _unsafe_ sysctls
is at-your-own-risk and can lead to severe problems like wrong behavior of
containers, resource shortage or complete breakage of a node.

It is good practice to consider nodes with special sysctl settings as
_tainted_ within a cluster, and only schedule pods onto them which need those
sysctl settings. It is suggested to use the Kubernetes _taints and toleration_
feature to implement this.

A pod with the _unsafe_ sysctls will fail to launch on any node which has not
enabled those two _unsafe_ sysctls explicitly. As with _node-level_ sysctls it
is recommended to use
_taints and toleration_ feature or
taints on nodes
to schedule those pods onto the right nodes.
