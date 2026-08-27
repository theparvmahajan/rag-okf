---
id: okf-structure/concepts/overview/kubernetes-api.md#api-groups-and-versioning
kind: section
title: API groups and versioning
source: concepts/overview/kubernetes-api.md
url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
heading: API groups and versioning
parent: okf-structure/concepts/overview/kubernetes-api
children: []
prev_sibling: okf-structure/concepts/overview/kubernetes-api.md#persistence
next_sibling: okf-structure/concepts/overview/kubernetes-api.md#api-extension
word_count: 491
---

To make it easier to eliminate fields or restructure resource representations,
Kubernetes supports multiple API versions, each at a different API path, such
as `/api/v1` or `/apis/rbac.authorization.k8s.io/v1alpha1`.

Versioning is done at the API level rather than at the resource or field level
to ensure that the API presents a clear, consistent view of system resources
and behavior, and to enable controlling access to end-of-life and/or
experimental APIs.

To make it easier to evolve and to extend its API, Kubernetes implements
API groups that can be
enabled or disabled.

API resources are distinguished by their API group, resource type, namespace
(for namespaced resources), and name. The API server handles the conversion between
API versions transparently: all the different versions are actually representations
of the same persisted data. The API server may serve the same underlying data
through multiple API versions.

For example, suppose there are two API versions, `v1` and `v1beta1`, for the same
resource. If you originally created an object using the `v1beta1` version of its
API, you can later read, update, or delete that object using either the `v1beta1`
or the `v1` API version, until the `v1beta1` version is deprecated and removed.
At that point you can continue accessing and modifying the object using the `v1` API.

### API changes

Any system that is successful needs to grow and change as new use cases emerge or existing ones change.
Therefore, Kubernetes has designed the Kubernetes API to continuously change and grow.
The Kubernetes project aims to _not_ break compatibility with existing clients, and to maintain that
compatibility for a length of time so that other projects have an opportunity to adapt.

In general, new API resources and new resource fields can be added often and frequently.
Elimination of resources or fields requires following the
API deprecation policy.

Kubernetes makes a strong commitment to maintain compatibility for official Kubernetes APIs
once they reach general availability (GA), typically at API version `v1`. Additionally,
Kubernetes maintains compatibility with data persisted via _beta_ API versions of official Kubernetes APIs,
and ensures that data can be converted and accessed via GA API versions when the feature goes stable.

If you adopt a beta API version, you will need to transition to a subsequent beta or stable API version
once the API graduates. The best time to do this is while the beta API is in its deprecation period,
since objects are simultaneously accessible via both API versions. Once the beta API completes its
deprecation period and is no longer served, the replacement API version must be used.

Although Kubernetes also aims to maintain compatibility for _alpha_ APIs versions, in some
circumstances this is not possible. If you use any alpha API versions, check the release notes
for Kubernetes when upgrading your cluster, in case the API did change in incompatible
ways that require deleting all existing alpha objects prior to upgrade.

Refer to API versions reference
for more details on the API version level definitions.
