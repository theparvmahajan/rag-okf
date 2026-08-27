---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-change-ownership-of-a-field-between-the-configuration-file-and-direct-imperative-writers
kind: section
title: How to change ownership of a field between the configuration file and direct
  imperative writers
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: How to change ownership of a field between the configuration file and direct
  imperative writers
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#default-field-values
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#changing-management-methods
word_count: 125
---

These are the only methods you should use to change an individual object field:

- Use `kubectl apply`.
- Write directly to the live configuration without modifying the configuration file:
for example, use `kubectl scale`.

### Changing the owner from a direct imperative writer to a configuration file

Add the field to the configuration file. For the field, discontinue direct updates to
the live configuration that do not go through `kubectl apply`.

### Changing the owner from a configuration file to a direct imperative writer

As of Kubernetes 1.5, changing ownership of a field from a configuration file to
an imperative writer requires manual steps:

- Remove the field from the configuration file.
- Remove the field from the `kubectl.kubernetes.io/last-applied-configuration` annotation on the live object.
