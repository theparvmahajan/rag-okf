---
id: okf-structure/concepts/storage/projected-volumes.md#clustertrustbundle-projected-volumes-clustertrustbundle
kind: section
title: clusterTrustBundle projected volumes {#clustertrustbundle}
source: concepts/storage/projected-volumes.md
url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
heading: clusterTrustBundle projected volumes {#clustertrustbundle}
parent: okf-structure/concepts/storage/projected-volumes
children: []
prev_sibling: okf-structure/concepts/storage/projected-volumes.md#serviceaccounttoken-projected-volumes-serviceaccounttoken
next_sibling: okf-structure/concepts/storage/projected-volumes.md#podcertificate-projected-volumes-podcertificate
word_count: 215
---

To use this feature in Kubernetes , you must enable support for ClusterTrustBundle objects
with the `ClusterTrustBundle` feature gate and
`--runtime-config=certificates.k8s.io/v1beta1/clustertrustbundles=true` kube-apiserver flag,
then enable the `ClusterTrustBundleProjection` feature gate.

The `clusterTrustBundle` projected volume source injects the contents of one or more
ClusterTrustBundle
objects as an automatically-updating file in the container filesystem.

ClusterTrustBundles can be selected either by name
or by signer name.

To select by name, use the `name` field to designate a single ClusterTrustBundle object.

To select by signer name, use the `signerName` field (and optionally the
`labelSelector` field) to designate a set of ClusterTrustBundle objects that use
the given signer name. If `labelSelector` is not present, then all
ClusterTrustBundles for that signer are selected.

The kubelet deduplicates the certificates in the selected ClusterTrustBundle objects,
normalizes the PEM representations (discarding comments and headers), reorders the certificates,
and writes them into the file named by `path`.
As the set of selected ClusterTrustBundles or their content changes, kubelet keeps the file up-to-date.

By default, the kubelet will prevent the pod from starting if the named ClusterTrustBundle is not found,
or if `signerName` / `labelSelector` do not match any ClusterTrustBundles.
If this behavior is not what you want, then set the `optional` field to `true`,
and the pod will start up with an empty file at `path`.
