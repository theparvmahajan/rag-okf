---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#restrictions
kind: section
title: Restrictions
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Restrictions
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#optional-configmaps
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#cleanup
word_count: 208
---

- You must create the `ConfigMap` object before you reference it in a Pod
  specification. Alternatively, mark the ConfigMap reference as `optional` in the Pod spec (see
  Optional ConfigMaps). If you reference a ConfigMap that doesn't exist
  and you don't mark the reference as `optional`, the Pod won't start. Similarly, references
  to keys that don't exist in the ConfigMap will also prevent the Pod from starting, unless
  you mark the key references as `optional`.

- If you use `envFrom` to define environment variables from ConfigMaps, keys that are considered
  invalid will be skipped. The pod will be allowed to start, but the invalid names will be
  recorded in the event log (`InvalidVariableNames`). The log message lists each skipped
  key. For example:

  ```shell
  kubectl get events
  ```

  The output is similar to this:
  ```
  LASTSEEN FIRSTSEEN COUNT NAME          KIND  SUBOBJECT  TYPE      REASON                            SOURCE                MESSAGE
  0s       0s        1     dapi-test-pod Pod              Warning   InvalidEnvironmentVariableNames   {kubelet, 127.0.0.1}  Keys [1badkey, 2alsobad] from the EnvFrom configMap default/myconfig were skipped since they are considered invalid environment variable names.
  ```

- ConfigMaps reside in a specific namespace.
  Pods can only refer to ConfigMaps that are in the same namespace as the Pod.

- You can't use ConfigMaps for
  static pods, because the
  kubelet does not support this.
