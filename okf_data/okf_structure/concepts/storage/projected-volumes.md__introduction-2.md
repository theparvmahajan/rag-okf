---
id: okf-structure/concepts/storage/projected-volumes.md#introduction-2
kind: section
title: Introduction
source: concepts/storage/projected-volumes.md
url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
heading: Introduction
parent: okf-structure/concepts/storage/projected-volumes
children: []
prev_sibling: okf-structure/concepts/storage/projected-volumes.md#introduction
next_sibling: okf-structure/concepts/storage/projected-volumes.md#serviceaccounttoken-projected-volumes-serviceaccounttoken
word_count: 147
---

A `projected` volume maps several existing volume sources into the same directory.

Currently, the following types of volume sources can be projected:

* `secret`
* `downwardAPI`
* `configMap`
* `serviceAccountToken`
* `clusterTrustBundle`
* `podCertificate`

All sources are required to be in the same namespace as the Pod. For more details,
see the all-in-one volume design document.

### Example configuration with a secret, a downwardAPI, and a configMap {#example-configuration-secret-downwardapi-configmap}

### Example configuration: secrets with a non-default permission mode set {#example-configuration-secrets-nondefault-permission-mode}

Each projected volume source is listed in the spec under `sources`. The
parameters are nearly the same with two exceptions:

* For secrets, the `secretName` field has been changed to `name` to be consistent
  with ConfigMap naming.
* The `defaultMode` can only be specified at the projected level and not for each
  volume source. However, as illustrated above, you can explicitly set the `mode`
  for each individual projection.
