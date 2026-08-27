---
id: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#service-account-token-for-image-pulls
kind: section
title: Service Account Token for Image Pulls
source: tasks/administer-cluster/kubelet-credential-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/
heading: Service Account Token for Image Pulls
parent: okf-structure/tasks/administer-cluster/kubelet-credential-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#prerequisites
word_count: 148
---

Starting from Kubernetes v1.33,
the kubelet can be configured to send a service account token
bound to the pod for which the image pull is being performed
to the credential provider plugin.

This allows the plugin to exchange the token for credentials
to access the image registry.

To enable this feature,
the `KubeletServiceAccountTokenForCredentialProviders` feature gate
must be enabled on the kubelet,
and the `tokenAttributes` field must be set
in the `CredentialProviderConfig` file for the plugin.

The `tokenAttributes` field contains information
about the service account token that will be passed to the plugin,
including the intended audience for the token
and whether the plugin requires the pod to have a service account.

Using service account token credentials can enable the following use-cases:

* Avoid needing a kubelet/node-based identity to pull images from a registry.
* Allow workloads to pull images based on their own runtime identity
without long-lived/persisted secrets.
