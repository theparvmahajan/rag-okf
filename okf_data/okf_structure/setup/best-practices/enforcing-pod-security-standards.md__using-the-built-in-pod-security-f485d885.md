---
id: okf-structure/setup/best-practices/enforcing-pod-security-standards.md#using-the-built-in-pod-security-admission-controller
kind: section
title: Using the built-in Pod Security Admission Controller
source: setup/best-practices/enforcing-pod-security-standards.md
url: https://kubernetes.io/docs/setup/best-practices/enforcing-pod-security-standards/
heading: Using the built-in Pod Security Admission Controller
parent: okf-structure/setup/best-practices/enforcing-pod-security-standards
children: []
prev_sibling: okf-structure/setup/best-practices/enforcing-pod-security-standards.md#introduction
next_sibling: okf-structure/setup/best-practices/enforcing-pod-security-standards.md#third-party-alternatives
word_count: 402
---

The Pod Security Admission Controller
intends to replace the deprecated PodSecurityPolicies. 

### Configure all cluster namespaces

Namespaces that lack any configuration at all should be considered significant gaps in your cluster
security model. We recommend taking the time to analyze the types of workloads occurring in each
namespace, and by referencing the Pod Security Standards, decide on an appropriate level for
each of them. Unlabeled namespaces should only indicate that they've yet to be evaluated.

In the scenario that all workloads in all namespaces have the same security requirements,
we provide an example
that illustrates how the PodSecurity labels can be applied in bulk.

### Embrace the principle of least privilege

In an ideal world, every pod in every namespace would meet the requirements of the `restricted`
policy. However, this is not possible nor practical, as some workloads will require elevated
privileges for legitimate reasons.

- Namespaces allowing `privileged` workloads should establish and enforce appropriate access controls.
- For workloads running in those permissive namespaces, maintain documentation about their unique
  security requirements. If at all possible, consider how those requirements could be further
  constrained.

### Adopt a multi-mode strategy

The `audit` and `warn` modes of the Pod Security Standards admission controller make it easy to
collect important security insights about your pods without breaking existing workloads.

It is good practice to enable these modes for all namespaces, setting them to the _desired_ level
and version you would eventually like to `enforce`. The warnings and audit annotations generated in
this phase can guide you toward that state. If you expect workload authors to make changes to fit
within the desired level, enable the `warn` mode. If you expect to use audit logs to monitor/drive
changes to fit within the desired level, enable the `audit` mode.

When you have the `enforce` mode set to your desired value, these modes can still be useful in a
few different ways:

- By setting `warn` to the same level as `enforce`, clients will receive warnings when attempting
  to create Pods (or resources that have Pod templates) that do not pass validation. This will help
  them update those resources to become compliant.
- In Namespaces that pin `enforce` to a specific non-latest version, setting the `audit` and `warn`
  modes to the same level as `enforce`, but to the `latest` version, gives visibility into settings
  that were allowed by previous versions but are not allowed per current best practices.
