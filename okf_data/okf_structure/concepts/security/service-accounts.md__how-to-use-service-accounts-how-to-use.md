---
id: okf-structure/concepts/security/service-accounts.md#how-to-use-service-accounts-how-to-use
kind: section
title: How to use service accounts {#how-to-use}
source: concepts/security/service-accounts.md
url: https://kubernetes.io/docs/concepts/security/service-accounts/
heading: How to use service accounts {#how-to-use}
parent: okf-structure/concepts/security/service-accounts
children: []
prev_sibling: okf-structure/concepts/security/service-accounts.md#use-cases-for-kubernetes-service-accounts-use-cases
next_sibling: okf-structure/concepts/security/service-accounts.md#authenticating-service-account-credentials-authenticating-credentials
word_count: 1062
---

To use a Kubernetes service account, you do the following:

1. Create a ServiceAccount object using a Kubernetes
   client like `kubectl` or a manifest that defines the object.
1. Grant permissions to the ServiceAccount object using an authorization
   mechanism such as
   RBAC.
1. Assign the ServiceAccount object to Pods during Pod creation.
   
   If you're using the identity from an external service,
   retrieve the ServiceAccount token and use it from that
   service instead.

For instructions, refer to
Configure Service Accounts for Pods.

### Grant permissions to a ServiceAccount {#grant-permissions}

You can use the built-in Kubernetes
role-based access control (RBAC)
mechanism to grant the minimum permissions required by each service account.
You create a *role*, which grants access, and then *bind* the role to your
ServiceAccount. RBAC lets you define a minimum set of permissions so that the
service account permissions follow the principle of least privilege. Pods that
use that service account don't get more permissions than are required to
function correctly.

For instructions, refer to
ServiceAccount permissions.

#### Cross-namespace access using a ServiceAccount {#cross-namespace}

You can use RBAC to allow service accounts in one namespace to perform actions
on resources in a different namespace in the cluster. For example, consider a
scenario where you have a service account and Pod in the `dev` namespace and
you want your Pod to see Jobs running in the `maintenance` namespace. You could
create a Role object that grants permissions to list Job objects. Then,
you'd create a RoleBinding object in the `maintenance` namespace to bind the
Role to the ServiceAccount object. Now, Pods in the `dev` namespace can list
Job objects in the `maintenance` namespace using that service account.

### Assign a ServiceAccount to a Pod {#assign-to-pod}

To assign a ServiceAccount to a Pod, you set the `spec.serviceAccountName`
field in the Pod specification. Kubernetes then automatically provides the
credentials for that ServiceAccount to the Pod. In v1.22 and later, Kubernetes
gets a short-lived, **automatically rotating** token using the `TokenRequest`
API and mounts the token as a
projected volume.

By default, Kubernetes provides the Pod
with the credentials for an assigned ServiceAccount, whether that is the
`default` ServiceAccount or a custom ServiceAccount that you specify.

To prevent Kubernetes from automatically injecting
credentials for a specified ServiceAccount or the `default` ServiceAccount, set the
`automountServiceAccountToken` field in your Pod specification to `false`.

In versions earlier than 1.22, Kubernetes provides a long-lived, static token
to the Pod as a Secret.

#### Manually retrieve ServiceAccount credentials {#get-a-token}

If you need the credentials for a ServiceAccount to mount in a non-standard
location, or for an audience that isn't the API server, use one of the
following methods:

* TokenRequest API
  (recommended): Request a short-lived service account token from within
  your own *application code*. The token expires automatically and can rotate
  upon expiration.
  If you have a legacy application that is not aware of Kubernetes, you
  could use a sidecar container within the same pod to fetch these tokens
  and make them available to the application workload.
* Token Volume Projection
  (also recommended): In Kubernetes v1.20 and later, use the Pod specification to
  tell the kubelet to add the service account token to the Pod as a
  *projected volume*. Projected tokens expire automatically, and the kubelet
  rotates the token before it expires.
* Service Account Token Secrets
  (not recommended): You can mount service account tokens as Kubernetes
  Secrets in Pods. These tokens don't expire and don't rotate. In versions prior to v1.24, a permanent token was automatically created for each service account.
  This method is not recommended anymore, especially at scale, because of the risks associated
  with static, long-lived credentials. The LegacyServiceAccountTokenNoAutoGeneration feature gate
  (which was enabled by default from Kubernetes v1.24 to v1.26),  prevented Kubernetes from automatically creating these tokens for
  ServiceAccounts. The feature gate is removed in v1.27, because it was elevated to GA status; you can still create indefinite service account tokens manually, but should take into account the security implications.

#### Node audience restriction for service account tokens {#node-audience-restriction}

When the `ServiceAccountNodeAudienceRestriction` feature gate
is enabled, the NodeRestriction
admission plugin limits which audiences a kubelet can request when creating service
account tokens via the `TokenRequest` API. By default, the kubelet can only request
tokens for audiences already referenced by pods on that node (through projected service
account token volumes or CSI driver token requests). Administrators can grant
kubelets access to additional audiences using RBAC rules with the
`request-serviceaccounts-token-audience` verb.

This restriction applies only to kubelets (node identities) and does not affect other
callers of the `TokenRequest` API. For details and RBAC examples,
see Service account token audience restriction.

For applications running outside your Kubernetes cluster, you might be considering
creating a long-lived ServiceAccount token that is stored in a Secret. This allows authentication, but the Kubernetes project recommends you avoid this approach.
Long-lived bearer tokens represent a security risk as, once disclosed, the token
can be misused. Instead, consider using an alternative. For example, your external
application can authenticate using a well-protected private key `and` a certificate,
or using a custom mechanism such as an authentication webhook that you implement yourself.

You can also use TokenRequest to obtain short-lived tokens for your external application.

### Restricting access to Secrets (deprecated) {#enforce-mountable-secrets}

`kubernetes.io/enforce-mountable-secrets` is deprecated since Kubernetes v1.32. Use separate namespaces to isolate access to mounted secrets.

Kubernetes provides an annotation called `kubernetes.io/enforce-mountable-secrets`
that you can add to your ServiceAccounts. When this annotation is applied,
the ServiceAccount's secrets can only be mounted on specified types of resources,
enhancing the security posture of your cluster.

You can add the annotation to a ServiceAccount using a manifest:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    kubernetes.io/enforce-mountable-secrets: "true"
  name: my-serviceaccount
  namespace: my-namespace
```
When this annotation is set to "true", the Kubernetes control plane ensures that
the Secrets from this ServiceAccount are subject to certain mounting restrictions.

1. The name of each Secret that is mounted as a volume in a Pod must appear in the `secrets` field of the
   Pod's ServiceAccount.
1. The name of each Secret referenced using `envFrom` in a Pod must also appear in the `secrets`
   field of the Pod's ServiceAccount.
1. The name of each Secret referenced using `imagePullSecrets` in a Pod must also appear in the `secrets`
   field of the Pod's ServiceAccount.

By understanding and enforcing these restrictions, cluster administrators can maintain a tighter security profile and ensure that secrets are accessed only by the appropriate resources.
