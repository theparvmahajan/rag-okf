---
id: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#define-an-environment-variable-for-a-container
kind: section
title: Define an environment variable for a container
source: tasks/inject-data-application/define-environment-variable-container.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/
heading: Define an environment variable for a container
parent: okf-structure/tasks/inject-data-application/define-environment-variable-container
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-container.md#using-environment-variables-inside-of-your-config
word_count: 289
---

When you create a Pod, you can set environment variables for the containers
that run in the Pod. To set environment variables, include the `env` or
`envFrom` field in the configuration file.

The `env` and `envFrom` fields have different effects.

`env`
: allows you to set environment variables for a container, specifying a value directly for each variable that you name.

`envFrom`
: allows you to set environment variables for a container by referencing either a ConfigMap or a Secret.
 When you use `envFrom`, all the key-value pairs in the referenced ConfigMap or Secret
 are set as environment variables for the container.
 You can also specify a common prefix string.

You can read more about ConfigMap
and Secret.

This page explains how to use `env`.

In this exercise, you create a Pod that runs one container. The configuration
file for the Pod defines an environment variable with name `DEMO_GREETING` and
value `"Hello from the environment"`. Here is the configuration manifest for the
Pod:

1. Create a Pod based on that manifest:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/envars.yaml
   ```

1. List the running Pods:

   ```shell
   kubectl get pods -l purpose=demonstrate-envars
   ```

   The output is similar to:

   ```
   NAME            READY     STATUS    RESTARTS   AGE
   envar-demo      1/1       Running   0          9s
   ```

1. List the Pod's container environment variables:

   ```shell
   kubectl exec envar-demo -- printenv
   ```

   The output is similar to this:

   ```
   NODE_VERSION=4.4.2
   EXAMPLE_SERVICE_PORT_8080_TCP_ADDR=10.3.245.237
   HOSTNAME=envar-demo
   ...
   DEMO_GREETING=Hello from the environment
   DEMO_FAREWELL=Such a sweet sorrow
   ```

The environment variables set using the `env` or `envFrom` field
override any environment variables specified in the container image.

Environment variables may reference each other, however ordering is important.
Variables making use of others defined in the same context must come later in
the list. Similarly, avoid circular references.
