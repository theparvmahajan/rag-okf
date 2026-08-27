---
id: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#use-container-fields-as-values-for-environment-variables
kind: section
title: Use container fields as values for environment variables
source: tasks/inject-data-application/environment-variable-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/
heading: Use container fields as values for environment variables
parent: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information
children: []
prev_sibling: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#use-pod-fields-as-values-for-environment-variables
next_sibling: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#whatsnext
word_count: 178
---

In the preceding exercise, you used information from Pod-level fields as the values
for environment variables.
In this next exercise, you are going to pass fields that are part of the Pod
definition, but taken from the specific
container
rather than from the Pod overall.

Here is a manifest for another Pod that again has just one container:

In this manifest, you can see four environment variables. The `env`
field is an array of
environment variable definitions.
The first element in the array specifies that the `MY_CPU_REQUEST` environment
variable gets its value from the `requests.cpu` field of a container named
`test-container`. Similarly, the other environment variables get their values
from fields that are specific to this container.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-container.yaml
```

Verify that the container in the Pod is running:

```shell
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

View the container's logs:

```shell
kubectl logs dapi-envars-resourcefieldref
```

The output shows the values of selected environment variables:

```
1
1
33554432
67108864
```
