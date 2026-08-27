---
id: okf-structure/concepts/security/pod-security-standards.md#policy-instantiation
kind: section
title: Policy Instantiation
source: concepts/security/pod-security-standards.md
url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
heading: Policy Instantiation
parent: okf-structure/concepts/security/pod-security-standards
children: []
prev_sibling: okf-structure/concepts/security/pod-security-standards.md#profile-details
next_sibling: okf-structure/concepts/security/pod-security-standards.md#pod-os-field
word_count: 83
---

Decoupling policy definition from policy instantiation allows for a common understanding and
consistent language of policies across clusters, independent of the underlying enforcement
mechanism.

As mechanisms mature, they will be defined below on a per-policy basis. The methods of enforcement
of individual policies are not defined here.

**Pod Security Admission Controller**

- Privileged namespace
- Baseline namespace
- Restricted namespace

### Alternatives

Other alternatives for enforcing policies are being developed in the Kubernetes ecosystem, such as:

- Kubewarden
- Kyverno
- OPA Gatekeeper
