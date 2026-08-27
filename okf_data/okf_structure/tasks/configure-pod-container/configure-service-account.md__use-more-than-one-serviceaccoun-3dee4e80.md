---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#use-more-than-one-serviceaccount-use-multiple-service-accounts
kind: section
title: Use more than one ServiceAccount {#use-multiple-service-accounts}
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: Use more than one ServiceAccount {#use-multiple-service-accounts}
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#use-the-default-service-account-to-access-the-api-server
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#manually-create-an-api-token-for-a-serviceaccount
word_count: 242
---

Every namespace has at least one ServiceAccount: the default ServiceAccount
resource, called `default`. You can list all ServiceAccount resources in your
current namespace
with:

```shell
kubectl get serviceaccounts
```

The output is similar to this:

```
NAME      SECRETS    AGE
default   1          1d
```

You can create additional ServiceAccount objects like this:

```shell
kubectl apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
EOF
```

The name of a ServiceAccount object must be a valid
DNS subdomain name.

If you get a complete dump of the service account object, like this:

```shell
kubectl get serviceaccounts/build-robot -o yaml
```

The output is similar to this:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2019-06-16T00:12:34Z
  name: build-robot
  namespace: default
  resourceVersion: "272500"
  uid: 721ab723-13bc-11e5-aec2-42010af0021e
```

You can use authorization plugins to
set permissions on service accounts.

To use a non-default service account, set the `spec.serviceAccountName`
field of a Pod to the name of the ServiceAccount you wish to use.

You can only set the `serviceAccountName` field when creating a Pod, or in a
template for a new Pod. You cannot update the `.spec.serviceAccountName` field
of a Pod that already exists.

The `.spec.serviceAccount` field is a deprecated alias for `.spec.serviceAccountName`.
If you want to remove the fields from a workload resource, set both fields to empty explicitly
on the pod template.

### Cleanup {#cleanup-use-multiple-service-accounts}

If you tried creating `build-robot` ServiceAccount from the example above,
you can clean it up by running:

```shell
kubectl delete serviceaccount/build-robot
```
