---
id: okf-structure/concepts/workloads/pods/advanced-pod-config.md#runtimeclasses
kind: section
title: RuntimeClasses
source: concepts/workloads/pods/advanced-pod-config.md
url: https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/
heading: RuntimeClasses
parent: okf-structure/concepts/workloads/pods/advanced-pod-config
children: []
prev_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#priorityclasses
next_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#pod-and-container-level-security-context-configuration-security-context
word_count: 119
---

A _RuntimeClass_ allows you to specify the low-level container runtime for a Pod. It is useful when you want to specify different container runtimes for different kinds of Pod, such as when you need different isolation levels or runtime features.

### Example Pod {#runtimeclass-pod-example}

apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  containers:
  - name: mycontainer
    image: nginx

A RuntimeClass is a cluster-scoped object that represents a container runtime that is available on some or all of your node.

The cluster administrator installs and configures the concrete runtimes backing the RuntimeClass.

They might set up that special container runtime configuration on all nodes, or perhaps just on some of them.

For more information, see the RuntimeClass documentation.
