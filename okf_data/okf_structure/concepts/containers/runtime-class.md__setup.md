---
id: okf-structure/concepts/containers/runtime-class.md#setup
kind: section
title: Setup
source: concepts/containers/runtime-class.md
url: https://kubernetes.io/docs/concepts/containers/runtime-class/
heading: Setup
parent: okf-structure/concepts/containers/runtime-class
children: []
prev_sibling: okf-structure/concepts/containers/runtime-class.md#motivation
next_sibling: okf-structure/concepts/containers/runtime-class.md#usage
word_count: 238
---

1. Configure the CRI implementation on nodes (runtime dependent)
2. Create the corresponding RuntimeClass resources

### 1. Configure the CRI implementation on nodes

The configurations available through RuntimeClass are Container Runtime Interface (CRI)
implementation dependent. See the corresponding documentation (below) for your
CRI implementation for how to configure.

RuntimeClass assumes a homogeneous node configuration across the cluster by default (which means
that all nodes are configured the same way with respect to container runtimes). To support
heterogeneous node configurations, see Scheduling below.

The configurations have a corresponding `handler` name, referenced by the RuntimeClass. The
handler must be a valid DNS label name.

### 2. Create the corresponding RuntimeClass resources

The configurations setup in step 1 should each have an associated `handler` name, which identifies
the configuration. For each handler, create a corresponding RuntimeClass object.

The RuntimeClass resource currently only has 2 significant fields: the RuntimeClass name
(`metadata.name`) and the handler (`handler`). The object definition looks like this:

```yaml
# RuntimeClass is defined in the node.k8s.io API group
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  # The name the RuntimeClass will be referenced by.
  # RuntimeClass is a non-namespaced resource.
  name: myclass 
# The name of the corresponding CRI configuration
handler: myconfiguration 
```

The name of a RuntimeClass object must be a valid
DNS subdomain name.

It is recommended that RuntimeClass write operations (create/update/patch/delete) be
restricted to the cluster administrator. This is typically the default. See
Authorization Overview for more details.
