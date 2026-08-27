---
id: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md#aggregation-layer
kind: section
title: Aggregation layer
source: concepts/extend-kubernetes/api-extension/apiserver-aggregation.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
heading: Aggregation layer
parent: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/apiserver-aggregation.md#whatsnext
word_count: 172
---

The aggregation layer runs in-process with the kube-apiserver. Until an extension resource is
registered, the aggregation layer will do nothing. To register an API, you add an _APIService_
object, which "claims" the URL path in the Kubernetes API. At that point, the aggregation layer
will proxy anything sent to that API path (e.g. `/apis/myextension.mycompany.io/v1/…`) to the
registered APIService.

The most common way to implement the APIService is to run an *extension API server* in Pod(s) that
run in your cluster. If you're using the extension API server to manage resources in your cluster,
the extension API server (also written as "extension-apiserver") is typically paired with one or
more controllers. The apiserver-builder
library provides a skeleton for both extension API servers and the associated controller(s).

### Response latency

Extension API servers should have low latency networking to and from the kube-apiserver.
Discovery requests are required to round-trip from the kube-apiserver in five seconds or less.

If your extension API server cannot achieve that latency requirement, consider making changes that
let you meet it.
