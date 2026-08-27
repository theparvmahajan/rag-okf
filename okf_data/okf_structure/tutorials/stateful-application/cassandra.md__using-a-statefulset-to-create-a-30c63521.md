---
id: okf-structure/tutorials/stateful-application/cassandra.md#using-a-statefulset-to-create-a-cassandra-ring
kind: section
title: Using a StatefulSet to create a Cassandra ring
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Using a StatefulSet to create a Cassandra ring
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#creating-a-headless-service-for-cassandra-creating-a-cassandra-headless-service
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#validating-the-cassandra-statefulset
word_count: 101
---

The StatefulSet manifest, included below, creates a Cassandra ring that consists of three Pods.

This example uses the default provisioner for Minikube.
Please update the following StatefulSet for the cloud you are working with.

Create the Cassandra StatefulSet from the `cassandra-statefulset.yaml` file:

```shell
# Use this if you are able to apply cassandra-statefulset.yaml unmodified
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml
```

If you need to modify `cassandra-statefulset.yaml` to suit your cluster, download
https://k8s.io/examples/application/cassandra/cassandra-statefulset.yaml and then apply
that manifest, from the folder you saved the modified version into:
```shell
# Use this if you needed to modify cassandra-statefulset.yaml locally
kubectl apply -f cassandra-statefulset.yaml
```
