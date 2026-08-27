---
id: okf-structure/concepts/security/rbac-good-practices.md#kubernetes-rbac-denial-of-service-risks-denial-of-service-risks
kind: section
title: Kubernetes RBAC - denial of service risks {#denial-of-service-risks}
source: concepts/security/rbac-good-practices.md
url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
heading: Kubernetes RBAC - denial of service risks {#denial-of-service-risks}
parent: okf-structure/concepts/security/rbac-good-practices
children: []
prev_sibling: okf-structure/concepts/security/rbac-good-practices.md#kubernetes-rbac-privilege-escalation-risks-privilege-escalation-risks
next_sibling: okf-structure/concepts/security/rbac-good-practices.md#whatsnext
word_count: 94
---

### Object creation denial-of-service {#object-creation-dos}

Users who have rights to create objects in a cluster may be able to create sufficient large 
objects to create a denial of service condition either based on the size or number of objects, as discussed in
etcd used by Kubernetes is vulnerable to OOM attack. This may be
specifically relevant in multi-tenant clusters if semi-trusted or untrusted users 
are allowed limited access to a system.

One option for mitigation of this issue would be to use
resource quotas
to limit the quantity of objects which can be created.
