---
id: okf-structure/concepts/policy/_index.md#apply-policies-using-dynamic-admission-control
kind: section
title: Apply policies using dynamic admission control
source: concepts/policy/_index.md
url: https://kubernetes.io/docs/concepts/policy/
heading: Apply policies using dynamic admission control
parent: okf-structure/concepts/policy/_index
children: []
prev_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-validatingadmissionpolicy
next_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-kubelet-configurations
word_count: 130
---

Dynamic admission controllers (or admission webhooks) run outside the API server as separate applications that register to receive webhooks requests to perform validation or mutation of API requests. 

Dynamic admission controllers can be used to apply policies on API requests and trigger other policy-based workflows. A dynamic admission controller can perform complex checks including those that require retrieval of other cluster resources and external data. For example, an image verification check can lookup data from OCI registries to validate the container image signatures and attestations.

Details on dynamic admission control are documented in a dedicated section:
* Dynamic Admission Control

### Implementations {#implementations-admission-control}

Dynamic Admission Controllers that act as flexible policy engines are being developed in the Kubernetes ecosystem, such as:
- Kubewarden
- Kyverno
- OPA Gatekeeper
- Polaris
