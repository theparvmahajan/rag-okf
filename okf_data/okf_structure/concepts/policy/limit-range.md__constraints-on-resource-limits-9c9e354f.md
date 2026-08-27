---
id: okf-structure/concepts/policy/limit-range.md#constraints-on-resource-limits-and-requests
kind: section
title: Constraints on resource limits and requests
source: concepts/policy/limit-range.md
url: https://kubernetes.io/docs/concepts/policy/limit-range/
heading: Constraints on resource limits and requests
parent: okf-structure/concepts/policy/limit-range
children: []
prev_sibling: okf-structure/concepts/policy/limit-range.md#introduction
next_sibling: okf-structure/concepts/policy/limit-range.md#limitrange-and-admission-checks-for-pods
word_count: 204
---

- The administrator creates a LimitRange in a namespace.
- Users create (or try to create) objects in that namespace, such as Pods or
  PersistentVolumeClaims.
- First, the LimitRange admission controller applies default request and limit values
  for all Pods (and their containers) that do not set compute resource requirements.
- Second, the LimitRange tracks usage to ensure it does not exceed resource minimum,
  maximum and ratio defined in any LimitRange present in the namespace.
- If you attempt to create or update an object (Pod or PersistentVolumeClaim) that violates
  a LimitRange constraint, your request to the API server will fail with an HTTP status
  code `403 Forbidden` and a message explaining the constraint that has been violated.
- If you add a LimitRange in a namespace that applies to compute-related resources
  such as `cpu` and `memory`, you must specify requests or limits for those values.
  Otherwise, the system may reject Pod creation.
- LimitRange validations occur only at Pod admission stage, not on running Pods.
  If you add or modify a LimitRange, the Pods that already exist in that namespace
  continue unchanged.
- If two or more LimitRange objects exist in the namespace, it is not deterministic
  which default value will be applied.
