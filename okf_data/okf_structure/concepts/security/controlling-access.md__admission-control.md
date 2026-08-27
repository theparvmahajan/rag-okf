---
id: okf-structure/concepts/security/controlling-access.md#admission-control
kind: section
title: Admission control
source: concepts/security/controlling-access.md
url: https://kubernetes.io/docs/concepts/security/controlling-access/
heading: Admission control
parent: okf-structure/concepts/security/controlling-access
children: []
prev_sibling: okf-structure/concepts/security/controlling-access.md#authorization
next_sibling: okf-structure/concepts/security/controlling-access.md#auditing
word_count: 154
---

Admission Control modules are software modules that can modify or reject requests.
In addition to the attributes available to Authorization modules, Admission
Control modules can access the contents of the object that is being created or modified.

Admission controllers act on requests that create, modify, delete, or connect to (proxy) an object.
Admission controllers do not act on requests that merely read objects.
When multiple admission controllers are configured, they are called in order.

This is shown as step **3** in the diagram.

Unlike Authentication and Authorization modules, if any admission controller module
rejects, then the request is immediately rejected.

In addition to rejecting objects, admission controllers can also set complex defaults for
fields.

The available Admission Control modules are described in Admission Controllers.

Once a request passes all admission controllers, it is validated using the validation routines
for the corresponding API object, and then written to the object store (shown as step **4**).
