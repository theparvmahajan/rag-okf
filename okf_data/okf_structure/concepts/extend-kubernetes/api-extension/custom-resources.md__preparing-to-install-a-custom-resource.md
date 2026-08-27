---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#preparing-to-install-a-custom-resource
kind: section
title: Preparing to install a custom resource
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Preparing to install a custom resource
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#choosing-a-method-for-adding-custom-resources
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#accessing-a-custom-resource
word_count: 290
---

There are several points to be aware of before adding a custom resource to your cluster.

### Third party code and new points of failure

While creating a CRD does not automatically add any new points of failure (for example, by causing
third party code to run on your API server), packages (for example, Charts) or other installation
bundles often include CRDs as well as a Deployment of third-party code that implements the
business logic for a new custom resource.

Installing an Aggregated API server always involves running a new Deployment.

### Storage

Custom resources consume storage space in the same way that ConfigMaps do. Creating too many
custom resources may overload your API server's storage space.

Custom resources are placed into storage based upon the the current storage
version of the resource, defined in the CRD spec. Any update to a custom
resource will use the currently defined storage version to store the resource.
All other versions either need to have all the fields of that version or define
conversions to work properly.

Aggregated API servers may use the same storage as the main API server, in which case the same
warning applies.

### Authentication, authorization, and auditing

CRDs always use the same authentication, authorization, and audit logging as the built-in
resources of your API server.

If you use RBAC for authorization, most RBAC roles will not grant access to the new resources
(except the cluster-admin role or any role created with wildcard rules). You'll need to explicitly
grant access to the new resources. CRDs and Aggregated APIs often come bundled with new role
definitions for the types they add.

Aggregated API servers may or may not use the same authentication, authorization, and auditing as
the primary API server.
