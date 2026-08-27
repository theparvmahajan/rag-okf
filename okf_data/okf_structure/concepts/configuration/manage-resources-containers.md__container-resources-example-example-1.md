---
id: okf-structure/concepts/configuration/manage-resources-containers.md#container-resources-example-example-1
kind: section
title: Container resources example {#example-1}
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: Container resources example {#example-1}
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#resource-units-in-kubernetes
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#pod-resources-example-example-2
word_count: 104
---

The following Pod has two containers. Both containers are defined with a request for
0.25 CPU
and 64MiB (2<sup>26</sup> bytes) of memory. Each container has a limit of 0.5
CPU and 128MiB of memory. You can say the Pod has a request of 0.5 CPU and 128
MiB of memory, and a limit of 1 CPU and 256MiB of memory.

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```
