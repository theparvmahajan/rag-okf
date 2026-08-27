---
id: okf-structure/concepts/scheduling-eviction/api-eviction.md#calling-the-eviction-api
kind: section
title: Calling the Eviction API
source: concepts/scheduling-eviction/api-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/
heading: Calling the Eviction API
parent: okf-structure/concepts/scheduling-eviction/api-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#how-api-initiated-eviction-works
word_count: 108
---

You can use a Kubernetes language client
to access the Kubernetes API and create an `Eviction` object. To do this, you
POST the attempted operation, similar to the following example:

`policy/v1` Eviction is available in v1.22+. Use `policy/v1beta1` with prior releases.

```json
{
  "apiVersion": "policy/v1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```

Deprecated in v1.22 in favor of `policy/v1`

```json
{
  "apiVersion": "policy/v1beta1",
  "kind": "Eviction",
  "metadata": {
    "name": "quux",
    "namespace": "default"
  }
}
```

Alternatively, you can attempt an eviction operation by accessing the API using
`curl` or `wget`, similar to the following example:

```bash
curl -v -H 'Content-type: application/json' https://your-cluster-api-endpoint.example/api/v1/namespaces/default/pods/quux/eviction -d @eviction.json
```
