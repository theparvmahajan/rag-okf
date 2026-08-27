---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaim-access-metadata-resourceclaim
kind: section
title: Access device metadata with a ResourceClaim {#access-metadata-resourceclaim}
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: Access device metadata with a ResourceClaim {#access-metadata-resourceclaim}
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaimtemplate-access-metadata-template
word_count: 148
---

When you use a directly referenced ResourceClaim to allocate devices, the
device metadata files appear inside the container at:

```
/var/run/kubernetes.io/dra-device-attributes/resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json
```

1. Review the following example manifest:

   

   This manifest creates a ResourceClaim named `gpu-claim` that requests a
   device from the `gpu.example.com` DeviceClass, and a Pod that reads the
   device metadata.

1. Create the ResourceClaim and Pod:

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-device-metadata-pod.yaml
   ```

1. After the Pod is running, view the container logs to see the metadata:

   ```shell
   kubectl logs gpu-metadata-reader
   ```

   The output is similar to:

   ```
   === DRA device metadata ===
   /var/run/kubernetes.io/dra-device-attributes/resourceclaims/gpu-claim/gpu/gpu.example.com-metadata.json
   {
     "kind": "DeviceMetadata",
     "apiVersion": "metadata.resource.k8s.io/v1alpha1",
     ...
   }
   ```

1. To inspect the full metadata file, exec into the container:

   ```shell
   kubectl exec gpu-metadata-reader -- \
     cat /var/run/kubernetes.io/dra-device-attributes/resourceclaims/gpu-claim/gpu/gpu.example.com-metadata.json
   ```

   The output is a JSON object containing device attributes like the model,
   driver version, and device UUID. See
   metadata schema
   for details on the JSON structure.
