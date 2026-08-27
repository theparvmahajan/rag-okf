---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#id-count-for-each-of-pods
kind: section
title: ID count for each of Pods
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: ID count for each of Pods
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#set-up-a-node-to-support-user-namespaces
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#integration-with-pod-security-admission-checks
word_count: 80
---

Starting with Kubernetes v1.33, the ID count for each of Pods can be set in
`KubeletConfiguration`.

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
userNamespaces:
  idsPerPod: 1048576
```

The value of `idsPerPod` (uint32) must be a multiple of 65536.
The default value is 65536.
This value only applies to containers created after the kubelet was started with
this `KubeletConfiguration`.
Running containers are not affected by this config.

In Kubernetes prior to v1.33, the ID count for each of Pods was hard-coded to
65536.
