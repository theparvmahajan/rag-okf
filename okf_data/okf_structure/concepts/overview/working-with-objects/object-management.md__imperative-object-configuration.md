---
id: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-object-configuration
kind: section
title: Imperative object configuration
source: concepts/overview/working-with-objects/object-management.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
heading: Imperative object configuration
parent: okf-structure/concepts/overview/working-with-objects/object-management
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#imperative-commands
next_sibling: okf-structure/concepts/overview/working-with-objects/object-management.md#declarative-object-configuration
word_count: 297
---

In imperative object configuration, the kubectl command specifies the
operation (create, replace, etc.), optional flags and at least one file
name. The file specified must contain a full definition of the object
in YAML or JSON format.

See the API reference
for more details on object definitions.

The imperative `replace` command replaces the existing
spec with the newly provided one, dropping all changes to the object missing from
the configuration file.  This approach should not be used with resource
types whose specs are updated independently of the configuration file.
Services of type `LoadBalancer`, for example, have their `externalIPs` field updated
independently from the configuration by the cluster.

### Examples

Create the objects defined in a configuration file:

```sh
kubectl create -f nginx.yaml
```

Delete the objects defined in two configuration files:

```sh
kubectl delete -f nginx.yaml -f redis.yaml
```

Update the objects defined in a configuration file by overwriting
the live configuration:

```sh
kubectl replace -f nginx.yaml
```

### Trade-offs

Advantages compared to imperative commands:

- Object configuration can be stored in a source control system such as Git.
- Object configuration can integrate with processes such as reviewing changes before push and audit trails.
- Object configuration provides a template for creating new objects.

Disadvantages compared to imperative commands:

- Object configuration requires basic understanding of the object schema.
- Object configuration requires the additional step of writing a YAML file.

Advantages compared to declarative object configuration:

- Imperative object configuration behavior is simpler and easier to understand.
- As of Kubernetes version 1.5, imperative object configuration is more mature.

Disadvantages compared to declarative object configuration:

- Imperative object configuration works best on files, not directories.
- Updates to live objects must be reflected in configuration files, or they will be lost during the next replacement.
