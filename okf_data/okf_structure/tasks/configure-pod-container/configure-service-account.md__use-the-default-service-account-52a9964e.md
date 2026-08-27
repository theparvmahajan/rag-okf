---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#use-the-default-service-account-to-access-the-api-server
kind: section
title: Use the default service account to access the API server
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: Use the default service account to access the API server
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#use-more-than-one-serviceaccount-use-multiple-service-accounts
word_count: 311
---

When Pods contact the API server, Pods authenticate as a particular
ServiceAccount (for example, `default`). There is always at least one
ServiceAccount in each namespace.

Every Kubernetes namespace contains at least one ServiceAccount: the default
ServiceAccount for that namespace, named `default`.
If you do not specify a ServiceAccount when you create a Pod, Kubernetes
automatically assigns the ServiceAccount named `default` in that namespace.

You can fetch the details for a Pod you have created. For example:

```shell
kubectl get pods/<podname> -o yaml
```

In the output, you see a field `spec.serviceAccountName`.
Kubernetes automatically
sets that value if you don't specify it when you create a Pod.

An application running inside a Pod can access the Kubernetes API using
automatically mounted service account credentials.
See accessing the Cluster to learn more.

When a Pod authenticates as a ServiceAccount, its level of access depends on the
authorization plugin and policy
in use.

The API credentials are automatically revoked when the Pod is deleted, even if
finalizers are in place. In particular, the API credentials are revoked 60 seconds
beyond the `.metadata.deletionTimestamp` set on the Pod (the deletion timestamp
is typically the time that the **delete** request was accepted plus the Pod's
termination grace period).

### Opt out of API credential automounting

If you don't want the kubelet
to automatically mount a ServiceAccount's API credentials, you can opt out of
the default behavior.
You can opt out of automounting API credentials on `/var/run/secrets/kubernetes.io/serviceaccount/token`
for a service account by setting `automountServiceAccountToken: false` on the ServiceAccount:

For example:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: build-robot
automountServiceAccountToken: false
...
```

You can also opt out of automounting API credentials for a particular Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  serviceAccountName: build-robot
  automountServiceAccountToken: false
  ...
```

If both the ServiceAccount and the Pod's `.spec` specify a value for
`automountServiceAccountToken`, the Pod spec takes precedence.
