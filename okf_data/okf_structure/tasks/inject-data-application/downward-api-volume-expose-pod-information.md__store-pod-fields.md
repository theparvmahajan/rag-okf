---
id: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#store-pod-fields
kind: section
title: Store Pod fields
source: tasks/inject-data-application/downward-api-volume-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/
heading: Store Pod fields
parent: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information
children: []
prev_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#store-container-fields
word_count: 396
---

In this part of exercise, you create a Pod that has one container, and you
project Pod-level fields into the running container as files.
Here is the manifest for the Pod:

In the manifest, you can see that the Pod has a `downwardAPI` Volume,
and the container mounts the volume at `/etc/podinfo`.

Look at the `items` array under `downwardAPI`. Each element of the array
defines a `downwardAPI` volume.
The first element specifies that the value of the Pod's
`metadata.labels` field should be stored in a file named `labels`.
The second element specifies that the value of the Pod's `annotations`
field should be stored in a file named `annotations`.

The fields in this example are Pod fields. They are not
fields of the container in the Pod.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/inject/dapi-volume.yaml
```

Verify that the container in the Pod is running:

```shell
kubectl get pods
```

View the container's logs:

```shell
kubectl logs kubernetes-downwardapi-volume-example
```

The output shows the contents of the `labels` file and the `annotations` file:

```
cluster="test-cluster1"
rack="rack-22"
zone="us-est-coast"

build="two"
builder="john-doe"
```

Get a shell into the container that is running in your Pod:

```shell
kubectl exec -it kubernetes-downwardapi-volume-example -- sh
```

In your shell, view the `labels` file:

```shell
/# cat /etc/podinfo/labels
```

The output shows that all of the Pod's labels have been written
to the `labels` file:

```shell
cluster="test-cluster1"
rack="rack-22"
zone="us-est-coast"
```

Similarly, view the `annotations` file:

```shell
/# cat /etc/podinfo/annotations
```

View the files in the `/etc/podinfo` directory:

```shell
/# ls -laR /etc/podinfo
```

In the output, you can see that the `labels` and `annotations` files
are in a temporary subdirectory: in this example,
`..2982_06_02_21_47_53.299460680`. In the `/etc/podinfo` directory, `..data` is
a symbolic link to the temporary subdirectory. Also in the `/etc/podinfo` directory,
`labels` and `annotations` are symbolic links.

```
drwxr-xr-x  ... Feb 6 21:47 ..2982_06_02_21_47_53.299460680
lrwxrwxrwx  ... Feb 6 21:47 ..data -> ..2982_06_02_21_47_53.299460680
lrwxrwxrwx  ... Feb 6 21:47 annotations -> ..data/annotations
lrwxrwxrwx  ... Feb 6 21:47 labels -> ..data/labels

/etc/..2982_06_02_21_47_53.299460680:
total 8
-rw-r--r--  ... Feb  6 21:47 annotations
-rw-r--r--  ... Feb  6 21:47 labels
```

Using symbolic links enables dynamic atomic refresh of the metadata; updates are
written to a new temporary directory, and the `..data` symlink is updated
atomically using rename(2).

A container using Downward API as a
subPath volume mount will not
receive Downward API updates.

Exit the shell:

```shell
/# exit
```
