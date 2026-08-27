---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#integration-with-pod-security-admission-checks
kind: section
title: Integration with Pod security admission checks
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Integration with Pod security admission checks
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#id-count-for-each-of-pods
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#limitations
word_count: 157
---

For Linux Pods that enable user namespaces, Kubernetes relaxes the application of
Pod Security Standards in a controlled way.

If you create a Pod that uses user
namespaces, the following fields won't be constrained even in contexts that enforce the
_Baseline_ or _Restricted_ pod security standard. This behavior does not
present a security concern because `root` inside a Pod with user namespaces
actually refers to the user inside the container, that is never mapped to a
privileged user on the host. Here's the list of fields that are **not** checked for Pods in those
circumstances:

- `spec.securityContext.runAsNonRoot`
- `spec.containers[*].securityContext.runAsNonRoot`
- `spec.initContainers[*].securityContext.runAsNonRoot`
- `spec.ephemeralContainers[*].securityContext.runAsNonRoot`
- `spec.securityContext.runAsUser`
- `spec.containers[*].securityContext.runAsUser`
- `spec.initContainers[*].securityContext.runAsUser`
- `spec.ephemeralContainers[*].securityContext.runAsUser`

Further, if the pod is in a context with the _Baseline_ pod security standard,
validation for the following fields will similarly be relaxed:

- `spec.containers[*].securityContext.procMount`
- `spec.initContainers[*].securityContext.procMount`
- `spec.ephemeralContainers[*].securityContext.procMount`

with the _Restricted_ pod security standard, a pod still must only use the
default or empty ProcMount.
