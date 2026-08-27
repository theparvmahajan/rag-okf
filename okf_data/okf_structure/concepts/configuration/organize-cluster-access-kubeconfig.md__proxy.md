---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#proxy
kind: section
title: Proxy
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: Proxy
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#file-references
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#whatsnext
word_count: 42
---

You can configure `kubectl` to use a proxy per cluster using `proxy-url` in your kubeconfig file, like this:

```yaml
apiVersion: v1
kind: Config

clusters:
- cluster:
    proxy-url: http://proxy.example.org:3128
    server: https://k8s.example.org/k8s/clusters/c-xxyyzz
  name: development

users:
- name: developer

contexts:
- context:
  name: development
```
