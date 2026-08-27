---
id: okf-structure/concepts/security/service-accounts.md#use-cases-for-kubernetes-service-accounts-use-cases
kind: section
title: Use cases for Kubernetes service accounts {#use-cases}
source: concepts/security/service-accounts.md
url: https://kubernetes.io/docs/concepts/security/service-accounts/
heading: Use cases for Kubernetes service accounts {#use-cases}
parent: okf-structure/concepts/security/service-accounts
children: []
prev_sibling: okf-structure/concepts/security/service-accounts.md#what-are-service-accounts-what-are-service-accounts
next_sibling: okf-structure/concepts/security/service-accounts.md#how-to-use-service-accounts-how-to-use
word_count: 162
---

As a general guideline, you can use service accounts to provide identities in
the following scenarios:

* Your Pods need to communicate with the Kubernetes API server, for example in
  situations such as the following:
  * Providing read-only access to sensitive information stored in Secrets.
  * Granting cross-namespace access, such as allowing a
    Pod in namespace `example` to read, list, and watch for Lease objects in
    the `kube-node-lease` namespace.
* Your Pods need to communicate with an external service. For example, a
  workload Pod requires an identity for a commercially available cloud API,
  and the commercial provider allows configuring a suitable trust relationship.
* Authenticating to a private image registry using an `imagePullSecret`.
* An external service needs to communicate with the Kubernetes API server. For
  example, authenticating to the cluster as part of a CI/CD pipeline.
* You use third-party security software in your cluster that relies on the
  ServiceAccount identity of different Pods to group those Pods into different
  contexts.
