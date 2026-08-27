---
id: okf-structure/concepts/cluster-administration/_index.md#securing-a-cluster
kind: section
title: Securing a cluster
source: concepts/cluster-administration/_index.md
url: https://kubernetes.io/docs/concepts/cluster-administration/
heading: Securing a cluster
parent: okf-structure/concepts/cluster-administration/_index
children: []
prev_sibling: okf-structure/concepts/cluster-administration/_index.md#managing-a-cluster
next_sibling: okf-structure/concepts/cluster-administration/_index.md#optional-cluster-services
word_count: 153
---

* Generate Certificates describes the steps to
  generate certificates using different tool chains.

* Kubernetes Container Environment describes
  the environment for Kubelet managed containers on a Kubernetes node.

* Controlling Access to the Kubernetes API describes
  how Kubernetes implements access control for its own API.

* Authenticating explains authentication in
  Kubernetes, including the various authentication options.

* Authorization is separate from
  authentication, and controls how HTTP calls are handled.

* Using Admission Controllers
  explains plug-ins which intercepts requests to the Kubernetes API server after authentication
  and authorization.

* Admission Webhook Good Practices
  provides good practices and considerations when designing mutating admission
  webhooks and validating admission webhooks.

* Using Sysctls in a Kubernetes Cluster
  describes to an administrator how to use the `sysctl` command-line tool to set kernel parameters
.

* Auditing describes how to interact with Kubernetes'
  audit logs.

### Securing the kubelet

* Control Plane-Node communication
* TLS bootstrapping
* Kubelet authentication/authorization
