---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#0-decide-whether-pod-security-admission-is-right-for-you-is-psa-right-for-you
kind: section
title: 0. Decide whether Pod Security Admission is right for you {#is-psa-right-for-you}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 0. Decide whether Pod Security Admission is right for you {#is-psa-right-for-you}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#overall-approach
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#1-review-namespace-permissions-review-namespace-permissions
word_count: 259
---

Pod Security Admission was designed to meet the most common security needs out of the box, and to
provide a standard set of security levels across clusters. However, it is less flexible than
PodSecurityPolicy. Notably, the following features are supported by PodSecurityPolicy but not Pod
Security Admission:

- **Setting default security constraints** - Pod Security Admission is a non-mutating admission
  controller, meaning it won't modify pods before validating them. If you were relying on this
  aspect of PSP, you will need to either modify your workloads to meet the Pod Security constraints,
  or use a Mutating Admission Webhook
  to make those changes. See Simplify & Standardize PodSecurityPolicies below for more detail.
- **Fine-grained control over policy definition** - Pod Security Admission only supports
  3 standard levels.
  If you require more control over specific constraints, then you will need to use a
  Validating Admission Webhook
  to enforce those policies.
- **Sub-namespace policy granularity** - PodSecurityPolicy lets you bind different policies to
  different Service Accounts or users, even within a single namespace. This approach has many
  pitfalls and is not recommended, but if you require this feature anyway you will
  need to use a 3rd party webhook instead. The exception to this is if you only need to completely exempt
  specific users or RuntimeClasses, in which case Pod
  Security Admission does expose some
  static configuration for exemptions.

Even if Pod Security Admission does not meet all of your needs it was designed to be _complementary_
to other policy enforcement mechanisms, and can provide a useful fallback running alongside other
admission webhooks.
