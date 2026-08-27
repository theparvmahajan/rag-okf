---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp
kind: hub
title: Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: null
parent: okf-structure/tasks/configure-pod-container
children:
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#introduction
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#prerequisites
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#overall-approach
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#0-decide-whether-pod-security-admission-is-right-for-you-is-psa-right-for-you
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#1-review-namespace-permissions-review-namespace-permissions
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#2-simplify-standardize-podsecuritypolicies-simplify-psps
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#3-update-namespaces-update-namespaces
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#4-review-namespace-creation-processes-review-namespace-creation-process
- okf-structure/tasks/configure-pod-container/migrate-from-psp.md#5-disable-podsecuritypolicy-disable-psp
prev_sibling: okf-structure/tasks/configure-pod-container/image-volumes
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry
word_count: 2316
---


