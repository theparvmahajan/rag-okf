---
id: okf-structure/tasks/configure-pod-container/image-volumes.md#use-subpath-or-subpathexpr
kind: section
title: Use `subPath` (or `subPathExpr`)
source: tasks/configure-pod-container/image-volumes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/
heading: Use `subPath` (or `subPathExpr`)
parent: okf-structure/tasks/configure-pod-container/image-volumes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/image-volumes.md#run-a-pod-that-uses-an-image-volume-create-pod
next_sibling: okf-structure/tasks/configure-pod-container/image-volumes.md#further-reading
word_count: 70
---

It is possible to utilize
`subPath` or
`subPathExpr`
from Kubernetes v1.33 when using the image volume feature.

1. Create the pod on your cluster:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/image-volumes-subpath.yaml
   ```

1. Attach to the container:

   ```shell
   kubectl exec image-volume -it -- bash
   ```

1. Check the content of the file from the `dir` sub path in the volume:

   ```shell
   cat /volume/file
   ```

   The output is similar to:

   ```none
   1
   ```
