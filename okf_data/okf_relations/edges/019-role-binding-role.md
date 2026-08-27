---
id: okf-relations/edges/019-role-binding-role
kind: relation
subject: RoleBinding
predicate: grants
object: Role
subject_entity: okf-relations/entities/role-binding
object_entity: okf-relations/entities/role
grounding_sources:
- source: concepts/security/rbac-good-practices.md
  score: 88
  subject_hits: 5
  object_hits: 9
- source: concepts/security/service-accounts.md
  score: 55
  subject_hits: 1
  object_hits: 7
- source: tasks/configure-pod-container/migrate-from-psp.md
  score: 54
  subject_hits: 5
  object_hits: 13
source: concepts/security/rbac-good-practices.md
word_count: 22
---

RoleBinding grants Role. A RoleBinding attaches the permissions defined in a Role to specific subjects (users, groups, or ServiceAccounts) within one Namespace.
