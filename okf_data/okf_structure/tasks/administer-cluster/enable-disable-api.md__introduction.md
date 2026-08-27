---
id: okf-structure/tasks/administer-cluster/enable-disable-api.md#introduction
kind: section
title: Enable Or Disable A Kubernetes API
source: tasks/administer-cluster/enable-disable-api.md
url: https://kubernetes.io/docs/tasks/administer-cluster/enable-disable-api/
heading: null
parent: okf-structure/tasks/administer-cluster/enable-disable-api
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/enable-disable-api.md#whatsnext
word_count: 101
---

This page shows how to enable or disable an API version from your cluster's
control plane.

Specific API versions can be turned on or off by passing `--runtime-config=api/<version>` as a
command line argument to the API server. The values for this argument are a comma-separated
list of API versions. Later values override earlier values.

The `runtime-config` command line argument also supports 2 special keys:

- `api/all`, representing all known APIs
- `api/legacy`, representing only legacy APIs. Legacy APIs are any APIs that have been
   explicitly deprecated.

For example, to turn off all API versions except v1, pass `--runtime-config=api/all=false,api/v1=true`
to the `kube-apiserver`.
