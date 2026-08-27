---
id: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-versions-for-custom-resources-customresourcedefinition-storage-version
kind: section
title: Storage versions for custom resources {#CustomResourceDefinition-storage-version}
source: concepts/overview/working-with-objects/storage-version.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/
heading: Storage versions for custom resources {#CustomResourceDefinition-storage-version}
parent: okf-structure/concepts/overview/working-with-objects/storage-version
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#storage-version-to-resource-mapping
next_sibling: okf-structure/concepts/overview/working-with-objects/storage-version.md#how-storage-versions-are-relevant-to-encryption-at-rest
word_count: 398
---

Custom
resources are
defined dynamically, and as such differ from built in Kubernetes types with
their storage version. Builtin objects generally have their storage encoding
defined separately from their API types, where the stored object acts as a hub
and the specific version of the resource does not matter apart from being a
field in the object schema. 

However, for custom resources, a certain version of the resource must be set as
the storage version. The schema defined by that specific version of the custom
resource will be used as the encoding of the resource in the storage layer. See
the advanced CRD
featureset
for more detailed information on the API setup and versioning.

For example see this CustomResourceDefinition for _crontabs_:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.example.com
spec:
  group: example.com
  # list of versions supported by this CustomResourceDefinition
  versions:
  - name: v1beta1
    # Each version can be enabled/disabled by Served flag.
    served: true
    # One and only one version must be marked as the storage version.
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
  - name: v1
    served: true
    storage: false
    schema:
      openAPIV3Schema:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
          time:
            type: string
  conversion:
    strategy: None
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
```

The `v1beta1` API definition is used as the storage version, meaning that any
updates or creation of `crontabs` will be stored with the object schema of the
`v1beta1` api. In this case it actually would mean that the `v1` API object
would never be able to store the `time` field since it is not part of the
storage definition. This schema is used in the storage layer as the binary
encoding of the object itself. Trying to set two versions as the stored version
at the same time is considered invalid, since that would mean that two data
schemes would be considered valid ways to store the objects at the same time.

Upon modification of the version that is used for storage, that version of the
API will be used to store any new or update CRs. Watching or getting the object
will have the object be in use but will just convert the object from the old
storage version and not affect the object. Only updating or creating will have
an effect and use the newly defined storage version.
