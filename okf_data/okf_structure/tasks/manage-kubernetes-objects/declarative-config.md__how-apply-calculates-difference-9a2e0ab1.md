---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-apply-calculates-differences-and-merges-changes
kind: section
title: How apply calculates differences and merges changes
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: How apply calculates differences and merges changes
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-view-an-object
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#default-field-values
word_count: 1603
---

A *patch* is an update operation that is scoped to specific fields of an object
instead of the entire object. This enables updating only a specific set of fields
on an object without reading the object first.

When `kubectl apply` updates the live configuration for an object,
it does so by sending a patch request to the API server. The
patch defines updates scoped to specific fields of the live object
configuration. The `kubectl apply` command calculates this patch request
using the configuration file, the live configuration, and the
`last-applied-configuration` annotation stored in the live configuration.

### Merge patch calculation

The `kubectl apply` command writes the contents of the configuration file to the
`kubectl.kubernetes.io/last-applied-configuration` annotation. This
is used to identify fields that have been removed from the configuration
file and need to be cleared from the live configuration. Here are the steps used
to calculate which fields should be deleted or set:

1. Calculate the fields to delete. These are the fields present in
   `last-applied-configuration` and missing from the configuration file.
2. Calculate the fields to add or set. These are the fields present in
   the configuration file whose values don't match the live configuration.

Here's an example. Suppose this is the configuration file for a Deployment object:

Also, suppose this is the live configuration for the same Deployment object:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # note that the annotation does not contain replicas
    # because it was not updated through apply
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  replicas: 2 # written by scale
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
      # ...
```

Here are the merge calculations that would be performed by `kubectl apply`:

1. Calculate the fields to delete by reading values from
   `last-applied-configuration` and comparing them to values in the
   configuration file.
   Clear fields explicitly set to null in the local object configuration file
   regardless of whether they appear in the `last-applied-configuration`.
   In this example, `minReadySeconds` appears in the
   `last-applied-configuration` annotation, but does not appear in the configuration file.
   **Action:** Clear `minReadySeconds` from the live configuration.
2. Calculate the fields to set by reading values from the configuration
   file and comparing them to values in the live configuration. In this example,
   the value of `image` in the configuration file does not match
   the value in the live configuration. **Action:** Set the value of `image` in the live configuration.
3. Set the `last-applied-configuration` annotation to match the value
   of the configuration file.
4. Merge the results from 1, 2, 3 into a single patch request to the API server.

Here is the live configuration that is the result of the merge:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    # ...
    # The annotation contains the updated image to nginx 1.16.1,
    # but does not contain the updated replicas to 2
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.16.1","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
    # ...
spec:
  selector:
    matchLabels:
      # ...
      app: nginx
  replicas: 2 # Set by `kubectl scale`.  Ignored by `kubectl apply`.
  # minReadySeconds cleared by `kubectl apply`
  # ...
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.16.1 # Set by `kubectl apply`
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```

### How different types of fields are merged

How a particular field in a configuration file is merged with
the live configuration depends on the
type of the field. There are several types of fields:

- *primitive*: A field of type string, integer, or boolean.
  For example, `image` and `replicas` are primitive fields. **Action:** Replace.

- *map*, also called *object*: A field of type map or a complex type that contains subfields. For example, `labels`,
  `annotations`,`spec` and `metadata` are all maps. **Action:** Merge elements or subfields.

- *list*: A field containing a list of items that can be either primitive types or maps.
  For example, `containers`, `ports`, and `args` are lists. **Action:** Varies.

When `kubectl apply` updates a map or list field, it typically does
not replace the entire field, but instead updates the individual subelements.
For instance, when merging the `spec` on a Deployment, the entire `spec` is
not replaced. Instead the subfields of `spec`, such as `replicas`, are compared
and merged.

### Merging changes to primitive fields

Primitive fields are replaced or cleared.

`-` is used for "not applicable" because the value is not used.

| Field in object configuration file  | Field in live object configuration | Field in last-applied-configuration | Action                                    |
|-------------------------------------|------------------------------------|-------------------------------------|-------------------------------------------|
| Yes                                 | Yes                                | -                                   | Set live to configuration file value.  |
| Yes                                 | No                                 | -                                   | Set live to local configuration.           |
| No                                  | -                                  | Yes                                 | Clear from live configuration.            |
| No                                  | -                                  | No                                  | Do nothing. Keep live value.             |

### Merging changes to map fields

Fields that represent maps are merged by comparing each of the subfields or elements of the map:

