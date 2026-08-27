---
id: okf-structure/concepts/workloads/pods/advanced-pod-config.md#pod-overhead
kind: section
title: Pod overhead
source: concepts/workloads/pods/advanced-pod-config.md
url: https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/
heading: Pod overhead
parent: okf-structure/concepts/workloads/pods/advanced-pod-config
children: []
prev_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#influencing-pod-scheduling-decisions-scheduling
next_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#whatsnext
word_count: 66
---

Pod overhead allows you to account for the resources consumed by the Pod infrastructure on top of the container requests and limits.

---
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: kvisor-runtime
handler: kvisor-runtime
overhead:
  podFixed:
    memory: "2Gi"
    cpu: "500m"
---
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: kvisor-runtime
  containers:
  - name: myapp
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
