---
id: okf-structure/concepts/configuration/configmap.md#configmap-object
kind: section
title: ConfigMap object
source: concepts/configuration/configmap.md
url: https://kubernetes.io/docs/concepts/configuration/configmap/
heading: ConfigMap object
parent: okf-structure/concepts/configuration/configmap
children: []
prev_sibling: okf-structure/concepts/configuration/configmap.md#motivation
next_sibling: okf-structure/concepts/configuration/configmap.md#configmaps-and-pods
word_count: 133
---

A ConfigMap is an API object
that lets you store configuration for other objects to use. Unlike most
Kubernetes objects that have a `spec`, a ConfigMap has `data` and `binaryData`
fields. These fields accept key-value pairs as their values.  Both the `data`
field and the `binaryData` are optional. The `data` field is designed to
contain UTF-8 strings while the `binaryData` field is designed to
contain binary data as base64-encoded strings.

The name of a ConfigMap must be a valid
DNS subdomain name.

Each key under the `data` or the `binaryData` field must consist of
alphanumeric characters, `-`, `_` or `.`. The keys stored in `data` must not
overlap with the keys in the `binaryData` field.

Starting from v1.19, you can add an `immutable` field to a ConfigMap
definition to create an immutable ConfigMap.
