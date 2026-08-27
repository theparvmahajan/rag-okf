---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#assign-role-to-service-accounts-to-use-specific-gmsa-credspecs
kind: section
title: Assign role to service accounts to use specific GMSA credspecs
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Assign role to service accounts to use specific GMSA credspecs
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-cluster-role-to-enable-rbac-on-specific-gmsa-credential-specs
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsa-credential-spec-reference-in-pod-spec
word_count: 80
---

A service account (that Pods will be configured with) needs to be bound to the
cluster role create above. This authorizes the service account to use the desired
GMSA credential spec resource. The following shows the default service account
being bound to a cluster role `webapp1-role` to use `gmsa-WebApp1` credential spec resource created above.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: allow-default-svc-account-read-on-gmsa-WebApp1
  namespace: default
subjects:
- kind: ServiceAccount
  name: default
  namespace: default
roleRef:
  kind: ClusterRole
  name: webapp1-role
  apiGroup: rbac.authorization.k8s.io
```
