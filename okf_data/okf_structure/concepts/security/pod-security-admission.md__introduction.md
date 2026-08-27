---
id: okf-structure/concepts/security/pod-security-admission.md#introduction
kind: section
title: Pod Security Admission
source: concepts/security/pod-security-admission.md
url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
heading: null
parent: okf-structure/concepts/security/pod-security-admission
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/pod-security-admission.md#pod-security-levels
word_count: 88
---

The Kubernetes Pod Security Standards define
different isolation levels for Pods. These standards let you define how you want to restrict the
behavior of pods in a clear, consistent fashion.

Kubernetes offers a built-in _Pod Security_ admission controller to enforce the Pod Security Standards. Pod security restrictions
are applied at the namespace level when pods are
created.

### Built-in Pod Security admission enforcement

This page is part of the documentation for Kubernetes v.
If you are running a different version of Kubernetes, consult the documentation for that release.
