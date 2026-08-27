---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#introduction
kind: section
title: Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: null
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#prerequisites
word_count: 39
---

This page describes the process of migrating from PodSecurityPolicies to the built-in PodSecurity
admission controller. This can be done effectively using a combination of dry-run and `audit` and
`warn` modes, although this becomes harder if mutating PSPs are used.
