---
id: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#optional-enable-additional-dra-api-groups-enable-dra
kind: section
title: 'Optional: enable additional DRA API groups {#enable-dra}'
source: tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/
heading: 'Optional: enable additional DRA API groups {#enable-dra}'
parent: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#verify-that-dra-is-enabled-verify
word_count: 110
---

DRA overall is a stable feature in Kubernetes; however, aspects of it may still be alpha or beta.
If you want to use any aspect of DRA that is not yet stable,
and the associated feature relies on a dedicated API kind,
then you must enable the associated alpha or beta API groups.

Some older DRA drivers or workloads might still need the
v1beta1 API from Kubernetes 1.30 or v1beta2 from Kubernetes 1.32.
If and only if support for those is desired, then enable the following
API groups:

    * `resource.k8s.io/v1beta1`
    * `resource.k8s.io/v1beta2`

Alpha features with separate API types need:

   * `resource.k8s.io/v1alpha3`

For more information, see
Enabling or disabling API groups.
