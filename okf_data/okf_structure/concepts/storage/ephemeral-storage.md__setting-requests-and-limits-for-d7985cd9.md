---
id: okf-structure/concepts/storage/ephemeral-storage.md#setting-requests-and-limits-for-local-ephemeral-storage-requests-limits
kind: section
title: Setting requests and limits for local ephemeral storage {#requests-limits}
source: concepts/storage/ephemeral-storage.md
url: https://kubernetes.io/docs/concepts/storage/ephemeral-storage/
heading: Setting requests and limits for local ephemeral storage {#requests-limits}
parent: okf-structure/concepts/storage/ephemeral-storage
children: []
prev_sibling: okf-structure/concepts/storage/ephemeral-storage.md#configurations-for-local-ephemeral-storage-configurations
next_sibling: okf-structure/concepts/storage/ephemeral-storage.md#how-pods-with-ephemeral-storage-requests-are-scheduled
word_count: 246
---

You can specify `ephemeral-storage` for managing local ephemeral storage. Each
container of a Pod can specify either or both of the following:

* `spec.containers[].resources.limits.ephemeral-storage`
* `spec.containers[].resources.requests.ephemeral-storage`

Limits and requests for `ephemeral-storage` are measured in byte quantities.
You can express storage as a plain integer or as a fixed-point number using one of these suffixes:
E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi,
Mi, Ki. For example, the following quantities all represent roughly the same value:

- `128974848`
- `129e6`
- `129M`
- `123Mi`

Pay attention to the case of the suffixes. If you request `400m` of ephemeral-storage, this is a request
for 0.4 bytes. Someone who types that probably meant to ask for 400 mebibytes (`400Mi`)
or 400 megabytes (`400M`).

In the following example, the Pod has two containers. Each container has a request of
2GiB of local ephemeral storage. Each container has a limit of 4GiB of local ephemeral
storage. Therefore, the Pod has a request of 4GiB of local ephemeral storage, and
a limit of 8GiB of local ephemeral storage. 500Mi of that limit could be
consumed by the `emptyDir` volume.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  volumes:
    - name: ephemeral
      emptyDir:
        sizeLimit: 500Mi
```
