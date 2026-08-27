---
id: okf-structure/tasks/administer-cluster/cpu-management-policies.md#configuration
kind: section
title: Configuration
source: tasks/administer-cluster/cpu-management-policies.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/
heading: Configuration
parent: okf-structure/tasks/administer-cluster/cpu-management-policies
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#windows-support
next_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#changing-the-cpu-manager-policy
word_count: 204
---

The CPU Manager policy is set with the `--cpu-manager-policy` kubelet
flag or the `cpuManagerPolicy` field in KubeletConfiguration.
There are two supported policies:

* `none`: the default policy.
* `static`: allows pods with certain resource characteristics to be
  granted increased CPU affinity and exclusivity on the node.

The CPU manager periodically writes resource updates through the CRI in
order to reconcile in-memory CPU assignments with cgroupfs. The reconcile
frequency is set through a new Kubelet configuration value
`--cpu-manager-reconcile-period`. If not specified, it defaults to the same
duration as `--node-status-update-frequency`.

The behavior of the static policy can be fine-tuned using the `--cpu-manager-policy-options` flag.
The flag takes a comma-separated list of `key=value` policy options.
If you disable the `CPUManagerPolicyOptions`
feature gate
then you cannot fine-tune CPU manager policies. In that case, the CPU manager
operates only using its default settings.

In addition to the top-level `CPUManagerPolicyOptions` feature gate, the policy options are split
into two groups: alpha quality (hidden by default) and beta quality (visible by default).
The groups are guarded respectively by the `CPUManagerPolicyAlphaOptions`
and `CPUManagerPolicyBetaOptions` feature gates. Diverging from the Kubernetes standard, these
feature gates guard groups of options, because it would have been too cumbersome to add a feature
gate for each individual option.
