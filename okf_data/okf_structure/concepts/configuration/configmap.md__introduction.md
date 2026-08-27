---
id: okf-structure/concepts/configuration/configmap.md#introduction
kind: section
title: ConfigMaps
source: concepts/configuration/configmap.md
url: https://kubernetes.io/docs/concepts/configuration/configmap/
heading: null
parent: okf-structure/concepts/configuration/configmap
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/configuration/configmap.md#motivation
word_count: 34
---

ConfigMap does not provide secrecy or encryption.
If the data you want to store are confidential, use a
Secret rather than a ConfigMap,
or use additional (third party) tools to keep your data private.
