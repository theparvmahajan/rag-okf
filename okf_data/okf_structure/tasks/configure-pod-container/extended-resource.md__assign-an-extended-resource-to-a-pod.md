---
id: okf-structure/tasks/configure-pod-container/extended-resource.md#assign-an-extended-resource-to-a-pod
kind: section
title: Assign an extended resource to a Pod
source: tasks/configure-pod-container/extended-resource.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/extended-resource/
heading: Assign an extended resource to a Pod
parent: okf-structure/tasks/configure-pod-container/extended-resource
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/extended-resource.md#attempt-to-create-a-second-pod
word_count: 105
---

To request an extended resource, include the `resources.requests.<resource_name>` field
in the container manifest.
`*.kubernetes.io/`. Valid extended resource names have the form `example.com/foo` where
`example.com` is replaced with your organization's domain and `foo` is a
descriptive resource name.

Here is the configuration file for a Pod that has one Container:

In the configuration file, you can see that the Container requests 3 dongles.

Create a Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/resource/extended-resource-pod.yaml
```

Verify that the Pod is running:

```shell
kubectl get pod extended-resource-demo
```

Describe the Pod:

```shell
kubectl describe pod extended-resource-demo
```

The output shows dongle requests:

```yaml
Limits:
  example.com/dongle: 3
Requests:
  example.com/dongle: 3
```
