---
id: okf-structure/tutorials/cluster-management/admission-policies.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: Prerequisites
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#introduction
next_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#what-are-declarative-admission-policies
word_count: 69
---

To define admission policies, you must be a cluster administrator. Make sure you have administrator
access to the cluster where you are learning.

For ValidatingAdmissionPolicy, you need:
* A cluster running version 1.30 or later.

For MutatingAdmissionPolicy, you need:
* A cluster running version 1.36 or later.

To check the version, run `kubectl version`.
If you are running an older version of Kubernetes, check the documentation for that version.
