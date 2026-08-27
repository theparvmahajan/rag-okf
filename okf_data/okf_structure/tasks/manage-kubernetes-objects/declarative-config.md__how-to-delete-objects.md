---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-delete-objects
kind: section
title: How to delete objects
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: How to delete objects
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-update-objects
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-view-an-object
word_count: 797
---

There are two approaches to delete objects managed by `kubectl apply`.

### Recommended: `kubectl delete -f <filename>`

Manually deleting objects using the imperative command is the recommended
approach, as it is more explicit about what is being deleted, and less likely
to result in the user deleting something unintentionally:

```shell
kubectl delete -f <filename>
```

### Alternative: `kubectl apply -f <directory> --prune`

As an alternative to `kubectl delete`, you can use `kubectl apply` to identify objects to be deleted after
their manifests have been removed from a directory in the local filesystem.

In Kubernetes , there are two pruning modes available in kubectl apply:

- Allowlist-based pruning: This mode has existed since kubectl v1.5 but is still
  in alpha due to usability, correctness and performance issues with its design.
  The ApplySet-based mode is designed to replace it.
- ApplySet-based pruning: An _apply set_ is a server-side object (by default, a Secret)
  that kubectl can use to accurately and efficiently track set membership across **apply**
  operations. This mode was introduced in alpha in kubectl v1.27 as a replacement for allowlist-based pruning.

Take care when using `--prune` with `kubectl apply` in allow list mode. Which
objects are pruned depends on the values of the `--prune-allowlist`, `--selector`
and `--namespace` flags, and relies on dynamic discovery of the objects in scope.
Especially if flag values are changed between invocations, this can lead to objects
being unexpectedly deleted or retained.

To use allowlist-based pruning, add the following flags to your `kubectl apply` invocation:

- `--prune`: Delete previously applied objects that are not in the set passed to the current invocation.
- `--prune-allowlist`: A list of group-version-kinds (GVKs) to consider for pruning.
  This flag is optional but strongly encouraged, as its default value is a partial
  list of both namespaced and cluster-scoped types, which can lead to surprising results.
- `--selector/-l`: Use a label selector to constrain the set of objects selected
  for pruning. This flag is optional but strongly encouraged.
- `--all`: use instead of `--selector/-l` to explicitly select all previously
  applied objects of the allowlisted types.

Allowlist-based pruning queries the API server for all objects of the allowlisted GVKs that match the given labels (if any), and attempts to match the returned live object configurations against the object
manifest files. If an object matches the query, and it does not have a
manifest in the directory, and it has a `kubectl.kubernetes.io/last-applied-configuration` annotation,
it is deleted.

```shell
kubectl apply -f <directory> --prune -l <labels> --prune-allowlist=<gvk-list>
```

Apply with prune should only be run against the root directory
containing the object manifests. Running against sub-directories
can cause objects to be unintentionally deleted if they were previously applied, 
have the labels given (if any), and do not appear in the subdirectory.

`kubectl apply --prune --applyset` is in alpha, and backwards incompatible
changes might be introduced in subsequent releases.

To use ApplySet-based pruning, set the `KUBECTL_APPLYSET=true` environment variable,
and add the following flags to your `kubectl apply` invocation:
- `--prune`: Delete previously applied objects that are not in the set passed
  to the current invocation.
- `--applyset`: The name of an object that kubectl can use to accurately and
  efficiently track set membership across `apply` operations.

```shell
KUBECTL_APPLYSET=true kubectl apply -f <directory> --prune --applyset=<name>
```

By default, the type of the ApplySet parent object used is a Secret. However,
ConfigMaps can also be used in the format: `--applyset=configmaps/<name>`.
When using a Secret or ConfigMap, kubectl will create the object if it does not already exist.

It is also possible to use custom resources as ApplySet parent objects. To enable
this, label the Custom Resource Definition (CRD) that defines the resource you want
to use with the following: `applyset.kubernetes.io/is-parent-type: true`. Then, create
the object you want to use as an ApplySet parent (kubectl does not do this automatically
for custom resources). Finally, refer to that object in the applyset flag as follows:
`--applyset=<resource>.<group>/<name>` (for example, `widgets.custom.example.com/widget-name`).

With ApplySet-based pruning, kubectl adds the `applyset.kubernetes.io/part-of=<parentID>`
label to each object in the set before they are sent to the server. For performance reasons,
it also collects the list of resource types and namespaces that the set contains and adds
these in annotations on the live parent object. Finally, at the end of the apply operation,
it queries the API server for objects of those types in those namespaces
(or in the cluster scope, as applicable) that belong to the set, as defined by the
`applyset.kubernetes.io/part-of=<parentID>` label.

Caveats and restrictions:

- Each object may be a member of at most one set.
- The `--namespace` flag is required when using any namespaced parent, including
  the default Secret.  This means that ApplySets spanning multiple namespaces must
  use a cluster-scoped custom resource as the parent object.
- To safely use ApplySet-based pruning with multiple directories,
  use a unique ApplySet name for each.
