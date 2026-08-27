---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#understanding-configmaps-and-pods
kind: section
title: Understanding ConfigMaps and Pods
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Understanding ConfigMaps and Pods
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#add-configmap-data-to-a-volume
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#optional-configmaps
word_count: 258
---

The ConfigMap API resource stores configuration data as key-value pairs. The data can be consumed
in pods or provide the configurations for system components such as controllers. ConfigMap is
similar to Secrets, but provides a means of working
with strings that don't contain sensitive information. Users and system components alike can
store configuration data in ConfigMap.

ConfigMaps should reference properties files, not replace them. Think of the ConfigMap as
representing something similar to the Linux `/etc` directory and its contents. For example,
if you create a Kubernetes Volume from a ConfigMap, each
data item in the ConfigMap is represented by an individual file in the volume.

The ConfigMap's `data` field contains the configuration data. As shown in the example below,
this can be simple (like individual properties defined using `--from-literal`) or complex
(like configuration files or JSON blobs defined using `--from-file`).

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: 2016-02-18T19:14:38Z
  name: example-config
  namespace: default
data:
  # example of a simple property defined using --from-literal
  example.property.1: hello
  example.property.2: world
  # example of a complex property defined using --from-file
  example.property.file: |-
    property.1=value-1
    property.2=value-2
    property.3=value-3
```

When `kubectl` creates a ConfigMap from inputs that are not ASCII or UTF-8, the tool puts
these into the `binaryData` field of the ConfigMap, and not in `data`. Both text and binary
data sources can be combined in one ConfigMap.

If you want to view the `binaryData` keys (and their values) in a ConfigMap, you can run
`kubectl get configmap -o jsonpath='{.binaryData}' <name>`.

Pods can load data from a ConfigMap that uses either `data` or `binaryData`.
