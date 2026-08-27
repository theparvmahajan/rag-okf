---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#choosing-a-method-for-adding-custom-resources
kind: section
title: Choosing a method for adding custom resources
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Choosing a method for adding custom resources
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#api-server-aggregation
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#preparing-to-install-a-custom-resource
word_count: 987
---

CRDs are easier to use. Aggregated APIs are more flexible. Choose the method that best meets your needs.

Typically, CRDs are a good fit if:

* You have a handful of fields
* You are using the resource within your company, or as part of a small open-source project (as
  opposed to a commercial product)

### Comparing ease of use

CRDs are easier to create than Aggregated APIs.

| CRDs                        | Aggregated API |
| --------------------------- | -------------- |
| Do not require programming. Users can choose any language for a CRD controller. | Requires programming and building binary and image. |
| No additional service to run; CRDs are handled by API server. | An additional service to create and that could fail. |
| No ongoing support once the CRD is created. Any bug fixes are picked up as part of normal Kubernetes Master upgrades. | May need to periodically pickup bug fixes from upstream and rebuild and update the Aggregated API server. |
| No need to handle multiple versions of your API; for example, when you control the client for this resource, you can upgrade it in sync with the API. | You need to handle multiple versions of your API; for example, when developing an extension to share with the world. |

### Advanced features and flexibility

Aggregated APIs offer more advanced API features and customization of other features; for example, the storage layer.

| Feature | Description | CRDs | Aggregated API |
| ------- | ----------- | ---- | -------------- |
| Validation | Help users prevent errors and allow you to evolve your API independently of your clients. These features are most useful when there are many clients who can't all update at the same time. | Yes.  Most validation can be specified in the CRD using OpenAPI v3.0 validation. CRDValidationRatcheting feature gate allows failing validations specified using OpenAPI also can be ignored if the failing part of the resource was unchanged.  Any other validations supported by addition of a Validating Webhook. | Yes, arbitrary validation checks |
| Defaulting | See above | Yes, either via OpenAPI v3.0 validation `default` keyword (GA in 1.17), or via a Mutating Webhook (though this will not be run when reading from etcd for old objects). | Yes |
| Multi-versioning | Allows serving the same object through two API versions. Can help ease API changes like renaming fields. Less important if you control your client versions. | Yes | Yes |
| Custom Storage | If you need storage with a different performance mode (for example, a time-series database instead of key-value store) or isolation for security (for example, encryption of sensitive information, etc.) | No | Yes |
| Custom Business Logic | Perform arbitrary checks or actions when creating, reading, updating or deleting an object | Yes, using Webhooks. | Yes |
| Scale Subresource | Allows systems like HorizontalPodAutoscaler and PodDisruptionBudget interact with your new resource | Yes  | Yes |
| Status Subresource | Allows fine-grained access control where user writes the spec section and the controller writes the status section. Allows incrementing object Generation on custom resource data mutation (requires separate spec and status sections in the resource) | Yes | Yes |
| Other Subresources | Add operations other than CRUD, such as "logs" or "exec". | No | Yes |
| strategic-merge-patch | The new endpoints support PATCH with `Content-Type: application/strategic-merge-patch+json`. Useful for updating objects that may be modified both locally, and by the server. For more information, see "Update API Objects in Place Using kubectl patch" | No | Yes |
| Protocol Buffers | The new resource supports clients that want to use Protocol Buffers | No | Yes |
| OpenAPI Schema | Is there an OpenAPI (swagger) schema for the types that can be dynamically fetched from the server? Is the user protected from misspelling field names by ensuring only allowed fields are set? Are types enforced (in other words, don't put an `int` in a `string` field?) | Yes, based on the OpenAPI v3.0 validation schema (GA in 1.16). | Yes |
| Instance Name | Does this extension mechanism impose any constraints on the names of objects whose kind/resource is defined this way? | Yes, such an object's name must be a valid DNS subdomain name. | No |

### Common Features

When you create a custom resource, either via a CRD or an AA, you get many features for your API,
compared to implementing it outside the Kubernetes platform:

| Feature | What it does |
| ------- | ------------ |
| CRUD | The new endpoints support CRUD basic operations via HTTP and `kubectl` |
| Watch | The new endpoints support Kubernetes Watch operations via HTTP |
| Discovery | Clients like `kubectl` and dashboard automatically offer list, display, and field edit operations on your resources |
| json-patch | The new endpoints support PATCH with `Content-Type: application/json-patch+json` |
| merge-patch | The new endpoints support PATCH with `Content-Type: application/merge-patch+json` |
| HTTPS | The new endpoints uses HTTPS |
| Built-in Authentication | Access to the extension uses the core API server (aggregation layer) for authentication |
| Built-in Authorization | Access to the extension can reuse the authorization used by the core API server; for example, RBAC. |
| Finalizers | Block deletion of extension resources until external cleanup happens. |
| Admission Webhooks | Set default values and validate extension resources during any create/update/delete operation. |
| UI/CLI Display | Kubectl, dashboard can display extension resources. |
| Unset versus Empty | Clients can distinguish unset fields from zero-valued fields. |
| Client Libraries Generation | Kubernetes provides generic client libraries, as well as tools to generate type-specific client libraries. |
| Labels and annotations | Common metadata across objects that tools know how to edit for core and custom resources. |
