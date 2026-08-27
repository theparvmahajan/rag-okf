---
id: okf-structure/concepts/scheduling-eviction/node-declared-features.md#how-it-works
kind: section
title: How it Works
source: concepts/scheduling-eviction/node-declared-features.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-declared-features/
heading: How it Works
parent: okf-structure/concepts/scheduling-eviction/node-declared-features
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-declared-features.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/node-declared-features.md#enabling-node-declared-features
word_count: 141
---

1.  **Kubelet Feature Reporting:** At startup, the kubelet on each node detects
    which managed Kubernetes features are currently enabled and reports them
    in the `.status.declaredFeatures` field of the Node. Only features
    under active development are included in this field.
2.  **Scheduler Filtering:** The default kube-scheduler uses the
    `NodeDeclaredFeatures` plugin. This plugin:
    * In the `PreFilter` stage, checks the `PodSpec` to infer the set of node
      features required by the pod.
    * In the `Filter` stage, checks if the features listed in the node's
      `.status.declaredFeatures` satisfy the requirements inferred for the Pod.
      Pods will not be scheduled on nodes lacking the required features.
    Custom schedulers can also utilize the
    `.status.declaredFeatures` field to enforce similar constraints.
3.  **Admission Control:** The `nodedeclaredfeaturevalidator` admission controller
    can reject Pods that require features not declared by the node they are
    bound to, preventing issues during pod updates.
