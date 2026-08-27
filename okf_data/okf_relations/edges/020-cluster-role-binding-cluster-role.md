---
id: okf-relations/edges/020-cluster-role-binding-cluster-role
kind: relation
subject: ClusterRoleBinding
predicate: grants
object: ClusterRole
subject_entity: okf-relations/entities/cluster-role-binding
object_entity: okf-relations/entities/cluster-role
grounding_sources:
- source: concepts/security/rbac-good-practices.md
  score: 61
  subject_hits: 2
  object_hits: 3
- source: tutorials/cluster-management/install-use-dra.md
  score: 39
  subject_hits: 4
  object_hits: 8
- source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
  score: 38
  subject_hits: 1
  object_hits: 3
source: concepts/security/rbac-good-practices.md
word_count: 20
---

ClusterRoleBinding grants ClusterRole. A ClusterRoleBinding attaches the permissions in a ClusterRole to subjects cluster-wide, rather than scoped to one Namespace.
