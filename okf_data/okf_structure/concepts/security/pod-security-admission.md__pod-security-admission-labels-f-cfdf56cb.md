---
id: okf-structure/concepts/security/pod-security-admission.md#pod-security-admission-labels-for-namespaces
kind: section
title: Pod Security Admission labels for namespaces
source: concepts/security/pod-security-admission.md
url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
heading: Pod Security Admission labels for namespaces
parent: okf-structure/concepts/security/pod-security-admission
children: []
prev_sibling: okf-structure/concepts/security/pod-security-admission.md#pod-security-levels
next_sibling: okf-structure/concepts/security/pod-security-admission.md#workload-resources-and-pod-templates
word_count: 259
---

Once the feature is enabled or the webhook is installed, you can configure namespaces to define the admission
control mode you want to use for pod security in each namespace. Kubernetes defines a set of 
labels that you can set to define which of the 
predefined Pod Security Standard levels you want to use for a namespace. The label you select
defines what action the control plane
takes if a potential violation is detected:

Mode | Description
:---------|:------------
**enforce** | Policy violations will cause the pod to be rejected.
**audit** | Policy violations will trigger the addition of an audit annotation to the event recorded in the audit log, but are otherwise allowed.
**warn** | Policy violations will trigger a user-facing warning, but are otherwise allowed.

A namespace can configure any or all modes, or even set a different level for different modes.

For each mode, there are two labels that determine the policy used:

```yaml
# The per-mode level label indicates which policy level to apply for the mode.
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# LEVEL must be one of `privileged`, `baseline`, or `restricted`.
pod-security.kubernetes.io/<MODE>: <LEVEL>

# Optional: per-mode version label that can be used to pin the policy to the
# version that shipped with a given Kubernetes minor version (for example v).
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# VERSION must be a valid Kubernetes minor version, or `latest`.
pod-security.kubernetes.io/<MODE>-version: <VERSION>
```

Check out Enforce Pod Security Standards with Namespace Labels to see example usage.
