---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#3-update-namespaces-update-namespaces
kind: section
title: 3. Update Namespaces {#update-namespaces}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 3. Update Namespaces {#update-namespaces}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#2-simplify-standardize-podsecuritypolicies-simplify-psps
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#4-review-namespace-creation-processes-review-namespace-creation-process
word_count: 690
---

The following steps will need to be performed on every namespace in the cluster. Commands referenced
in these steps use the `$NAMESPACE` variable to refer to the namespace being updated.

### 3.a. Identify an appropriate Pod Security level {#identify-appropriate-level}

Start reviewing the Pod Security Standards and
familiarizing yourself with the 3 different levels.

There are several ways to choose a Pod Security level for your namespace:

1. **By security requirements for the namespace** - If you are familiar with the expected access
   level for the namespace, you can choose an appropriate level based on those requirements, similar
   to how one might approach this on a new cluster.
2. **By existing PodSecurityPolicies** - Using the
   Mapping PodSecurityPolicies to Pod Security Standards
   reference you can map each
   PSP to a Pod Security Standard level. If your PSPs aren't based on the Pod Security Standards, you
   may need to decide between choosing a level that is at least as permissive as the PSP, and a
   level that is at least as restrictive. You can see which PSPs are in use for pods in a given
   namespace with this command:
   ```sh
   kubectl get pods -n $NAMESPACE -o jsonpath="{.items[*].metadata.annotations.kubernetes\.io\/psp}" | tr " " "\n" | sort -u
   ```
3. **By existing pods** - Using the strategies under Verify the Pod Security level,
   you can test out both the Baseline and Restricted levels to see
   whether they are sufficiently permissive for existing workloads, and chose the least-privileged
   valid level.

Options 2 & 3 above are based on _existing_ pods, and may miss workloads that aren't currently
running, such as CronJobs, scale-to-zero workloads, or other workloads that haven't rolled out.

### 3.b. Verify the Pod Security level {#verify-pss-level}

Once you have selected a Pod Security level for the namespace (or if you're trying several), it's a
good idea to test it out first (you can skip this step if using the Privileged level). Pod Security
includes several tools to help test and safely roll out profiles.

First, you can dry-run the policy, which will evaluate pods currently running in the namespace
against the applied policy, without making the new policy take effect:
```sh
# $LEVEL is the level to dry-run, either "baseline" or "restricted".
kubectl label --dry-run=server --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL
```
This command will return a warning for any _existing_ pods that are not valid under the proposed
level.

The second option is better for catching workloads that are not currently running: audit mode. When
running under audit-mode (as opposed to enforcing), pods that violate the policy level are recorded
in the audit logs, which can be reviewed later after some soak time, but are not forbidden. Warning
mode works similarly, but returns the warning to the user immediately. You can set the audit level
on a namespace with this command:
```sh
kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/audit=$LEVEL
```

If either of these approaches yield unexpected violations, you will need to either update the
violating workloads to meet the policy requirements, or relax the namespace Pod Security level.

### 3.c. Enforce the Pod Security level {#enforce-pod-security-level}

When you are satisfied that the chosen level can safely be enforced on the namespace, you can update
the namespace to enforce the desired level:

```sh
kubectl label --overwrite ns $NAMESPACE pod-security.kubernetes.io/enforce=$LEVEL
```

### 3.d. Bypass PodSecurityPolicy {#bypass-psp}

Finally, you can effectively bypass PodSecurityPolicy at the namespace level by binding the fully
privileged PSP to all service
accounts in the namespace.

```sh
# The following cluster-scoped commands are only needed once.
kubectl apply -f privileged-psp.yaml
kubectl create clusterrole privileged-psp --verb use --resource podsecuritypolicies.policy --resource-name privileged

# Per-namespace disable
kubectl create -n $NAMESPACE rolebinding disable-psp --clusterrole privileged-psp --group system:serviceaccounts:$NAMESPACE
```

Since the privileged PSP is non-mutating, and the PSP admission controller always
prefers non-mutating PSPs, this will ensure that pods in this namespace are no longer being modified
or restricted by PodSecurityPolicy.

The advantage to disabling PodSecurityPolicy on a per-namespace basis like this is if a problem
arises you can easily roll the change back by deleting the RoleBinding. Just make sure the
pre-existing PodSecurityPolicies are still in place!

```sh
# Undo PodSecurityPolicy disablement.
kubectl delete -n $NAMESPACE rolebinding disable-psp
```
