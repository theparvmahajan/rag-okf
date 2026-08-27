---
id: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-resource-requests-and-limits-at-both-pod-level-and-container-level
kind: section
title: Create a pod with resource requests and limits at both pod-level and container-level
source: tasks/configure-pod-container/assign-pod-level-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
heading: Create a pod with resource requests and limits at both pod-level and container-level
parent: okf-structure/tasks/configure-pod-container/assign-pod-level-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#create-a-pod-with-cpu-requests-and-limits-at-pod-level
next_sibling: okf-structure/tasks/configure-pod-container/assign-pod-level-resources.md#clean-up
word_count: 322
---

To assign CPU and memory resources to a Pod, you can specify them at both the pod
level and the container level.  Include the `resources` field in the Pod spec to
define resources for the entire Pod. Additionally, include the `resources` field
within container's specification in the Pod's manifest to set container-specific
resource requirements.

In this exercise, you'll create a Pod with two containers to explore the interaction
of pod-level and container-level resource specifications. The Pod itself will have
defined CPU requests and limits, while only one of the containers will have its own
explicit resource requests and limits. The other container will inherit the resource
constraints from the pod-level settings. Here's the configuration file for the Pod:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/pod-level-resources.yaml --namespace=pod-resources-example
```

Verify that the Pod Container is running:

```shell
kubectl get pod pod-resources-demo --namespace=pod-resources-example
```

View detailed information about the Pod:

```shell
kubectl get pod pod-resources-demo --output=yaml --namespace=pod-resources-example
```

The output shows that one container in the Pod has a memory request of 50 MiB and a
CPU request of 0.5 cores, with a memory limit of 100 MiB and a CPU limit of 0.5
cores. The Pod itself has a memory request of 100 MiB and a CPU request of
1 core, and a memory limit of 200 MiB and a CPU limit of 1 core.

```yaml
...
  containers:
  -
    name: pod-resources-demo-ctr-1
    resources:
      limits:
        cpu: 500m
        memory: 100Mi
      requests:
        cpu: 500m
        memory: 50Mi
...
  -
    name: pod-resources-demo-ctr-2
    resources: {}
...
  resources:
    limits:
      cpu: "1"
      memory: 200Mi
    requests:
      cpu: "1"
      memory: 100Mi
...
```

Since pod-level requests and limits are specified, the request guarantees for both
containers in the pod will be equal 1 core or CPU and 100Mi of memory. Additionally,
both containers together won't be able to use more resources than specified in the
pod-level limits, ensuring they cannot exceed a combined total of 200 MiB of memory
and 1 core of CPU.