`-` is used for "not applicable" because the value is not used.

| Key in object configuration file    | Key in live object configuration   | Field in last-applied-configuration | Action                           |
|-------------------------------------|------------------------------------|-------------------------------------|----------------------------------|
| Yes                                 | Yes                                | -                                   | Compare sub fields values.        |
| Yes                                 | No                                 | -                                   | Set live to local configuration.  |
| No                                  | -                                  | Yes                                 | Delete from live configuration.   |
| No                                  | -                                  | No                                  | Do nothing. Keep live value.     |

### Merging changes for fields of type list

Merging changes to a list uses one of three strategies:

* Replace the list if all its elements are primitives.
* Merge individual elements in a list of complex elements.
* Merge a list of primitive elements.

The choice of strategy is made on a per-field basis.

#### Replace the list if all its elements are primitives

Treat the list the same as a primitive field. Replace or delete the
entire list. This preserves ordering.

**Example:** Use `kubectl apply` to update the `args` field of a Container in a Pod. This sets
the value of `args` in the live configuration to the value in the configuration file.
Any `args` elements that had previously been added to the live configuration are lost.
The order of the `args` elements defined in the configuration file is
retained in the live configuration.

```yaml
# last-applied-configuration value
    args: ["a", "b"]

# configuration file value
    args: ["a", "c"]

# live configuration
    args: ["a", "b", "d"]

# result after merge
    args: ["a", "c"]
```

**Explanation:** The merge used the configuration file value as the new list value.

#### Merge individual elements of a list of complex elements:

Treat the list as a map, and treat a specific field of each element as a key.
Add, delete, or update individual elements. This does not preserve ordering.

This merge strategy uses a special tag on each field called a `patchMergeKey`. The
`patchMergeKey` is defined for each field in the Kubernetes source code:
types.go
When merging a list of maps, the field specified as the `patchMergeKey` for a given element
is used like a map key for that element.

**Example:** Use `kubectl apply` to update the `containers` field of a PodSpec.
This merges the list as though it was a map where each element is keyed
by `name`.

```yaml
# last-applied-configuration value
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-a # key: nginx-helper-a; will be deleted in result
      image: helper:1.3
    - name: nginx-helper-b # key: nginx-helper-b; will be retained
      image: helper:1.3

# configuration file value
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-b
      image: helper:1.3
    - name: nginx-helper-c # key: nginx-helper-c; will be added in result
      image: helper:1.3

# live configuration
    containers:
    - name: nginx
      image: nginx:1.16
    - name: nginx-helper-a
      image: helper:1.3
    - name: nginx-helper-b
      image: helper:1.3
      args: ["run"] # Field will be retained
    - name: nginx-helper-d # key: nginx-helper-d; will be retained
      image: helper:1.3

# result after merge
    containers:
    - name: nginx
      image: nginx:1.16
      # Element nginx-helper-a was deleted
    - name: nginx-helper-b
      image: helper:1.3
      args: ["run"] # Field was retained
    - name: nginx-helper-c # Element was added
      image: helper:1.3
    - name: nginx-helper-d # Element was ignored
      image: helper:1.3
```

**Explanation:**

- The container named "nginx-helper-a" was deleted because no container
  named "nginx-helper-a" appeared in the configuration file.
- The container named "nginx-helper-b" retained the changes to `args`
  in the live configuration. `kubectl apply` was able to identify
  that "nginx-helper-b" in the live configuration was the same
  "nginx-helper-b" as in the configuration file, even though their fields
  had different values (no `args` in the configuration file). This is
  because the `patchMergeKey` field value (name) was identical in both.
- The container named "nginx-helper-c" was added because no container
  with that name appeared in the live configuration, but one with
  that name appeared in the configuration file.
- The container named "nginx-helper-d" was retained because
  no element with that name appeared in the last-applied-configuration.

#### Merge a list of primitive elements

As of Kubernetes 1.5, merging lists of primitive elements is not supported.

Which of the above strategies is chosen for a given field is controlled by
the `patchStrategy` tag in types.go
If no `patchStrategy` is specified for a field of type list, then
the list is replaced.

TODO(pwittrock): Uncomment this for 1.6

- Treat the list as a set of primitives.  Replace or delete individual
  elements.  Does not preserve ordering.  Does not preserve duplicates.

**Example:** Using apply to update the `finalizers` field of ObjectMeta
keeps elements added to the live configuration.  Ordering of finalizers
is lost.
