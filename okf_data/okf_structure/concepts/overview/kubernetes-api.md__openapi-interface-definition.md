---
id: okf-structure/concepts/overview/kubernetes-api.md#openapi-interface-definition
kind: section
title: OpenAPI interface definition
source: concepts/overview/kubernetes-api.md
url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
heading: OpenAPI interface definition
parent: okf-structure/concepts/overview/kubernetes-api
children: []
prev_sibling: okf-structure/concepts/overview/kubernetes-api.md#discovery-api
next_sibling: okf-structure/concepts/overview/kubernetes-api.md#persistence
word_count: 425
---

For details about the OpenAPI specifications, see the OpenAPI documentation.

Kubernetes serves both OpenAPI v2.0 and OpenAPI v3.0. OpenAPI v3 is the
preferred method of accessing the OpenAPI because it offers a more comprehensive
(lossless) representation of Kubernetes resources. Due to limitations of OpenAPI
version 2, certain fields are dropped from the published OpenAPI including but not
limited to `default`, `nullable`, `oneOf`.
### OpenAPI V2

The Kubernetes API server serves an aggregated OpenAPI v2 spec via the
`/openapi/v2` endpoint. You can request the response format using
request headers as follows:

  <caption style="display:none">Valid request header values for OpenAPI v2 queries</caption>
  
     
        Header
        Possible values
        Notes
     
  
  
     
        <code>Accept-Encoding</code>
        <code>gzip</code>
        not supplying this header is also acceptable
     
     
        <code>Accept</code>
        <code>application/com.github.proto-openapi.spec.v2@v1.0+protobuf</code>
        mainly for intra-cluster use
     
     
        <code>application/json</code>
        default
     
     
        <code>*</code>
        serves <code>application/json</code>
     
  

The validation rules published as part of OpenAPI schemas may not be complete, and usually aren't.
Additional validation occurs within the API server. If you want precise and complete verification,
a `kubectl apply --dry-run=server` runs all the applicable validation (and also activates admission-time
checks).

### OpenAPI V3

Kubernetes supports publishing a description of its APIs as OpenAPI v3.

A discovery endpoint `/openapi/v3` is provided to see a list of all
group/versions available. This endpoint only returns JSON. These
group/versions are provided in the following format:

```yaml
{
    "paths": {
        ...,
        "api/v1": {
            "serverRelativeURL": "/openapi/v3/api/v1?hash=CC0E9BFD992D8C59AEC98A1E2336F899E8318D3CF4C68944C3DEC640AF5AB52D864AC50DAA8D145B3494F75FA3CFF939FCBDDA431DAD3CA79738B297795818CF"
        },
        "apis/admissionregistration.k8s.io/v1": {
            "serverRelativeURL": "/openapi/v3/apis/admissionregistration.k8s.io/v1?hash=E19CC93A116982CE5422FC42B590A8AFAD92CDE9AE4D59B5CAAD568F083AD07946E6CB5817531680BCE6E215C16973CD39003B0425F3477CFD854E89A9DB6597"
        },
        ....
    }
}
```

The relative URLs are pointing to immutable OpenAPI descriptions, in
order to improve client-side caching. The proper HTTP caching headers
are also set by the API server for that purpose (`Expires` to 1 year in
the future, and `Cache-Control` to `immutable`). When an obsolete URL is
used, the API server returns a redirect to the newest URL.

The Kubernetes API server publishes an OpenAPI v3 spec per Kubernetes
group version at the `/openapi/v3/apis/<group>/<version>?hash=<hash>`
endpoint.

Refer to the table below for accepted request headers.

  <caption style="display:none">Valid request header values for OpenAPI v3 queries</caption>
  
     
        Header
        Possible values
        Notes
     
  
  
     
        <code>Accept-Encoding</code>
        <code>gzip</code>
        not supplying this header is also acceptable
     
     
        <code>Accept</code>
        <code>application/com.github.proto-openapi.spec.v3@v1.0+protobuf</code>
        mainly for intra-cluster use
     
     
        <code>application/json</code>
        default
     
     
        <code>*</code>
        serves <code>application/json</code>
     
  

A Golang implementation to fetch the OpenAPI V3 is provided in the package
`k8s.io/client-go/openapi3`.

Kubernetes  publishes
OpenAPI v2.0 and v3.0; there are no plans to support 3.1 in the near future.

### Protobuf serialization

Kubernetes implements an alternative Protobuf based serialization format that
is primarily intended for intra-cluster communication. For more information
about this format, see the Kubernetes Protobuf serialization
design proposal and the
Interface Definition Language (IDL) files for each schema located in the Go
packages that define the API objects.
