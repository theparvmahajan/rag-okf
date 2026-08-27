---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
kind: section
title: Configure all key-value pairs in a ConfigMap as container environment variables
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Configure all key-value pairs in a ConfigMap as container environment variables
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#define-container-environment-variables-using-configmap-data
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#use-configmap-defined-environment-variables-in-pod-commands
word_count: 79
---

* Create a ConfigMap containing multiple key-value pairs.

  

  Create the ConfigMap:

  ```shell
  kubectl create -f https://kubernetes.io/examples/configmap/configmap-multikeys.yaml
  ```

* Use `envFrom` to define all of the ConfigMap's data as container environment variables. The
  key from the ConfigMap becomes the environment variable name in the Pod.

  

  Create the Pod:

  ```shell
  kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-envFrom.yaml
  ```
  Now, the Pod's output includes environment variables `SPECIAL_LEVEL=very` and
  `SPECIAL_TYPE=charm`.

  Once you're happy to move on, delete that Pod:
  ```shell
  kubectl delete pod dapi-test-pod --now
  ```
