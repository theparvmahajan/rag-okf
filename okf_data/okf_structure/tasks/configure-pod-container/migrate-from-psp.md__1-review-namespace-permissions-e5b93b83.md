---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#1-review-namespace-permissions-review-namespace-permissions
kind: section
title: 1. Review namespace permissions {#review-namespace-permissions}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 1. Review namespace permissions {#review-namespace-permissions}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#0-decide-whether-pod-security-admission-is-right-for-you-is-psa-right-for-you
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#2-simplify-standardize-podsecuritypolicies-simplify-psps
word_count: 94
---

Pod Security Admission is controlled by labels on
namespaces.
This means that anyone who can update (or patch or create) a namespace can also modify the Pod
Security level for that namespace, which could be used to bypass a more restrictive policy. Before
proceeding, ensure that only trusted, privileged users have these namespace permissions. It is not
recommended to grant these powerful permissions to users that shouldn't have elevated permissions,
but if you must you will need to use an
admission webhook
to place additional restrictions on setting Pod Security labels on Namespace objects.
