---
id: okf-structure/tutorials/security/ns-level-pss.md#enable-pod-security-standards-checking-for-that-namespace
kind: section
title: Enable Pod Security Standards checking for that namespace
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: Enable Pod Security Standards checking for that namespace
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/ns-level-pss.md#create-a-namespace
next_sibling: okf-structure/tutorials/security/ns-level-pss.md#verify-the-pod-security-standard-enforcement
word_count: 110
---

1. Enable Pod Security Standards on this namespace using labels supported by
   built-in Pod Security Admission. In this step you will configure a check to
   warn on Pods that don't meet the latest version of the _baseline_ pod
   security standard.

   ```shell
   kubectl label --overwrite ns example \
      pod-security.kubernetes.io/warn=baseline \
      pod-security.kubernetes.io/warn-version=latest
   ```

2. You can configure multiple pod security standard checks on any namespace, using labels.
   The following command will `enforce` the `baseline` Pod Security Standard, but
   `warn` and `audit` for `restricted` Pod Security Standards as per the latest
   version (default value)

   ```shell
   kubectl label --overwrite ns example \
     pod-security.kubernetes.io/enforce=baseline \
     pod-security.kubernetes.io/enforce-version=latest \
     pod-security.kubernetes.io/warn=restricted \
     pod-security.kubernetes.io/warn-version=latest \
     pod-security.kubernetes.io/audit=restricted \
     pod-security.kubernetes.io/audit-version=latest
   ```
