---
id: okf-structure/tutorials/configuration/pod-sidecar-containers.md#benefits-of-a-built-in-sidecar-container
kind: section
title: Benefits of a built-in sidecar container
source: tutorials/configuration/pod-sidecar-containers.md
url: https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/
heading: Benefits of a built-in sidecar container
parent: okf-structure/tutorials/configuration/pod-sidecar-containers
children: []
prev_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#sidecar-containers-overview
next_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#adopting-built-in-sidecar-containers
word_count: 138
---

Using Kubernetes' native support for sidecar containers provides several benefits:

1. You can configure a native sidecar container to start ahead of
   init containers.
1. The built-in sidecar containers can be authored to guarantee that they are terminated last.
   Sidecar containers are terminated with a `SIGTERM` signal once all the regular containers
   are completed and terminated. If the sidecar container isn’t gracefully shut down, a
   `SIGKILL` signal will be used to terminate it.
1. With Jobs, when Pod's `restartPolicy: OnFailure` or `restartPolicy: Never`,
   native sidecar containers do not block Pod completion. With legacy sidecar containers,
   special care is needed to handle this situation.
1. Also, with Jobs, built-in sidecar containers would keep being restarted once they are done,
   even if regular containers would not with Pod's `restartPolicy: Never`.

See differences from init containers
to learn more about it.
