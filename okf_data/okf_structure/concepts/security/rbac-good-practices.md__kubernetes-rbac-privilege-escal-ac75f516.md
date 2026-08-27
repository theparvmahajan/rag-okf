---
id: okf-structure/concepts/security/rbac-good-practices.md#kubernetes-rbac-privilege-escalation-risks-privilege-escalation-risks
kind: section
title: Kubernetes RBAC - privilege escalation risks {#privilege-escalation-risks}
source: concepts/security/rbac-good-practices.md
url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
heading: Kubernetes RBAC - privilege escalation risks {#privilege-escalation-risks}
parent: okf-structure/concepts/security/rbac-good-practices
children: []
prev_sibling: okf-structure/concepts/security/rbac-good-practices.md#general-good-practice
next_sibling: okf-structure/concepts/security/rbac-good-practices.md#kubernetes-rbac-denial-of-service-risks-denial-of-service-risks
word_count: 915
---

Within Kubernetes RBAC there are a number of privileges which, if granted, can allow a user or a service account
to escalate their privileges in the cluster or affect systems outside the cluster.

This section is intended to provide visibility of the areas where cluster operators
should take care, to ensure that they do not inadvertently allow for more access to clusters than intended.

### Listing secrets

It is generally clear that allowing `get` access on Secrets will allow a user to read their contents.
It is also important to note that `list` and `watch` access also effectively allow for users to reveal the Secret contents.
For example, when a List response is returned (for example, via `kubectl get secrets -A -o yaml`), the response
includes the contents of all Secrets.

### Workload creation

Permission to create workloads (either Pods, or
workload resources that manage Pods) in a namespace
implicitly grants access to many other resources in that namespace, such as Secrets, ConfigMaps, and
PersistentVolumes that can be mounted in Pods. Additionally, since Pods can run as any
ServiceAccount, granting permission
to create workloads also implicitly grants the API access levels of any service account in that
namespace.

Users who can run privileged Pods can use that access to gain node access and potentially to
further elevate their privileges. Where you do not fully trust a user or other principal
with the ability to create suitably secure and isolated Pods, you should enforce either the
**Baseline** or **Restricted** Pod Security Standard.
You can use Pod Security admission
or other (third party) mechanisms to implement that enforcement.

For these reasons, namespaces should be used to separate resources requiring different levels of
trust or tenancy. It is still considered best practice to follow least privilege
principles and assign the minimum set of permissions, but boundaries within a namespace should be
considered weak.

### Persistent volume creation

If someone - or some application - is allowed to create arbitrary PersistentVolumes, that access
includes the creation of `hostPath` volumes, which then means that a Pod would get access
to the underlying host filesystem(s) on the associated node. Granting that ability is a security risk.

There are many ways a container with unrestricted access to the host filesystem can escalate privileges, including
reading data from other containers, and abusing the credentials of system services, such as Kubelet.

You should only allow access to create PersistentVolume objects for:

- Users (cluster operators) that need this access for their work, and who you trust.
- The Kubernetes control plane components which creates PersistentVolumes based on PersistentVolumeClaims
  that are configured for automatic provisioning.
  This is usually setup by the Kubernetes provider or by the operator when installing a CSI driver.

Where access to persistent storage is required trusted administrators should create
PersistentVolumes, and constrained users should use PersistentVolumeClaims to access that storage.

### Access to `proxy` subresource of Nodes

Users with access to the `nodes/proxy` sub-resource have rights to the Kubelet API,
which allows for command execution on every pod on the node(s) to which they have rights.
This access bypasses audit logging and admission control, so care should be taken before
granting any rights to this resource.
These APIs can be exercised via websocket HTTP `GET` requests, which only requires authorization of the **get** verb.
This means that **get** permission on `nodes/proxy` is not a read-only permission.
For example, permission to **get** `nodes/proxy` provides access to privileged kubelet
APIs that can retrieve container logs or execute and attach to pod processes,
even when a caller does not have the equivalent permissions through the
Kubernetes API.

See Kubelet authentication/authorization
for more information.

### Escalate verb

Generally, the RBAC system prevents users from creating clusterroles with more rights than the user possesses.
The exception to this is the `escalate` verb. As noted in the RBAC documentation,
users with this right can effectively escalate their privileges.

### Bind verb

Similar to the `escalate` verb, granting users this right allows for the bypass of Kubernetes
in-built protections against privilege escalation, allowing users to create bindings to
roles with rights they do not already have.

### Impersonate verb

This verb allows users to impersonate and gain the rights of other users in the cluster.
Care should be taken when granting it, to ensure that excessive permissions cannot be gained
via one of the impersonated accounts.

### CSRs and certificate issuing

The CSR API allows for users with `create` rights to CSRs and `update` rights on `certificatesigningrequests/approval`
where the signer is `kubernetes.io/kube-apiserver-client` to create new client certificates
which allow users to authenticate to the cluster. Those client certificates can have arbitrary
names including duplicates of Kubernetes system components. This will effectively allow for privilege escalation.

### Token request

Users with `create` rights on `serviceaccounts/token` can create TokenRequests to issue
tokens for existing service accounts.

### Control admission webhooks

Users with control over `validatingwebhookconfigurations` or `mutatingwebhookconfigurations`
can control webhooks that can read any object admitted to the cluster, and in the case of
mutating webhooks, also mutate admitted objects.

### Namespace modification

Users who can perform **patch** operations on Namespace objects (through a namespaced RoleBinding to a Role with that access) can modify
labels on that namespace. In clusters where Pod Security Admission is used, this may allow a user to configure the namespace
for a more permissive policy than intended by the administrators.
For clusters where NetworkPolicy is used, users may be set labels that indirectly allow
access to services that an administrator did not intend to allow.
