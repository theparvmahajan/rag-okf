---
id: okf-structure/concepts/security/cloud-native-security.md#develop-lifecycle-phase-lifecycle-phase-develop
kind: section
title: _Develop_ lifecycle phase {#lifecycle-phase-develop}
source: concepts/security/cloud-native-security.md
url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
heading: _Develop_ lifecycle phase {#lifecycle-phase-develop}
parent: okf-structure/concepts/security/cloud-native-security
children: []
prev_sibling: okf-structure/concepts/security/cloud-native-security.md#cloud-native-information-security
next_sibling: okf-structure/concepts/security/cloud-native-security.md#distribute-lifecycle-phase-lifecycle-phase-distribute
word_count: 103
---

- Ensure the integrity of development environments.
- Design applications following good practices for information security,
  appropriate for your context.
- Consider end user security as part of solution design.

To achieve this, you can:

1. Adopt an architecture, such as zero trust,
   that minimizes attack surfaces, even for internal threats.
1. Define a code review process that considers security concerns.
1. Build a _threat model_ of your system or application that identifies
   trust boundaries. Use that threat model to identify risks and determine
   how to treat them.
1. Incorporate advanced security automation, such as _fuzzing_ and
   security chaos engineering,
   where it's justified.
