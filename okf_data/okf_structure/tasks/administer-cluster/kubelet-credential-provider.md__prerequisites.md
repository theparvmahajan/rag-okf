---
id: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubelet-credential-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubelet-credential-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#service-account-token-for-image-pulls
next_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#installing-plugins-on-nodes
word_count: 93
---

* You need a Kubernetes cluster with nodes that support kubelet credential
  provider plugins. This support is available in Kubernetes ;
  Kubernetes v1.24 and v1.25 included this as a beta feature, enabled by default.
* If you are configuring a credential provider plugin
that requires the service account token,
you need a Kubernetes cluster with nodes running Kubernetes v1.33 or later
and the `KubeletServiceAccountTokenForCredentialProviders` feature gate
enabled on the kubelet.
* A working implementation of a credential provider exec plugin. You can build your own plugin or use one provided by cloud providers.
