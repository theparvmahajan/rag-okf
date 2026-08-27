---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#overview
kind: section
title: Overview
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: Overview
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#trade-offs
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-create-objects
word_count: 160
---

Declarative object configuration requires a firm understanding of
the Kubernetes object definitions and configuration. Read and complete
the following documents if you have not already:

* Managing Kubernetes Objects Using Imperative Commands
* Imperative Management of Kubernetes Objects Using Configuration Files

Following are definitions for terms used in this document:

- *object configuration file / configuration file*: A file that defines the
  configuration for a Kubernetes object. This topic shows how to pass configuration
  files to `kubectl apply`. Configuration files are typically stored in source control, such as Git.
- *live object configuration / live configuration*: The live configuration
  values of an object, as observed by the Kubernetes cluster. These are kept in the Kubernetes
  cluster storage, typically etcd.
- *declarative configuration writer / declarative writer*: A person or software component
  that makes updates to a live object. The live writers referred to in this topic make changes
  to object configuration files and run `kubectl apply` to write the changes.
