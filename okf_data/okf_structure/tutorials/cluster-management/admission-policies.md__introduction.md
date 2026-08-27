---
id: okf-structure/tutorials/cluster-management/admission-policies.md#introduction
kind: section
title: Explore Validating and Mutating Admission Policies
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: null
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#prerequisites
word_count: 43
---

This page lets you try out declarative _admission policies_, which allow you to use the Common
Expression Language (CEL) to validate or mutate resources.

Kubernetes  supports two kinds of admission policy:

- ValidatingAdmissionPolicy
- MutatingAdmissionPolicy

This tutorial covers both kinds of admission policy.
