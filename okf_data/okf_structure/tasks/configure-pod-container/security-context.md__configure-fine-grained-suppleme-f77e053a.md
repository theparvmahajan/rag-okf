---
id: okf-structure/tasks/configure-pod-container/security-context.md#configure-fine-grained-supplementalgroups-control-for-a-pod-supplementalgroupspolicy
kind: section
title: Configure fine-grained SupplementalGroups control for a Pod {#supplementalgroupspolicy}
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Configure fine-grained SupplementalGroups control for a Pod {#supplementalgroupspolicy}
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#set-the-security-context-for-a-pod
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#configure-volume-permission-and-ownership-change-policy-for-pods
word_count: 466
---

This feature can be enabled by setting the `SupplementalGroupsPolicy`
feature gate for kubelet and
kube-apiserver, and setting the `.spec.securityContext.supplementalGroupsPolicy` field for a pod.

The `supplementalGroupsPolicy` field defines the policy for calculating the
supplementary groups for the container processes in a pod. There are two valid
values for this field:

* `Merge`: The group membership defined in `/etc/group` for the container's primary user will be merged.
  This is the default policy if not specified.

* `Strict`: Only group IDs in `fsGroup`, `supplementalGroups`, or `runAsGroup` fields 
  are attached as the supplementary groups of the container processes.
  This means no group membership from `/etc/group` for the container's primary user will be merged.

When the feature is enabled, it also exposes the process identity attached to the first container process
in `.status.containerStatuses[].user.linux` field. It would be useful for detecting if
implicit group ID's are attached.

This pod manifest defines `supplementalGroupsPolicy=Strict`. You can see that no group memberships
defined in `/etc/group` are merged to the supplementary groups for container processes.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-6.yaml
```

Verify that the Pod's Container is running:

```shell
kubectl get pod security-context-demo
```

Check the process identity:

```shell
kubectl exec -it security-context-demo -- id
```

The output is similar to this:

```none
uid=1000 gid=3000 groups=3000,4000
```

See the Pod's status:

```shell
kubectl get pod security-context-demo -o yaml
```

You can see that the `status.containerStatuses[].user.linux` field exposes the process identity
attached to the first container process.

```none
...
status:
  containerStatuses:
  - name: sec-ctx-demo
    user:
      linux:
        gid: 3000
        supplementalGroups:
        - 3000
        - 4000
        uid: 1000
...
```

Please note that the values in the `status.containerStatuses[].user.linux` field is _the first attached_
process identity to the first container process in the container. If the container has sufficient privilege
to make system calls related to process identity
(e.g. `setuid(2)`,
`setgid(2)` or
`setgroups(2)`, etc.),
the container process can change its identity. Thus, the _actual_ process identity will be dynamic.

### Implementations {#implementations-supplementalgroupspolicy}

The following container runtimes are known to support fine-grained SupplementalGroups control.

CRI-level:
- containerd, since v2.0
- CRI-O, since v1.31

You can see if the feature is supported in the Node status.

```yaml
apiVersion: v1
kind: Node
...
status:
  features:
    supplementalGroupsPolicy: true
```

At this alpha release(from v1.31 to v1.32), when a pod with `SupplementalGroupsPolicy=Strict` are scheduled to a node that does NOT support this feature(i.e. `.status.features.supplementalGroupsPolicy=false`), the pod's supplemental groups policy falls back to the `Merge` policy _silently_.

However, since the beta release (v1.33), to enforce the policy more strictly, __such pod creation will be rejected by kubelet because the node cannot ensure the specified policy__. When your pod is rejected, you will see warning events with `reason=SupplementalGroupsPolicyNotSupported` like below:

```yaml
apiVersion: v1
kind: Event
...
type: Warning
reason: SupplementalGroupsPolicyNotSupported
message: "SupplementalGroupsPolicy=Strict is not supported in this node"
involvedObject:
  apiVersion: v1
  kind: Pod
  ...
```
