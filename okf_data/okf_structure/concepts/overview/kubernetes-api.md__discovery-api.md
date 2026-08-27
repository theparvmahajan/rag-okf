---
id: okf-structure/concepts/overview/kubernetes-api.md#discovery-api
kind: section
title: Discovery API
source: concepts/overview/kubernetes-api.md
url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
heading: Discovery API
parent: okf-structure/concepts/overview/kubernetes-api
children: []
prev_sibling: okf-structure/concepts/overview/kubernetes-api.md#introduction
next_sibling: okf-structure/concepts/overview/kubernetes-api.md#openapi-interface-definition
word_count: 341
---

Kubernetes publishes a list of all group versions and resources supported via
the Discovery API. This includes the following for each resource:

- Name
- Cluster or namespaced scope
- Endpoint URL and supported verbs
- Alternative names
- Group, version, kind

The API is available in both aggregated and unaggregated form. The aggregated
discovery serves two endpoints, while the unaggregated discovery serves a
separate endpoint for each group version.

### Aggregated discovery

Kubernetes offers stable support for _aggregated discovery_, publishing
all resources supported by a cluster through two endpoints (`/api` and
`/apis`). Requesting this
endpoint drastically reduces the number of requests sent to fetch the
discovery data from the cluster. You can access the data by
requesting the respective endpoints with an `Accept` header indicating
the aggregated discovery resource:
`Accept: application/json;v=v2;g=apidiscovery.k8s.io;as=APIGroupDiscoveryList`.

Without indicating the resource type using the `Accept` header, the default
response for the `/api` and `/apis` endpoint is an unaggregated discovery
document.

The discovery document
for the built-in resources can be found in the Kubernetes GitHub repository.
This Github document can be used as a reference of the base set of the available resources
if a Kubernetes cluster is not available to query.

The endpoint also supports ETag and protobuf encoding.

### Unaggregated discovery

Without discovery aggregation, discovery is published in levels, with the root
endpoints publishing discovery information for downstream documents.

A list of all group versions supported by a cluster is published at
the `/api` and `/apis` endpoints. Example:

```
{
  "kind": "APIGroupList",
  "apiVersion": "v1",
  "groups": [
    {
      "name": "apiregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "apiregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apps",
      "versions": [
        {
          "groupVersion": "apps/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apps/v1",
        "version": "v1"
      }
    },
    ...
}
```

Additional requests are needed to obtain the discovery document for each group version at
`/apis/<group>/<version>` (for example:
`/apis/rbac.authorization.k8s.io/v1alpha1`), which advertises the list of
resources served under a particular group version. These endpoints are used by
kubectl to fetch the list of resources supported by a cluster.
