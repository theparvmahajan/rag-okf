---
id: okf-structure/tasks/configure-pod-container/image-volumes.md#run-a-pod-that-uses-an-image-volume-create-pod
kind: section
title: Run a Pod that uses an image volume {#create-pod}
source: tasks/configure-pod-container/image-volumes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/
heading: Run a Pod that uses an image volume {#create-pod}
parent: okf-structure/tasks/configure-pod-container/image-volumes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/image-volumes.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/image-volumes.md#use-subpath-or-subpathexpr
word_count: 100
---

An image volume for a pod is enabled by setting the `volumes[*].image` field of `.spec`
to a valid reference and consuming it in the `volumeMounts` of the container. For example:

1. Create the pod on your cluster:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/image-volumes.yaml
   ```

1. Attach to the container:

   ```shell
   kubectl exec image-volume -it -- bash
   ```

1. Check the content of a file in the volume:

   ```shell
   cat /volume/dir/file
   ```

   The output is similar to:

   ```none
   1
   ```

   You can also check another file in a different path:

   ```shell
   cat /volume/file
   ```

   The output is similar to:

   ```none
   2
   ```
