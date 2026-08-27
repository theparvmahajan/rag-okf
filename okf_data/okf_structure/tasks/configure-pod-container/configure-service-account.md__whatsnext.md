---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#whatsnext
kind: section
title: Whatsnext
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: Whatsnext
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#serviceaccount-token-volume-projection
next_sibling: null
word_count: 80
---

See also:

- Read the Cluster Admin Guide to Service Accounts
- Read about Authorization in Kubernetes
- Read about Secrets
  - or learn to distribute credentials securely using Secrets
  - but also bear in mind that using Secrets for authenticating as a ServiceAccount
    is deprecated. The recommended alternative is
    ServiceAccount token volume projection.
- Read about projected volumes.
- For background on OIDC discovery, read the
  ServiceAccount signing key retrieval
  Kubernetes Enhancement Proposal
- Read the OIDC Discovery Spec
