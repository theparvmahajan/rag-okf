---
id: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#exploring-the-kubernetes-api
kind: section
title: Exploring the Kubernetes API
source: tasks/extend-kubernetes/http-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/http-proxy-access-api/
heading: Exploring the Kubernetes API
parent: okf-structure/tasks/extend-kubernetes/http-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#using-kubectl-to-start-a-proxy-server
next_sibling: okf-structure/tasks/extend-kubernetes/http-proxy-access-api.md#whatsnext
word_count: 96
---

When the proxy server is running, you can explore the API using `curl`, `wget`,
or a browser.

Get the API versions:

    curl http://localhost:8080/api/

The output should look similar to this:

    {
      "kind": "APIVersions",
      "versions": [
        "v1"
      ],
      "serverAddressByClientCIDRs": [
        {
          "clientCIDR": "0.0.0.0/0",
          "serverAddress": "10.0.2.15:8443"
        }
      ]
    }

Get a list of pods:

    curl http://localhost:8080/api/v1/namespaces/default/pods

The output should look similar to this:

    {
      "kind": "PodList",
      "apiVersion": "v1",
      "metadata": {
        "resourceVersion": "33074"
      },
      "items": 
        {
          "metadata": {
            "name": "kubernetes-bootcamp-2321272333-ix8pt",
            "generateName": "kubernetes-bootcamp-2321272333-",
            "namespace": "default",
            "uid": "ba21457c-6b1d-11e6-85f7-1ef9f1dab92b",
            "resourceVersion": "33003",
            "creationTimestamp": "2016-08-25T23:43:30Z",
            "labels": {
              "pod-template-hash": "2321272333",
              "run": "kubernetes-bootcamp"
            },
            ...
    }
