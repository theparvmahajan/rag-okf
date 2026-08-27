---
id: okf-structure/concepts/overview/working-with-objects/labels.md#syntax-and-character-set
kind: section
title: Syntax and character set
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: Syntax and character set
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#motivation
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#label-selectors
word_count: 212
---

_Labels_ are key/value pairs. Valid label keys have two segments: an optional
prefix and name, separated by a slash (`/`). The name segment is required and
must be 63 characters or less, beginning and ending with an alphanumeric
character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`),
and alphanumerics between. The prefix is optional. If specified, the prefix
must be a DNS subdomain: a series of DNS labels separated by dots (`.`),
not longer than 253 characters in total, followed by a slash (`/`).

If the prefix is omitted, the label Key is presumed to be private to the user.
Automated system components (e.g. `kube-scheduler`, `kube-controller-manager`,
`kube-apiserver`, `kubectl`, or other third-party automation) which add labels
to end-user objects must specify a prefix.

The `kubernetes.io/` and `k8s.io/` prefixes are
reserved for Kubernetes core components.

Valid label value:

* must be 63 characters or less (can be empty),
* unless empty, must begin and end with an alphanumeric character (`[a-z0-9A-Z]`),
* could contain dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.

For example, here's a manifest for a Pod that has two labels
`environment: production` and `app: nginx`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: label-demo
  labels:
    environment: production
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```
