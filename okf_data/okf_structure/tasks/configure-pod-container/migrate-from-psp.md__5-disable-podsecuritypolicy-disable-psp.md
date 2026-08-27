---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#5-disable-podsecuritypolicy-disable-psp
kind: section
title: 5. Disable PodSecurityPolicy {#disable-psp}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 5. Disable PodSecurityPolicy {#disable-psp}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#4-review-namespace-creation-processes-review-namespace-creation-process
next_sibling: null
word_count: 177
---

Finally, you're ready to disable PodSecurityPolicy. To do so, you will need to modify the admission
configuration of the API server:
How do I turn off an admission controller?.

To verify that the PodSecurityPolicy admission controller is no longer enabled, you can manually run
a test by impersonating a user without access to any PodSecurityPolicies (see the
PodSecurityPolicy example), or by verifying in
the API server logs. At startup, the API server outputs log lines listing the loaded admission
controller plugins:

```
I0218 00:59:44.903329      13 plugins.go:158] Loaded 16 mutating admission controller(s) successfully in the following order: NamespaceLifecycle,LimitRanger,ServiceAccount,NodeRestriction,TaintNodesByCondition,Priority,DefaultTolerationSeconds,ExtendedResourceToleration,PersistentVolumeLabel,DefaultStorageClass,StorageObjectInUseProtection,RuntimeClass,DefaultIngressClass,MutatingAdmissionWebhook.
I0218 00:59:44.903350      13 plugins.go:161] Loaded 14 validating admission controller(s) successfully in the following order: LimitRanger,ServiceAccount,PodSecurity,Priority,PersistentVolumeClaimResize,RuntimeClass,CertificateApproval,CertificateSigning,CertificateSubjectRestriction,DenyServiceExternalIPs,ValidatingAdmissionWebhook,ResourceQuota.
```

You should see `PodSecurity` (in the validating admission controllers), and neither list should
contain `PodSecurityPolicy`.

Once you are certain the PSP admission controller is disabled (and after sufficient soak time to be
confident you won't need to roll back), you are free to delete your PodSecurityPolicies and any
associated Roles, ClusterRoles, RoleBindings and ClusterRoleBindings (just make sure they don't
grant any other unrelated permissions).
