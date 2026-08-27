---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#trusting-tls-in-a-cluster
kind: section
title: Trusting TLS in a cluster
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Trusting TLS in a cluster
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#prerequisites
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#requesting-a-certificate
word_count: 150
---

Trusting the custom CA from an application running as a pod usually requires
some extra application configuration. You will need to add the CA certificate
bundle to the list of CA certificates that the TLS client or server trusts. For
example, you would do this with a Golang TLS config by parsing the certificate
chain and adding the parsed certificates to the `RootCAs` field in the
`tls.Config` struct.

Even though the custom CA certificate may be included in the filesystem (in the
ConfigMap `kube-root-ca.crt`),
you should not use that certificate authority for any purpose other than to verify internal
Kubernetes endpoints. An example of an internal Kubernetes endpoint is the
Service named `kubernetes` in the default namespace.

If you want to use a custom certificate authority for your workloads, you should generate
that CA separately, and distribute its CA certificate using a 
ConfigMap that your pods 
have access to read.
