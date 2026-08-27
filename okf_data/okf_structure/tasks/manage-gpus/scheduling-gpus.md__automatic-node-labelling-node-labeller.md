---
id: okf-structure/tasks/manage-gpus/scheduling-gpus.md#automatic-node-labelling-node-labeller
kind: section
title: Automatic node labelling {#node-labeller}
source: tasks/manage-gpus/scheduling-gpus.md
url: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
heading: Automatic node labelling {#node-labeller}
parent: okf-structure/tasks/manage-gpus/scheduling-gpus
children: []
prev_sibling: okf-structure/tasks/manage-gpus/scheduling-gpus.md#manage-clusters-with-different-types-of-gpus
next_sibling: null
word_count: 241
---

As an administrator, you can automatically discover and label all your GPU enabled nodes
by deploying Kubernetes Node Feature Discovery (NFD).
NFD detects the hardware features that are available on each node in a Kubernetes cluster.
Typically, NFD is configured to advertise those features as node labels, but NFD can also add extended resources, annotations, and node taints.
NFD is compatible with all supported versions of Kubernetes.
By default NFD create the feature labels for the detected features.
Administrators can leverage NFD to also taint nodes with specific features, so that only pods that request those features can be scheduled on those nodes.

You also need a plugin for NFD that adds appropriate labels to your nodes; these might be generic
labels or they could be vendor specific. Your GPU vendor may provide a third party
plugin for NFD; check their documentation for more details.

apiVersion: v1
kind: Pod
metadata:
  name: example-vector-add
spec:
  restartPolicy: OnFailure
  # You can use Kubernetes node affinity to schedule this Pod onto a node
  # that provides the kind of GPU that its container needs in order to work
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: "gpu.gpu-vendor.example/installed-memory"
            operator: Gt # (greater than)
            values: ["40535"]
          - key: "feature.node.kubernetes.io/pci-10.present" # NFD Feature label
            values: ["true"] # (optional) only schedule on nodes with PCI device 10
  containers:
    - name: example-vector-add
      image: "registry.example/example-vector-add:v42"
      resources:
        limits:
          gpu-vendor.example/example-gpu: 1 # requesting 1 GPU

#### GPU vendor implementations

- Intel
- NVIDIA
