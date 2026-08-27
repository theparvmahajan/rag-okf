---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#2-simplify-standardize-podsecuritypolicies-simplify-psps
kind: section
title: 2. Simplify & standardize PodSecurityPolicies {#simplify-psps}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 2. Simplify & standardize PodSecurityPolicies {#simplify-psps}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#1-review-namespace-permissions-review-namespace-permissions
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#3-update-namespaces-update-namespaces
word_count: 797
---

In this section, you will reduce mutating PodSecurityPolicies and remove options that are outside
the scope of the Pod Security Standards. You should make the changes recommended here to an offline
copy of the original PodSecurityPolicy being modified. The cloned PSP should have a different
name that is alphabetically before the original (for example, prepend a `0` to it). Do not create the
new policies in Kubernetes yet - that will be covered in the Rollout the updated
policies section below.

### 2.a. Eliminate purely mutating fields {#eliminate-mutating-fields}

If a PodSecurityPolicy is mutating pods, then you could end up with pods that don't meet the Pod
Security level requirements when you finally turn PodSecurityPolicy off. In order to avoid this, you
should eliminate all PSP mutation prior to switching over. Unfortunately PSP does not cleanly
separate mutating & validating fields, so this is not a straightforward migration.

You can start by eliminating the fields that are purely mutating, and don't have any bearing on the
validating policy. These fields (also listed in the
Mapping PodSecurityPolicies to Pod Security Standards
reference) are:

- `.spec.defaultAllowPrivilegeEscalation`
- `.spec.runtimeClass.defaultRuntimeClassName`
- `.metadata.annotations['seccomp.security.alpha.kubernetes.io/defaultProfileName']`
- `.metadata.annotations['apparmor.security.beta.kubernetes.io/defaultProfileName']`
- `.spec.defaultAddCapabilities` - Although technically a mutating & validating field, these should
  be merged into `.spec.allowedCapabilities` which performs the same validation without mutation.

Removing these could result in workloads missing required configuration, and cause problems. See
Rollout the updated policies below for advice on how to roll these changes
out safely.

### 2.b. Eliminate options not covered by the Pod Security Standards {#eliminate-non-standard-options}

There are several fields in PodSecurityPolicy that are not covered by the Pod Security Standards. If
you must enforce these options, you will need to supplement Pod Security Admission with an
admission webhook,
which is outside the scope of this guide.

First, you can remove the purely validating fields that the Pod Security Standards do not cover.
These fields (also listed in the
Mapping PodSecurityPolicies to Pod Security Standards
reference with "no opinion") are:

- `.spec.allowedHostPaths`
- `.spec.allowedFlexVolumes`
- `.spec.allowedCSIDrivers`
- `.spec.forbiddenSysctls`
- `.spec.runtimeClass`

You can also remove the following fields, that are related to POSIX / UNIX group controls.

If any of these use the `MustRunAs` strategy they may be mutating! Removing these could result in
workloads not setting the required groups, and cause problems. See
Rollout the updated policies below for advice on how to roll these changes
out safely.

- `.spec.runAsGroup`
- `.spec.supplementalGroups`
- `.spec.fsGroup`

The remaining mutating fields are required to properly support the Pod Security Standards, and will
need to be handled on a case-by-case basis later:

- `.spec.requiredDropCapabilities` - Required to drop `ALL` for the Restricted profile.
- `.spec.seLinux` - (Only mutating with the `MustRunAs` rule) required to enforce the SELinux
  requirements of the Baseline & Restricted profiles.
- `.spec.runAsUser` - (Non-mutating with the `RunAsAny` rule) required to enforce `RunAsNonRoot` for
  the Restricted profile.
- `.spec.allowPrivilegeEscalation` - (Only mutating if set to `false`) required for the Restricted
  profile.

### 2.c. Rollout the updated PSPs {#psp-update-rollout}

Next, you can rollout the updated policies to your cluster. You should proceed with caution, as
removing the mutating options may result in workloads missing required configuration.

For each updated PodSecurityPolicy:

1. Identify pods running under the original PSP. This can be done using the `kubernetes.io/psp`
   annotation. For example, using kubectl:
   ```sh
   PSP_NAME="original" # Set the name of the PSP you're checking for
   kubectl get pods --all-namespaces -o jsonpath="{range .items[?(@.metadata.annotations.kubernetes\.io\/psp=='$PSP_NAME')]}{.metadata.namespace} {.metadata.name}{'\n'}{end}"
   ```
2. Compare these running pods against the original pod spec to determine whether PodSecurityPolicy
   has modified the pod. For pods created by a workload resource
   you can compare the pod with the PodTemplate in the controller resource. If any changes are
   identified, the original Pod or PodTemplate should be updated with the desired configuration.
   The fields to review are:
   - `.metadata.annotations['container.apparmor.security.beta.kubernetes.io/*']` (replace * with each container name)
   - `.spec.runtimeClassName`
   - `.spec.securityContext.fsGroup`
   - `.spec.securityContext.seccompProfile`
   - `.spec.securityContext.seLinuxOptions`
   - `.spec.securityContext.supplementalGroups`
   - On containers, under `.spec.containers[*]` and `.spec.initContainers[*]`:
       - `.securityContext.allowPrivilegeEscalation`
       - `.securityContext.capabilities.add`
       - `.securityContext.capabilities.drop`
       - `.securityContext.readOnlyRootFilesystem`
       - `.securityContext.runAsGroup`
       - `.securityContext.runAsNonRoot`
       - `.securityContext.runAsUser`
       - `.securityContext.seccompProfile`
       - `.securityContext.seLinuxOptions`
3. Create the new PodSecurityPolicies. If any Roles or ClusterRoles are granting `use` on all PSPs
   this could cause the new PSPs to be used instead of their mutating counter-parts.
4. Update your authorization to grant access to the new PSPs. In RBAC this means updating any Roles
   or ClusterRoles that grant the `use` permission on the original PSP to also grant it to the
   updated PSP.
5. Verify: after some soak time, rerun the command from step 1 to see if any pods are still using
   the original PSPs. Note that pods need to be recreated after the new policies have been rolled
   out before they can be fully verified.
6. (optional) Once you have verified that the original PSPs are no longer in use, you can delete
   them.
