---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#read-metadata-in-your-application-read-metadata-application
kind: section
title: Read metadata in your application {#read-metadata-application}
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: Read metadata in your application {#read-metadata-application}
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaimtemplate-access-metadata-template
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#clean-up-clean-up
word_count: 127
---

### Go applications

The `k8s.io/dynamic-resource-allocation/devicemetadata` package provides
ready-made functions for reading metadata files. These functions handle
version negotiation automatically, decoding the metadata stream and converting
it to internal types so your code works across schema versions without manual
version checks.

For a directly referenced ResourceClaim:

```go
import "k8s.io/dynamic-resource-allocation/devicemetadata"

dm, err := devicemetadata.ReadResourceClaimMetadata("gpu-claim", "gpu")
```

For a template-generated claim (using the Pod's claim reference name):

```go
dm, err := devicemetadata.ReadResourceClaimTemplateMetadata("my-gpu", "gpu")
```

If you know the specific driver name, you can read a single driver's metadata
file:

```go
dm, err := devicemetadata.ReadResourceClaimMetadataWithDriverName("gpu.example.com", "gpu-claim", "gpu")
```

The returned `*metadata.DeviceMetadata` contains the claim metadata, requests,
and per-device attributes.

Applications in other languages can read the JSON file directly and inspect
the `apiVersion` field to determine the schema version before parsing.
