---
id: okf-structure/concepts/security/application-security-checklist.md#base-security-hardening
kind: section
title: Base security hardening
source: concepts/security/application-security-checklist.md
url: https://kubernetes.io/docs/concepts/security/application-security-checklist/
heading: Base security hardening
parent: okf-structure/concepts/security/application-security-checklist
children: []
prev_sibling: okf-structure/concepts/security/application-security-checklist.md#introduction
next_sibling: okf-structure/concepts/security/application-security-checklist.md#advanced-security-hardening-advanced
word_count: 488
---

The following checklist provides base security hardening recommendations that
would apply to most applications deploying to Kubernetes.

### Application design

- [ ] Follow the right
  security principles
  when designing applications.
- [ ] Application configured with appropriate QoS class
  through resource request and limits.
  - [ ] Memory limit is set for the workloads with a limit equal to or greater than the request.
  - [ ] CPU limit might be set on sensitive workloads.

### Service account

- [ ] Avoid using the `default` ServiceAccount. Instead, create ServiceAccounts for
  each workload or microservice.
- [ ] `automountServiceAccountToken` should be set to `false` unless the pod
  specifically requires access to the Kubernetes API to operate.

### Pod-level `securityContext` recommendations {#security-context-pod}

- [ ] Set `runAsNonRoot: true`.
- [ ] Configure the container to execute as a less privileged user
  (for example, using `runAsUser` and `runAsGroup`), and configure appropriate
  permissions on files or directories inside the container image.
- [ ] Optionally add a supplementary group with `fsGroup` to access persistent volumes.
- [ ] The application deploys into a namespace that enforces an appropriate
  Pod security standard.
  If you cannot control this enforcement for the cluster(s) where the application is
  deployed, take this into account either through documentation or additional defense in depth.

### Container-level `securityContext` recommendations {#security-context-container}

- [ ] Disable privilege escalations using `allowPrivilegeEscalation: false`.
- [ ] Configure the root filesystem to be read-only with `readOnlyRootFilesystem: true`.
- [ ] Avoid running privileged containers (set `privileged: false`).
- [ ] Drop all capabilities from the containers and add back only specific ones
  that are needed for operation of the container.

### Role Based Access Control (RBAC) {#rbac}

- [ ] Permissions such as **create**, **patch**, **update** and **delete**
  should be only granted if necessary.
- [ ] Avoid creating RBAC permissions to create or update roles which can lead to
  privilege escalation.
- [ ] Review bindings for the `system:unauthenticated` group and remove them where
  possible, as this gives access to anyone who can contact the API server at a network level.

The **create**, **update** and **delete** verbs should be permitted judiciously.
The **patch** verb if allowed on a Namespace can
allow users to update labels on the namespace or deployments
which can increase the attack surface.

For sensitive workloads, consider providing a recommended ValidatingAdmissionPolicy
that further restricts the permitted write actions.

### Image security

- [ ] Using an image scanning tool to scan an image before deploying containers in the Kubernetes cluster.
- [ ] Use container signing to validate the container image signature before deploying to the Kubernetes cluster.

### Network policies

- [ ] Configure NetworkPolicies
  to only allow expected ingress and egress traffic from the pods.

Make sure that your cluster provides and enforces NetworkPolicy.
If you are writing an application that users will deploy to different clusters,
consider whether you can assume that NetworkPolicy is available and enforced.
