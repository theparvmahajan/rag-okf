---
id: okf-structure/concepts/security/pod-security-admission.md#metrics
kind: section
title: Metrics
source: concepts/security/pod-security-admission.md
url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
heading: Metrics
parent: okf-structure/concepts/security/pod-security-admission
children: []
prev_sibling: okf-structure/concepts/security/pod-security-admission.md#exemptions
next_sibling: okf-structure/concepts/security/pod-security-admission.md#whatsnext
word_count: 72
---

Here are the Prometheus metrics exposed by kube-apiserver:

- `pod_security_errors_total`: This metric indicates the number of errors preventing normal evaluation.
  Non-fatal errors may result in the latest restricted profile being used for enforcement.
- `pod_security_evaluations_total`: This metric indicates the number of policy evaluations that have occurred,
  not counting ignored or exempt requests during exporting.
- `pod_security_exemptions_total`: This metric indicates the number of exempt requests, not counting ignored
  or out of scope requests.
