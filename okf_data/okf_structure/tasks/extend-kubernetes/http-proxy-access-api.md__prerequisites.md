---
id: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#prerequisites
kind: section
title: Prerequisites
source: tasks/extend-kubernetes/http-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/
heading: Prerequisites
parent: okf-structure/tasks/extend-kubernetes/http-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#introduction
next_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#using-kubectl-to-start-a-proxy-server
word_count: 29
---

If you do not already have an application running in your cluster, start
a Hello world application by entering this command:

```shell
kubectl create deployment hello-app --image=gcr.io/google-samples/hello-app:2.0 --port=8080
```
