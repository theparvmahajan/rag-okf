---
id: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#configure-a-projected-volume-for-a-pod
kind: section
title: Configure a projected volume for a pod
source: tasks/configure-pod-container/configure-projected-volume-storage.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-projected-volume-storage/
heading: Configure a projected volume for a pod
parent: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/configure-projected-volume-storage.md#clean-up
word_count: 170
---

In this exercise, you create username and password Secrets from local files. You then create a Pod that runs one container, using a `projected` Volume to mount the Secrets into the same shared directory.

Here is the configuration file for the Pod:

1. Create the Secrets:

    ```shell
    # Create files containing the username and password:
    echo -n "admin" > ./username.txt
    echo -n "1f2d1e2e67df" > ./password.txt

    # Package these files into secrets:
    kubectl create secret generic user --from-file=./username.txt
    kubectl create secret generic pass --from-file=./password.txt
    ```
1. Create the Pod:

    ```shell
    kubectl apply -f https://k8s.io/examples/pods/storage/projected.yaml
    ```
1. Verify that the Pod's container is running, and then watch for changes to
the Pod:

    ```shell
    kubectl get --watch pod test-projected-volume
    ```
    The output looks like this:
    ```
    NAME                    READY     STATUS    RESTARTS   AGE
    test-projected-volume   1/1       Running   0          14s
    ```
1. In another terminal, get a shell to the running container:

    ```shell
    kubectl exec -it test-projected-volume -- /bin/sh
    ```
1. In your shell, verify that the `projected-volume` directory contains your projected sources:

    ```shell
    ls /projected-volume/
    ```
