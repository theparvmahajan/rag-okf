---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#optional-configmaps
kind: section
title: Optional ConfigMaps
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Optional ConfigMaps
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#understanding-configmaps-and-pods
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#restrictions
word_count: 262
---

You can mark a reference to a ConfigMap as _optional_ in a Pod specification.
If the ConfigMap doesn't exist, the configuration for which it provides data in the Pod
(for example: environment variable, mounted volume) will be empty.
If the ConfigMap exists, but the referenced key is non-existent the data is also empty.

For example, the following Pod specification marks an environment variable from a ConfigMap
as optional:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox
      command: ["/bin/sh", "-c", "env"]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: a-config
              key: akey
              optional: true # mark the variable as optional
  restartPolicy: Never
```

If you run this pod, and there is no ConfigMap named `a-config`, the output is empty.
If you run this pod, and there is a ConfigMap named `a-config` but that ConfigMap doesn't have
a key named `akey`, the output is also empty. If you do set a value for `akey` in the `a-config`
ConfigMap, this pod prints that value and then terminates.

You can also mark the volumes and files provided by a ConfigMap as optional. Kubernetes always
creates the mount paths for the volume, even if the referenced ConfigMap or key doesn't exist. For
example, the following Pod specification marks a volume that references a ConfigMap as optional:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod
spec:
  containers:
    - name: test-container
      image: gcr.io/google_containers/busybox
      command: ["/bin/sh", "-c", "ls /etc/config"]
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config
  volumes:
    - name: config-volume
      configMap:
        name: no-config
        optional: true # mark the source ConfigMap as optional
  restartPolicy: Never
```
