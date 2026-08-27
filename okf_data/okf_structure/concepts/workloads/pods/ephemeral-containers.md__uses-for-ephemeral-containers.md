---
id: okf-structure/concepts/workloads/pods/ephemeral-containers.md#uses-for-ephemeral-containers
kind: section
title: Uses for ephemeral containers
source: concepts/workloads/pods/ephemeral-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
heading: Uses for ephemeral containers
parent: okf-structure/concepts/workloads/pods/ephemeral-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/ephemeral-containers.md#understanding-ephemeral-containers
next_sibling: okf-structure/concepts/workloads/pods/ephemeral-containers.md#whatsnext
word_count: 87
---

Ephemeral containers are useful for interactive troubleshooting when `kubectl
exec` is insufficient because a container has crashed or a container image
doesn't include debugging utilities.

In particular, distroless images
enable you to deploy minimal container images that reduce attack surface
and exposure to bugs and vulnerabilities. Since distroless images do not include a
shell or any debugging utilities, it's difficult to troubleshoot distroless
images using `kubectl exec` alone.

When using ephemeral containers, it's helpful to enable process namespace
sharing so
you can view processes in other containers.
