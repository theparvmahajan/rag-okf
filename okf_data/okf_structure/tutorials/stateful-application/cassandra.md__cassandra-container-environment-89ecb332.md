---
id: okf-structure/tutorials/stateful-application/cassandra.md#cassandra-container-environment-variables
kind: section
title: Cassandra container environment variables
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Cassandra container environment variables
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#cleanup
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#whatsnext
word_count: 77
---

The Pods in this tutorial use the `gcr.io/google-samples/cassandra:v13`
image from Google's container registry.
The Docker image above is based on debian-base
and includes OpenJDK 8.

This image includes a standard Cassandra installation from the Apache Debian repo.
By using environment variables you can change values that are inserted into `cassandra.yaml`.

| Environment variable     | Default value    |
| ------------------------ |:---------------: |
| `CASSANDRA_CLUSTER_NAME` | `'Test Cluster'` |
| `CASSANDRA_NUM_TOKENS`   | `32`             |
| `CASSANDRA_RPC_ADDRESS`  | `0.0.0.0`        |
