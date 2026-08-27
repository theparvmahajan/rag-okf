---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#manually-create-an-api-token-for-a-serviceaccount
kind: section
title: Manually create an API token for a ServiceAccount
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: Manually create an API token for a ServiceAccount
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#use-more-than-one-serviceaccount-use-multiple-service-accounts
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#add-imagepullsecrets-to-a-service-account
word_count: 483
---

Suppose you have an existing service account named "build-robot" as mentioned earlier.

You can get a time-limited API token for that ServiceAccount using `kubectl`:

```shell
kubectl create token build-robot
```

The output from that command is a token that you can use to authenticate as that
ServiceAccount. You can request a specific token duration using the `--duration`
command line argument to `kubectl create token` (the actual duration of the issued
token might be shorter, or could even be longer).

Using `kubectl` v1.31 or later, it is possible to create a service 
account token that is directly bound to a Node:

```shell
kubectl create token build-robot --bound-object-kind Node --bound-object-name node-001 --bound-object-uid 123...456
```

The token will be valid until it expires or either the associated Node or service account are deleted.

Versions of Kubernetes before v1.22 automatically created long term credentials for
accessing the Kubernetes API. This older mechanism was based on creating token Secrets
that could then be mounted into running Pods. In more recent versions, including
Kubernetes v, API credentials are obtained directly by using the
TokenRequest API,
and are mounted into Pods using a
projected volume.
The tokens obtained using this method have bounded lifetimes, and are automatically
invalidated when the Pod they are mounted into is deleted.

You can still manually create a service account token Secret; for example,
if you need a token that never expires. However, using the
TokenRequest
subresource to obtain a token to access the API is recommended instead.

### Manually create a long-lived API token for a ServiceAccount

If you want to obtain an API token for a ServiceAccount, you create a new Secret
with a special annotation, `kubernetes.io/service-account.name`.

```shell
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: build-robot-secret
  annotations:
    kubernetes.io/service-account.name: build-robot
type: kubernetes.io/service-account-token
EOF
```

If you view the Secret using:

```shell
kubectl get secret/build-robot-secret -o yaml
```

you can see that the Secret now contains an API token for the "build-robot" ServiceAccount.

Because of the annotation you set, the control plane automatically generates a token for that
ServiceAccounts, and stores them into the associated Secret. The control plane also cleans up
tokens for deleted ServiceAccounts.

```shell
kubectl describe secrets/build-robot-secret
```

The output is similar to this:

```
Name:           build-robot-secret
Namespace:      default
Labels:         <none>
Annotations:    kubernetes.io/service-account.name: build-robot
                kubernetes.io/service-account.uid: da68f9c6-9d26-11e7-b84e-002dc52800da

Type:   kubernetes.io/service-account-token

Data
====
ca.crt:         1338 bytes
namespace:      7 bytes
token:          ...
```

The content of `token` is omitted here.

Take care not to display the contents of a `kubernetes.io/service-account-token`
Secret somewhere that your terminal / computer screen could be seen by an onlooker.

When you delete a ServiceAccount that has an associated Secret, the Kubernetes
control plane automatically cleans up the long-lived token from that Secret.

If you view the ServiceAccount using:

` kubectl get serviceaccount build-robot -o yaml`

You can't see the `build-robot-secret` Secret in the ServiceAccount API objects
`.secrets` field
because that field is only populated with auto-generated Secrets.
