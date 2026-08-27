---
id: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#using-kubectl-to-start-a-proxy-server
kind: section
title: Using kubectl to start a proxy server
source: tasks/extend-kubernetes/http-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/
heading: Using kubectl to start a proxy server
parent: okf-structure/tasks/extend-kubernetes/http-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#exploring-the-kubernetes-api
word_count: 13
---

This command starts a proxy to the Kubernetes API server:

    kubectl proxy --port=8080
