---
id: okf-structure/tutorials/stateful-application/cassandra.md#validating-the-cassandra-statefulset
kind: section
title: Validating the Cassandra StatefulSet
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Validating the Cassandra StatefulSet
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#using-a-statefulset-to-create-a-cassandra-ring
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#modifying-the-cassandra-statefulset
word_count: 188
---

1. Get the Cassandra StatefulSet:

    ```shell
    kubectl get statefulset cassandra
    ```

    The response should be similar to:

    ```
    NAME        DESIRED   CURRENT   AGE
    cassandra   3         0         13s
    ```

    The `StatefulSet` resource deploys Pods sequentially.

1. Get the Pods to see the ordered creation status:

    ```shell
    kubectl get pods -l="app=cassandra"
    ```

    The response should be similar to:

    ```shell
    NAME          READY     STATUS              RESTARTS   AGE
    cassandra-0   1/1       Running             0          1m
    cassandra-1   0/1       ContainerCreating   0          8s
    ```

    It can take several minutes for all three Pods to deploy. Once they are deployed, the same command
    returns output similar to:

    ```
    NAME          READY     STATUS    RESTARTS   AGE
    cassandra-0   1/1       Running   0          10m
    cassandra-1   1/1       Running   0          9m
    cassandra-2   1/1       Running   0          8m
    ```

3. Run the Cassandra nodetool inside the first Pod, to
   display the status of the ring.

    ```shell
    kubectl exec -it cassandra-0 -- nodetool status
    ```

    The response should look something like:

    ```
    Datacenter: DC1-K8Demo
    ======================
    Status=Up/Down
    |/ State=Normal/Leaving/Joining/Moving
    --  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
    UN  172.17.0.5  83.57 KiB  32           74.0%             e2dd09e6-d9d3-477e-96c5-45094c08db0f  Rack1-K8Demo
    UN  172.17.0.4  101.04 KiB  32           58.8%             f89d6835-3a42-4419-92b3-0e62cae1479c  Rack1-K8Demo
    UN  172.17.0.6  84.74 KiB  32           67.1%             a6a1e8c2-3dc5-4417-b1a0-26507af2aaad  Rack1-K8Demo
    ```
