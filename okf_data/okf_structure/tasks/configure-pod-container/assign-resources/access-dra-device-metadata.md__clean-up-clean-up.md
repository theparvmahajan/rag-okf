---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#clean-up-clean-up
kind: section
title: Clean up {#clean-up}
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: Clean up {#clean-up}
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#read-metadata-in-your-application-read-metadata-application
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#whatsnext
word_count: 16
---

Delete the resources that you created:

```shell
kubectl delete -f https://k8s.io/examples/dra/dra-device-metadata-pod.yaml
kubectl delete -f https://k8s.io/examples/dra/dra-device-metadata-template-pod.yaml
```
