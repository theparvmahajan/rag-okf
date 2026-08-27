---
id: okf-structure/concepts/security/application-security-checklist.md#introduction
kind: section
title: Application Security Checklist
source: concepts/security/application-security-checklist.md
url: https://kubernetes.io/docs/concepts/security/application-security-checklist/
heading: null
parent: okf-structure/concepts/security/application-security-checklist
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/application-security-checklist.md#base-security-hardening
word_count: 159
---

This checklist aims to provide basic guidelines on securing applications
running in Kubernetes from a developer's perspective.
This list is not meant to be exhaustive and is intended to evolve over time.

On how to read and use this document:

- The order of topics does not reflect an order of priority.
- Some checklist items are detailed in the paragraph below the list of each section.
- This checklist assumes that a `developer` is a Kubernetes cluster user who
  interacts with namespaced scope objects.

Checklists are **not** sufficient for attaining a good security posture on their own.
A good security posture requires constant attention and improvement, but a checklist
can be the first step on the never-ending journey towards security preparedness.
Some recommendations in this checklist may be too restrictive or too lax for
your specific security needs. Since Kubernetes security is not "one size fits all",
each category of checklist items should be evaluated on its merits.
