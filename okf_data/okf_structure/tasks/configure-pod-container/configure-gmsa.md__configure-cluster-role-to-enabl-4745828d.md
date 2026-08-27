---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-cluster-role-to-enable-rbac-on-specific-gmsa-credential-specs
kind: section
title: Configure cluster role to enable RBAC on specific GMSA credential specs
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Configure cluster role to enable RBAC on specific GMSA credential specs
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#create-gmsa-credential-spec-resources
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#assign-role-to-service-accounts-to-use-specific-gmsa-credspecs
word_count: 88
---

A cluster role needs to be defined for each GMSA credential spec resource. This
authorizes the `use` verb on a specific GMSA resource by a subject which is typically
a service account. The following example shows a cluster role that authorizes usage
of the `gmsa-WebApp1` credential spec from above. Save the file as gmsa-webapp1-role.yaml
and apply using `kubectl apply -f gmsa-webapp1-role.yaml`

```yaml
# Create the Role to read the credspec
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: webapp1-role
rules:
- apiGroups: ["windows.k8s.io"]
  resources: ["gmsacredentialspecs"]
  verbs: ["use"]
  resourceNames: ["gmsa-WebApp1"]
```
