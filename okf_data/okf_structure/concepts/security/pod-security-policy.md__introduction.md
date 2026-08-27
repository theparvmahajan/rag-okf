---
id: okf-structure/concepts/security/pod-security-policy.md#introduction
kind: section
title: Pod Security Policies
source: concepts/security/pod-security-policy.md
url: https://kubernetes.io/docs/concepts/security/pod-security-policy/
heading: null
parent: okf-structure/concepts/security/pod-security-policy
children: []
prev_sibling: null
next_sibling: null
word_count: 88
---

PodSecurityPolicy was deprecated
in Kubernetes v1.21, and removed from Kubernetes in v1.25.

Instead of using PodSecurityPolicy, you can enforce similar restrictions on Pods using
either or both:

- Pod Security Admission
- a 3rd party admission plugin, that you deploy and configure yourself

For a migration guide, see Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller.
For more information on the removal of this API,
see PodSecurityPolicy Deprecation: Past, Present, and Future.

If you are not running Kubernetes v, check the documentation for
your version of Kubernetes.
