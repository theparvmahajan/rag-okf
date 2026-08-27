---
id: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#store-container-fields
kind: section
title: Store container fields
source: tasks/inject-data-application/downward-api-volume-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/
heading: Store container fields
parent: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information
children: []
prev_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#store-pod-fields
next_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#project-keys-to-specific-paths-and-file-permissions
word_count: 218
---

The preceding exercise, you made Pod-level fields accessible using the
downward API.
In this next exercise, you are going to pass fields that are part of the Pod
definition, but taken from the specific
container
rather than from the Pod overall. Here is a manifest for a Pod that again has
just one container:

In the manifest, you can see that the Pod has a
`downwardAPI` volume,
and that the single container in that Pod mounts the volume at `/etc/podinfo`.

Look at the `items` array under `downwardAPI`. Each element of the array
defines a file in the downward API volume.

The first element specifies that in the container named `client-container`,
the value of the `limits.cpu` field in the format specified by `1m` should be
published as a file named `cpu_limit`. The `divisor` field is optional and has the
default value of `1`. A divisor of 1 means cores for `cpu` resources, or
bytes for `memory` resources.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume-resources.yaml
```

Get a shell into the container that is running in your Pod:

```shell
kubectl exec -it kubernetes-downwardapi-volume-example-2 -- sh
```

In your shell, view the `cpu_limit` file:

```shell
# Run this in a shell inside the container
cat /etc/podinfo/cpu_limit
```

You can use similar commands to view the `cpu_request`, `mem_limit` and
`mem_request` files.
