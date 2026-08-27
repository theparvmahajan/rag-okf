---
id: okf-structure/concepts/security/rbac-good-practices.md#general-good-practice
kind: section
title: General good practice
source: concepts/security/rbac-good-practices.md
url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
heading: General good practice
parent: okf-structure/concepts/security/rbac-good-practices
children: []
prev_sibling: okf-structure/concepts/security/rbac-good-practices.md#introduction
next_sibling: okf-structure/concepts/security/rbac-good-practices.md#kubernetes-rbac-privilege-escalation-risks-privilege-escalation-risks
word_count: 501
---

### Least privilege

Ideally, minimal RBAC rights should be assigned to users and service accounts. Only permissions
explicitly required for their operation should be used. While each cluster will be different,
some general rules that can be applied are :

- Assign permissions at the namespace level where possible. Use RoleBindings as opposed to
  ClusterRoleBindings to give users rights only within a specific namespace.
- Avoid providing wildcard permissions when possible, especially to all resources.
  As Kubernetes is an extensible system, providing wildcard access gives rights
  not just to all object types that currently exist in the cluster, but also to all object types
  which are created in the future.
- Administrators should not use `cluster-admin` accounts except where specifically needed.
  Providing a low privileged account with
  impersonation rights
  can avoid accidental modification of cluster resources.
- Avoid adding users to the `system:masters` group. Any user who is a member of this group
  bypasses all RBAC rights checks and will always have unrestricted superuser access, which cannot be
  revoked by removing RoleBindings or ClusterRoleBindings. As an aside, if a cluster is
  using an authorization webhook, membership of this group also bypasses that webhook (requests
  from users who are members of that group are never sent to the webhook)

### Minimize distribution of privileged tokens

Ideally, pods shouldn't be assigned service accounts that have been granted powerful permissions
(for example, any of the rights listed under privilege escalation risks).
In cases where a workload requires powerful permissions, consider the following practices:

- Limit the number of nodes running powerful pods. Ensure that any DaemonSets you run
  are necessary and are run with least privilege to limit the blast radius of container escapes.
- Avoid running powerful pods alongside untrusted or publicly-exposed ones. Consider using
  Taints and Toleration,
  NodeAffinity, or
  PodAntiAffinity
  to ensure pods don't run alongside untrusted or less-trusted Pods. Pay special attention to
  situations where less-trustworthy Pods are not meeting the **Restricted** Pod Security Standard.

### Hardening

Kubernetes defaults to providing access which may not be required in every cluster. Reviewing
the RBAC rights provided by default can provide opportunities for security hardening.
In general, changes should not be made to rights provided to `system:` accounts some options
to harden cluster rights exist:

- Review bindings for the `system:unauthenticated` group and remove them where possible, as this gives 
  access to anyone who can contact the API server at a network level.
- Avoid the default auto-mounting of service account tokens by setting
  `automountServiceAccountToken: false`. For more details, see
  using default service account token.
  Setting this value for a Pod will overwrite the service account setting, workloads
  which require service account tokens can still mount them.

### Periodic review

It is vital to periodically review the Kubernetes RBAC settings for redundant entries and
possible privilege escalations.
If an attacker is able to create a user account with the same name as a deleted user,
they can automatically inherit all the rights of the deleted user, especially the
rights assigned to that user.
