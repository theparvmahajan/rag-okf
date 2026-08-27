---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#define-container-environment-variables-using-configmap-data
kind: section
title: Define container environment variables using ConfigMap data
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Define container environment variables using ConfigMap data
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#interim-cleanup
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
word_count: 156
---

### Define a container environment variable with data from a single ConfigMap

1. Define an environment variable as a key-value pair in a ConfigMap:

   ```shell
   kubectl create configmap special-config --from-literal=special.how=very
   ```

2. Assign the `special.how` value defined in the ConfigMap to the `SPECIAL_LEVEL_KEY`
   environment variable in the Pod specification.

   

   Create the Pod:

   ```shell
   kubectl create -f https://kubernetes.io/examples/pods/pod-single-configmap-env-variable.yaml
   ```

   Now, the Pod's output includes environment variable `SPECIAL_LEVEL_KEY=very`.

### Define container environment variables with data from multiple ConfigMaps

As with the previous example, create the ConfigMaps first.
Here is the manifest you will use:

* Create the ConfigMap:

  ```shell
  kubectl create -f https://kubernetes.io/examples/configmap/configmaps.yaml
  ```

* Define the environment variables in the Pod specification.

  

  Create the Pod:

  ```shell
  kubectl create -f https://kubernetes.io/examples/pods/pod-multiple-configmap-env-variable.yaml
  ```

  Now, the Pod's output includes environment variables `SPECIAL_LEVEL_KEY=very` and `LOG_LEVEL=INFO`.

  Once you're happy to move on, delete that Pod and ConfigMap:
  ```shell
  kubectl delete pod dapi-test-pod --now
  kubectl delete configmap special-config
  kubectl delete configmap env-config
  ```
