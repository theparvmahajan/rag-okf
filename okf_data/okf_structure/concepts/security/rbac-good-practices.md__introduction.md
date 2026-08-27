---
id: okf-structure/concepts/security/rbac-good-practices.md#introduction
kind: section
title: Role Based Access Control Good Practices
source: concepts/security/rbac-good-practices.md
url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
heading: null
parent: okf-structure/concepts/security/rbac-good-practices
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/rbac-good-practices.md#general-good-practice
word_count: 75
---

Kubernetes RBAC is a key security control
to ensure that cluster users and workloads have only the access to resources required to
execute their roles. It is important to ensure that, when designing permissions for cluster
users, the cluster administrator understands the areas where privilege escalation could occur,
to reduce the risk of excessive access leading to security incidents.

The good practices laid out here should be read in conjunction with the general
RBAC documentation.
