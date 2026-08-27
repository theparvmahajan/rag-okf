---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-role-and-rolebinding
kind: section
title: Create Role and RoleBinding
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Create Role and RoleBinding
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#configure-the-certificate-into-kubeconfig
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#whatsnext
word_count: 93
---

If you don't use Kubernetes RBAC, skip this step and make the appropriate changes for the authorization mechanism
your cluster actually uses.

With the certificate created, it is time to define the Role and RoleBinding for this user to access Kubernetes cluster resources.

This is a sample command to create a Role for this new user:

```shell
kubectl create role developer --verb=create --verb=get --verb=list --verb=update --verb=delete --resource=pods
```

Equivalent YAML:

This is a sample command to create a RoleBinding for this new user:

```shell
kubectl create rolebinding developer-binding-myuser --role=developer --user=myuser
```

Equivalent YAML:
