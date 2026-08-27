---
id: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#use-pod-fields-as-values-for-environment-variables
kind: section
title: Use Pod fields as values for environment variables
source: tasks/inject-data-application/environment-variable-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/
heading: Use Pod fields as values for environment variables
parent: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information
children: []
prev_sibling: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#use-container-fields-as-values-for-environment-variables
word_count: 260
---

In this part of exercise, you create a Pod that has one container, and you
project Pod-level fields into the running container as environment variables.

In that manifest, you can see five environment variables. The `env`
field is an array of
environment variable definitions.
The first element in the array specifies that the `MY_NODE_NAME` environment
variable gets its value from the Pod's `spec.nodeName` field. Similarly, the
other environment variables get their names from Pod fields.

The fields in this example are Pod fields. They are not fields of the
container in the Pod.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-envars-pod.yaml
```

Verify that the container in the Pod is running:

```shell
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

View the container's logs:

```shell
kubectl logs dapi-envars-fieldref
```

The output shows the values of selected environment variables:

```
minikube
dapi-envars-fieldref
default
172.17.0.4
default
```

To see why these values are in the log, look at the `command` and `args` fields
in the configuration file. When the container starts, it writes the values of
five environment variables to stdout. It repeats this every ten seconds.

Next, get a shell into the container that is running in your Pod:

```shell
kubectl exec -it dapi-envars-fieldref -- sh
```

In your shell, view the environment variables:

```shell
# Run this in a shell inside the container
printenv
```

The output shows that certain environment variables have been assigned the
values of Pod fields:

```
MY_POD_SERVICE_ACCOUNT=default
...
MY_POD_NAMESPACE=default
MY_POD_IP=172.17.0.4
...
MY_NODE_NAME=minikube
...
MY_POD_NAME=dapi-envars-fieldref
```
