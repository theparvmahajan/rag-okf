---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-beta-features-beta-features
kind: section
title: DRA beta features {#beta-features}
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: DRA beta features {#beta-features}
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#limitations
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-alpha-features-alpha-features
word_count: 258
---

The following sections describe DRA features that support advanced use
cases. Usage of them is optional and may only be relevant with DRA
drivers that support them.

Some of them are available in the Alpha or Beta
feature stage.
Those depend on feature gates and may depend on additional
API groups.
For more information, see
Set up DRA in the cluster.

### Admin access {#admin-access}

You can mark a request in a ResourceClaim or ResourceClaimTemplate as having
privileged features for maintenance and troubleshooting tasks. A request with
admin access grants access to in-use devices and may enable additional
permissions when making the device available in a container:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: large-black-cat-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          allocationMode: All
          adminAccess: true
```

Admin access is a privileged mode and should not be granted to regular users in
multi-tenant clusters. Only users authorized to
create ResourceClaim or ResourceClaimTemplate objects in namespaces labeled with
`resource.kubernetes.io/admin-access: "true"` (case-sensitive) can use the
`adminAccess` field. This ensures that non-admin users cannot misuse the
feature.

Admin access is a *beta feature* and is enabled by default with the
`DRAAdminAccess` feature gate
in the kube-apiserver, kube-scheduler, and kubelet.

### Granular status authorization {#granular-status-authorization}

Starting in Kubernetes v1.36, DRA enforces fine-grained authorization checks for updates
to `ResourceClaim` status by using synthetic subresources and node-aware verbs.

For security hardening guidance, including RBAC examples for scheduler and DRA
drivers, see
Hardening Guide - Dynamic Resource Allocation.

For a step-by-step cluster administrator procedure, see
Harden Dynamic Resource Allocation in Your Cluster.
