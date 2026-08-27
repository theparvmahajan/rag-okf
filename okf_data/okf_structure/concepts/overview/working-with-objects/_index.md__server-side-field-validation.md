---
id: okf-structure/concepts/overview/working-with-objects/_index.md#server-side-field-validation
kind: section
title: Server side field validation
source: concepts/overview/working-with-objects/_index.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/
heading: Server side field validation
parent: okf-structure/concepts/overview/working-with-objects/_index
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/_index.md#understanding-kubernetes-objects-kubernetes-objects
next_sibling: okf-structure/concepts/overview/working-with-objects/_index.md#whatsnext
word_count: 161
---

Starting with Kubernetes v1.25, the API server offers server side
field validation
that detects unrecognized or duplicate fields in an object. It provides all the functionality
of `kubectl --validate` on the server side.

The `kubectl` tool uses the `--validate` flag to set the level of field validation. It accepts the
values `ignore`, `warn`, and `strict` while also accepting the values `true` (equivalent to `strict`)
and `false` (equivalent to `ignore`). The default validation setting for `kubectl` is `--validate=true`.

`Strict`
: Strict field validation, errors on validation failure

`Warn`
: Field validation is performed, but errors are exposed as warnings rather than failing the request

`Ignore`
: No server side field validation is performed

When `kubectl` cannot connect to an API server that supports field validation it will fall back
to using client-side validation. Kubernetes 1.27 and later versions always offer field validation;
older Kubernetes releases might not. If your cluster is older than v1.27, check the documentation
for your version of Kubernetes.
