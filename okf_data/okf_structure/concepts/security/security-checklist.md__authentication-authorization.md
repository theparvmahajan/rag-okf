---
id: okf-structure/concepts/security/security-checklist.md#authentication-authorization
kind: section
title: Authentication & Authorization
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Authentication & Authorization
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#introduction
next_sibling: okf-structure/concepts/security/security-checklist.md#network-security
word_count: 144
---

- [ ] `system:masters` group is not used for user or component authentication after bootstrapping.
- [ ] The kube-controller-manager is running with `--use-service-account-credentials`
  enabled.
- [ ] The root certificate is protected (either an offline CA, or a managed
  online CA with effective access controls).
- [ ] Intermediate and leaf certificates have an expiry date no more than 3
  years in the future.
- [ ] A process exists for periodic access review, and reviews occur no more
  than 24 months apart.
- [ ] The Role Based Access Control Good Practices
  are followed for guidance related to authentication and authorization.

After bootstrapping, neither users nor components should authenticate to the
Kubernetes API as `system:masters`. Similarly, running all of
kube-controller-manager as `system:masters` should be avoided. In fact,
`system:masters` should only be used as a break-glass mechanism, as opposed to
an admin user.
