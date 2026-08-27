---
id: okf-structure/concepts/configuration/configmap.md#motivation
kind: section
title: Motivation
source: concepts/configuration/configmap.md
url: https://kubernetes.io/docs/concepts/configuration/configmap/
heading: Motivation
parent: okf-structure/concepts/configuration/configmap
children: []
prev_sibling: okf-structure/concepts/configuration/configmap.md#introduction
next_sibling: okf-structure/concepts/configuration/configmap.md#configmap-object
word_count: 146
---

Use a ConfigMap for setting configuration data separately from application code.

For example, imagine that you are developing an application that you can run on your
own computer (for development) and in the cloud (to handle real traffic).
You write the code to look in an environment variable named `DATABASE_HOST`.
Locally, you set that variable to `localhost`. In the cloud, you set it to
refer to a Kubernetes Service
that exposes the database component to your cluster.
This lets you fetch a container image running in the cloud and
debug the exact same code locally if needed.

A ConfigMap is not designed to hold large chunks of data. The data stored in a
ConfigMap cannot exceed 1 MiB. If you need to store settings that are
larger than this limit, you may want to consider mounting a volume or use a
separate database or file service.
