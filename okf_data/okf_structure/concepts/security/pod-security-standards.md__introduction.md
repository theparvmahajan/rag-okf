---
id: okf-structure/concepts/security/pod-security-standards.md#introduction
kind: section
title: Pod Security Standards
source: concepts/security/pod-security-standards.md
url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
heading: null
parent: okf-structure/concepts/security/pod-security-standards
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/pod-security-standards.md#profile-details
word_count: 94
---

The Pod Security Standards define three different _policies_ to broadly cover the security
spectrum. These policies are _cumulative_ and range from highly-permissive to highly-restrictive.
This guide outlines the requirements of each policy.

| Profile | Description |
| ------ | ----------- |
| Privileged | Unrestricted policy, providing the widest possible level of permissions. This policy allows for known privilege escalations. |
| Baseline | Minimally restrictive policy which prevents known privilege escalations. Allows the default (minimally specified) Pod configuration. |
| Restricted | Heavily restricted policy, following current Pod hardening best practices. |
