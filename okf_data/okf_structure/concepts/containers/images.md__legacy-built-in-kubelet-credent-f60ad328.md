---
id: okf-structure/concepts/containers/images.md#legacy-built-in-kubelet-credential-provider
kind: section
title: Legacy built-in kubelet credential provider
source: concepts/containers/images.md
url: https://kubernetes.io/docs/concepts/containers/images/
heading: Legacy built-in kubelet credential provider
parent: okf-structure/concepts/containers/images
children: []
prev_sibling: okf-structure/concepts/containers/images.md#using-a-private-registry
next_sibling: okf-structure/concepts/containers/images.md#whatsnext
word_count: 91
---

In older versions of Kubernetes, the kubelet had a direct integration with cloud
provider credentials. This provided the ability to dynamically fetch credentials
for image registries.

There were three built-in implementations of the kubelet credential provider
integration: ACR (Azure Container Registry), ECR (Elastic Container Registry),
and GCR (Google Container Registry).

Starting with version 1.26 of Kubernetes, the legacy mechanism has been removed,
so you would need to either:
- configure a kubelet image credential provider on each node; or
- specify image pull credentials using `imagePullSecrets` and at least one Secret.
