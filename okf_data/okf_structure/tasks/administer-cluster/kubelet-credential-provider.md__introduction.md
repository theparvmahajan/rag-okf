---
id: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#introduction
kind: section
title: Configure a kubelet image credential provider
source: tasks/administer-cluster/kubelet-credential-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/
heading: null
parent: okf-structure/tasks/administer-cluster/kubelet-credential-provider
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#service-account-token-for-image-pulls
word_count: 151
---

Starting from Kubernetes v1.20, the kubelet can dynamically retrieve credentials for a container image registry
using exec plugins. The kubelet and the exec plugin communicate through stdio (stdin, stdout, and stderr) using
Kubernetes versioned APIs. These plugins allow the kubelet to request credentials for a container registry dynamically
as opposed to storing static credentials on disk. For example, the plugin may talk to a local metadata server to retrieve
short-lived credentials for an image that is being pulled by the kubelet.

You may be interested in using this capability if any of the below are true:

* API calls to a cloud provider service are required to retrieve authentication information for a registry.
* Credentials have short expiration times and requesting new credentials frequently is required.
* Storing registry credentials on disk or in imagePullSecrets is not acceptable.

This guide demonstrates how to configure the kubelet's image credential provider plugin mechanism.
