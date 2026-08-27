---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#overall-approach
kind: section
title: Overall approach
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: Overall approach
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#0-decide-whether-pod-security-admission-is-right-for-you-is-psa-right-for-you
word_count: 96
---

There are multiple strategies you can take for migrating from PodSecurityPolicy to Pod Security
Admission. The following steps are one possible migration path, with a goal of minimizing both the
risks of a production outage and of a security gap.

0. Decide whether Pod Security Admission is the right fit for your use case.
1. Review namespace permissions
2. Simplify & standardize PodSecurityPolicies
3. Update namespaces
   1. Identify an appropriate Pod Security level
   2. Verify the Pod Security level
   3. Enforce the Pod Security level
   4. Bypass PodSecurityPolicy
4. Review namespace creation processes
5. Disable PodSecurityPolicy
