---
id: okf-structure/tutorials/security/ns-level-pss.md#verify-the-pod-security-standard-enforcement
kind: section
title: Verify the Pod Security Standard enforcement
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: Verify the Pod Security Standard enforcement
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/ns-level-pss.md#enable-pod-security-standards-checking-for-that-namespace
next_sibling: okf-structure/tutorials/security/ns-level-pss.md#clean-up
word_count: 129
---

1. Create a baseline Pod in the `example` namespace:

   ```shell
   kubectl apply -n example -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```
   The Pod does start OK; the output includes a warning. For example:

   ```
   Warning: would violate PodSecurity "restricted:latest": allowPrivilegeEscalation != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
   pod/nginx created
   ```

1. Create a baseline Pod in the `default` namespace:

   ```shell
   kubectl apply -n default -f https://k8s.io/examples/security/example-baseline-pod.yaml
   ```
   Output is similar to this:

   ```
   pod/nginx created
   ```

The Pod Security Standards enforcement and warning settings were applied only
to the `example` namespace. You could create the same Pod in the `default`
namespace with no warnings.
