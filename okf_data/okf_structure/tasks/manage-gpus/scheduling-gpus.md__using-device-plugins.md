---
id: okf-structure/tasks/manage-gpus/scheduling-gpus.md#using-device-plugins
kind: section
title: Using device plugins
source: tasks/manage-gpus/scheduling-gpus.md
url: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
heading: Using device plugins
parent: okf-structure/tasks/manage-gpus/scheduling-gpus
children: []
prev_sibling: okf-structure/tasks/manage-gpus/scheduling-gpus.md#introduction
next_sibling: okf-structure/tasks/manage-gpus/scheduling-gpus.md#manage-clusters-with-different-types-of-gpus
word_count: 206
---

Kubernetes implements device plugins to let Pods access specialized hardware features such as GPUs.

As an administrator, you have to install GPU drivers from the corresponding
hardware vendor on the nodes and run the corresponding device plugin from the
GPU vendor. Here are some links to vendors' instructions:

* AMD
* Intel
* NVIDIA

Once you have installed the plugin, your cluster exposes a custom schedulable resource such as `amd.com/gpu` or `nvidia.com/gpu`.

You can consume these GPUs from your containers by requesting
the custom GPU resource, the same way you request `cpu` or `memory`.
However, there are some limitations in how you specify the resource
requirements for custom devices.

GPUs are only supposed to be specified in the `limits` section, which means:
* You can specify GPU `limits` without specifying `requests`, because
  Kubernetes will use the limit as the request value by default.
* You can specify GPU in both `limits` and `requests` but these two values
  must be equal.
* You cannot specify GPU `requests` without specifying `limits`.

Here's an example manifest for a Pod that requests a GPU:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-vector-add
spec:
  restartPolicy: OnFailure
  containers:
    - name: example-vector-add
      image: "registry.example/example-vector-add:v42"
      resources:
        limits:
          gpu-vendor.example/example-gpu: 1 # requesting 1 GPU
```
