---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaimtemplate-access-metadata-template
kind: section
title: Access device metadata with a ResourceClaimTemplate {#access-metadata-template}
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: Access device metadata with a ResourceClaimTemplate {#access-metadata-template}
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaim-access-metadata-resourceclaim
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#read-metadata-in-your-application-read-metadata-application
word_count: 123
---

When you use a ResourceClaimTemplate, Kubernetes generates a ResourceClaim for
each Pod. Because the generated claim name is not predictable, the metadata
files appear at a path that uses the Pod's claim reference name instead:

```
/var/run/kubernetes.io/dra-device-attributes/resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json
```

The `<podClaimName>` corresponds to the `name` field in the Pod's
`spec.resourceClaims[]` entry. The JSON metadata also includes a
`podClaimName` field that records this mapping.

1. Review the following example manifest:

   

   This manifest creates a ResourceClaimTemplate and a Pod. Each Pod gets its
   own generated ResourceClaim. The metadata path uses the Pod's claim
   reference name `my-gpu`.

1. Create the ResourceClaimTemplate and Pod:

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-device-metadata-template-pod.yaml
   ```

1. After the Pod is running, view the metadata:

   ```shell
   kubectl exec gpu-metadata-template-reader -- \
     cat /var/run/kubernetes.io/dra-device-attributes/resourceclaimtemplates/my-gpu/gpu/gpu.example.com-metadata.json
   ```
