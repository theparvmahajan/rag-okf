---
id: okf-structure/concepts/overview/working-with-objects/annotations.md#syntax-and-character-set
kind: section
title: Syntax and character set
source: concepts/overview/working-with-objects/annotations.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/
heading: Syntax and character set
parent: okf-structure/concepts/overview/working-with-objects/annotations
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/annotations.md#attaching-metadata-to-objects
next_sibling: okf-structure/concepts/overview/working-with-objects/annotations.md#whatsnext
word_count: 240
---

_Annotations_ are key/value pairs. Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (`.`), not longer than 253 characters in total, followed by a slash (`/`).

If the prefix is omitted, the annotation Key is presumed to be private to the user. Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation) which add annotations to end-user objects must specify a prefix.

The `kubernetes.io/` and `k8s.io/` prefixes are reserved for Kubernetes core components.

Valid annotation values have no character set restrictions — unlike label values, annotation values may contain any string, including special characters, whitespace, and structured data such as JSON or YAML.
If you plan to store binary data (such as CBOR),
the Kubernetes project recommends that you base64 encode it.
However, the total size of **all** annotations on a single object (keys and values combined) must not exceed 256 KiB.

For example, here's a manifest for a Pod that has the annotation `imageregistry: https://hub.docker.com/` :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: annotations-demo
  annotations:
    imageregistry: "https://hub.docker.com/"
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```
