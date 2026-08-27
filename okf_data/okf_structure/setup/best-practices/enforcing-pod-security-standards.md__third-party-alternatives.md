---
id: okf-structure/setup/best-practices/enforcing-pod-security-standards.md#third-party-alternatives
kind: section
title: Third-party alternatives
source: setup/best-practices/enforcing-pod-security-standards.md
url: https://kubernetes.io/docs/setup/best-practices/enforcing-pod-security-standards/
heading: Third-party alternatives
parent: okf-structure/setup/best-practices/enforcing-pod-security-standards
children: []
prev_sibling: okf-structure/setup/best-practices/enforcing-pod-security-standards.md#using-the-built-in-pod-security-admission-controller
next_sibling: null
word_count: 67
---

Other alternatives for enforcing security profiles are being developed in the Kubernetes
ecosystem:

- Kubewarden.
- Kyverno.
- OPA Gatekeeper.

The decision to go with a _built-in_ solution (e.g. PodSecurity admission controller) versus a
third-party tool is entirely dependent on your own situation. When evaluating any solution,
trust of your supply chain is crucial. Ultimately, using _any_ of the aforementioned approaches
will be better than doing nothing.
