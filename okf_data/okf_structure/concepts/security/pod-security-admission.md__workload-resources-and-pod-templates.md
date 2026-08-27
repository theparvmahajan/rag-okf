---
id: okf-structure/concepts/security/pod-security-admission.md#workload-resources-and-pod-templates
kind: section
title: Workload resources and Pod templates
source: concepts/security/pod-security-admission.md
url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
heading: Workload resources and Pod templates
parent: okf-structure/concepts/security/pod-security-admission
children: []
prev_sibling: okf-structure/concepts/security/pod-security-admission.md#pod-security-admission-labels-for-namespaces
next_sibling: okf-structure/concepts/security/pod-security-admission.md#exemptions
word_count: 68
---

Pods are often created indirectly, by creating a workload
object such as a deployment or job. The workload object defines a
_Pod template_ and a controller for the
workload resource creates Pods based on that template. To help catch violations early, both the
audit and warning modes are applied to the workload resources. However, enforce mode is **not**
applied to workload resources, only to the resulting pod objects.
