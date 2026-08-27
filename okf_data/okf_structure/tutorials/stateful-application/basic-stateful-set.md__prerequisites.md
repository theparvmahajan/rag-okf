---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Prerequisites
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#introduction
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#objectives
word_count: 150
---

Before you begin this tutorial, you should familiarize yourself with the
following Kubernetes concepts:

* Pods
* Cluster DNS
* Headless Services
* PersistentVolumes
* PersistentVolumes Provisioning
* The kubectl command line tool

You should configure `kubectl` to use a context that uses the `default`
namespace.
If you are using an existing cluster, make sure that it's OK to use that
cluster's default namespace to practice. Ideally, practice in a cluster
that doesn't run any real workloads.

It's also useful to read the concept page about StatefulSets.

This tutorial assumes that your cluster is configured to dynamically provision
PersistentVolumes. You'll also need to have a default StorageClass.
If your cluster is not configured to provision storage dynamically, you
will have to manually provision two 1 GiB volumes prior to starting this
tutorial and
set up your cluster so that those PersistentVolumes map to the
PersistentVolumeClaim templates that the StatefulSet defines.
