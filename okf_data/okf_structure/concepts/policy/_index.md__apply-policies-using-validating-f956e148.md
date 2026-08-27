---
id: okf-structure/concepts/policy/_index.md#apply-policies-using-validatingadmissionpolicy
kind: section
title: Apply policies using ValidatingAdmissionPolicy
source: concepts/policy/_index.md
url: https://kubernetes.io/docs/concepts/policy/
heading: Apply policies using ValidatingAdmissionPolicy
parent: okf-structure/concepts/policy/_index
children: []
prev_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-admission-controllers
next_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-dynamic-admission-control
word_count: 72
---

Validating admission policies allow configurable validation checks to be executed in the API server using the Common Expression Language (CEL). For example, a `ValidatingAdmissionPolicy` can be used to disallow use of the `latest` image tag.

A `ValidatingAdmissionPolicy` operates on an API request and can be used to block, audit, and warn users about non-compliant configurations.

Details on the `ValidatingAdmissionPolicy` API, with examples, are documented in a dedicated section:
* Validating Admission Policy
