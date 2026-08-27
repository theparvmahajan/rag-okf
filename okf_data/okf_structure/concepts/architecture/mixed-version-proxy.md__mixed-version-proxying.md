---
id: okf-structure/concepts/architecture/mixed-version-proxy.md#mixed-version-proxying
kind: section
title: Mixed version proxying
source: concepts/architecture/mixed-version-proxy.md
url: https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/
heading: Mixed version proxying
parent: okf-structure/concepts/architecture/mixed-version-proxy
children: []
prev_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#peer-aggregated-discovery
next_sibling: null
word_count: 406
---

When you enable mixed version proxying, the aggregation layer
loads a special filter that does the following:

* When a resource request reaches an API server that cannot serve that API
  (either because it is at a version pre-dating the introduction of the API or the API is turned off on the API server)
  the API server attempts to send the request to a peer API server that can serve the requested API.
  It does so by identifying API groups / versions / resources that the local server doesn't recognise,
  and tries to proxy those requests to a peer API server that is capable of handling the request.
* If the peer API server fails to respond, the _source_ API server responds with 503 ("Service Unavailable") error.

### How it works under the hood

When an API Server receives a resource request, it first checks which API servers can
serve the requested resource. This check happens using the non peer-aggregated discovery document.

* If the resource is listed in the non peer-aggregated discovery document retrieved from the API server that received the request(for example, `GET /api/v1/pods/some-pod`), the request is handled locally.

* If the resource in a request (for example, `GET /apis/resource.k8s.io/v1beta1/resourceclaims`) is not found in the non peer-aggregated discovery document retrieved from the API server trying to handle the request (the _handling API server_), likely because the `resource.k8s.io/v1beta1` API was introduced in a newer Kubernetes version and the _handling API server_ is running an older version that does not support it, then the _handling API server_ fetches the peer API servers that do serve the relevant API group / version / resource (`resource.k8s.io/v1beta1/resourceclaims` in this case) by checking the non peer-aggregated discovery documents from all peer API servers. The _handling API server_ then proxies the request to one of the matching peer kube-apiservers that are aware of the requested resource.

* If there is no peer known for that API group / version / resource, the handling API server
passes the request to its own handler chain which should eventually return a 404 ("Not Found") response.

* If the handling API server has identified and selected a peer API server, but that peer fails
to respond (for reasons such as network connectivity issues, or a data race between the request
being received and a controller registering the peer's info into the control plane), then the handling
API server responds with a 503 ("Service Unavailable") error.
