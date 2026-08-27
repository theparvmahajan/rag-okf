---
id: okf-structure/concepts/configuration/secret.md#introduction
kind: section
title: Secrets
source: concepts/configuration/secret.md
url: https://kubernetes.io/docs/concepts/configuration/secret/
heading: null
parent: okf-structure/concepts/configuration/secret
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/configuration/secret.md#uses-for-secrets
word_count: 262
---

A Secret is an object that contains a small amount of sensitive data such as
a password, a token, or a key. Such information might otherwise be put in a
pod specification or in a
container image. Using a
Secret means that you don't need to include confidential data in your
application code.

Because Secrets can be created independently of the Pods that use them, there
is less risk of the Secret (and its data) being exposed during the workflow of
creating, viewing, and editing Pods. Kubernetes, and applications that run in
your cluster, can also take additional precautions with Secrets, such as avoiding
writing sensitive data to nonvolatile storage.

Secrets are similar to ConfigMaps
but are specifically intended to hold confidential data.

Kubernetes Secrets are, by default, stored unencrypted in the API server's underlying data store
(etcd). Anyone with API access can retrieve or modify a Secret, and so can anyone with access to etcd.
Additionally, anyone who is authorized to create a Pod in a namespace can use that access to read
any Secret in that namespace; this includes indirect access such as the ability to create a
Deployment.

In order to safely use Secrets, take at least the following steps:

1. Enable Encryption at Rest for Secrets.
1. Enable or configure RBAC rules with
   least-privilege access to Secrets.
1. Restrict Secret access to specific containers.
1. Consider using external Secret store providers.

For more guidelines to manage and improve the security of your Secrets, refer to
Good practices for Kubernetes Secrets.

See Information security for Secrets for more details.
