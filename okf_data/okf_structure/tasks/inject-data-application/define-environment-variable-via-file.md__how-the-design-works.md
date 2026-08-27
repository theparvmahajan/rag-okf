---
id: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#how-the-design-works
kind: section
title: How the design works
source: tasks/inject-data-application/define-environment-variable-via-file.md
url: https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-via-file/
heading: How the design works
parent: okf-structure/tasks/inject-data-application/define-environment-variable-via-file
children: []
prev_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/define-environment-variable-via-file.md#env-file-syntax-env-file-syntax
word_count: 265
---

In this exercise, you will create a Pod that sources environment variables from files, 
projecting these values into the running container.

In this manifest, you can see the `initContainer` mounts an `emptyDir` volume and writes environment variables to a file within it,
and the regular containers reference both the file and the environment variable key 
through the `fileKeyRef` field without needing to mount the volume. 
When `optional` field is set to false, the specified `key` in `fileKeyRef` must exist in the environment variables file.

The volume will only be mounted to the container that writes to the file
(`initContainer`), while the consumer container that consumes the environment variable will not have the volume mounted.

The env file format adheres to the kubernetes env file standard.

During container initialization, the kubelet retrieves environment variables 
from specified files in the `emptyDir` volume and exposes them to the container.

All container types (initContainers, regular containers, sidecars containers,
and ephemeral containers) support environment variable loading from files.

While these environment variables can store sensitive information, 
`emptyDir` volumes don't provide the same protection mechanisms as
dedicated Secret objects. Therefore, exposing confidential environment variables 
to containers through this feature is not considered a security best practice.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/envars-file-container.yaml
```

Verify that the container in the Pod is running:

```shell
# If the new Pod isn't yet healthy, rerun this command a few times.
kubectl get pods
```

Check container logs for environment variables:

```shell
kubectl logs envfile-test-pod -c use-envfile | grep DB_ADDRESS
```

The output shows the values of selected environment variables:

```
DB_ADDRESS=address
```
