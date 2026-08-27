---
id: okf-structure/concepts/workloads/pods/pod-condition.md#structure-of-a-pod-condition
kind: section
title: Structure of a Pod condition
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: Structure of a Pod condition
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#built-in-pod-conditions-built-in-pod-conditions
word_count: 136
---

A Pod's status includes an array of
PodConditions
that indicate whether the Pod has passed certain checkpoints.

Each element of the PodCondition array has the following fields:

| Field name           | Description                                                                                          |
|:---------------------|:-----------------------------------------------------------------------------------------------------|
| `type`               | Name of this Pod condition.                                                                          |
| `status`             | Indicates whether that condition is applicable, with possible values `"True"`, `"False"`, or `"Unknown"`. |
| `lastProbeTime`      | Timestamp of when the Pod condition was last probed.                                                 |
| `lastTransitionTime` | Timestamp for when the Pod last transitioned from one status to another.                             |
| `reason`             | Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition.     |
| `message`            | Human-readable message indicating details about the last status transition.                          |
| `observedGeneration` | The `.metadata.generation` of the Pod at the time the condition was recorded. See Pod generation. |
