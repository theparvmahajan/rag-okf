---
id: okf-structure/concepts/policy/_index.md#apply-policies-using-admission-controllers
kind: section
title: Apply policies using admission controllers
source: concepts/policy/_index.md
url: https://kubernetes.io/docs/concepts/policy/
heading: Apply policies using admission controllers
parent: okf-structure/concepts/policy/_index
children: []
prev_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-api-objects
next_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-validatingadmissionpolicy
word_count: 76
---

An admission controller
runs in the API server
and can validate or mutate API requests. Some admission controllers act to apply policies.
For example, the AlwaysPullImages admission controller modifies a new Pod to set the image pull policy to `Always`.

Kubernetes has several built-in admission controllers that are configurable via the API server `--enable-admission-plugins` flag.

Details on admission controllers, with the complete list of available admission controllers, are documented in a dedicated section:

* Admission Controllers
