---
id: okf-structure/tutorials/stateful-application/cassandra.md#modifying-the-cassandra-statefulset
kind: section
title: Modifying the Cassandra StatefulSet
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Modifying the Cassandra StatefulSet
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#validating-the-cassandra-statefulset
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#cleanup
word_count: 168
---

Use `kubectl edit` to modify the size of a Cassandra StatefulSet.

1. Run the following command:

    ```shell
    kubectl edit statefulset cassandra
    ```

    This command opens an editor in your terminal. The line you need to change is the `replicas` field.
    The following sample is an excerpt of the StatefulSet file:

    ```yaml
    # Please edit the object below. Lines beginning with a '#' will be ignored,
    # and an empty file will abort the edit. If an error occurs while saving this file will be
    # reopened with the relevant failures.
    #
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      creationTimestamp: 2016-08-13T18:40:58Z
      generation: 1
      labels:
      app: cassandra
      name: cassandra
      namespace: default
      resourceVersion: "323"
      uid: 7a219483-6185-11e6-a910-42010a8a0fc0
    spec:
      replicas: 3
    ```

1. Change the number of replicas to 4, and then save the manifest.

    The StatefulSet now scales to run with 4 Pods.

1. Get the Cassandra StatefulSet to verify your change:

    ```shell
    kubectl get statefulset cassandra
    ```

    The response should be similar to:

    ```
    NAME        DESIRED   CURRENT   AGE
    cassandra   4         4         36m
    ```
