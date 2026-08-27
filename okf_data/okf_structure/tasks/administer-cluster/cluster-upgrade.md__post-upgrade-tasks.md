---
id: okf-structure/tasks/administer-cluster/cluster-upgrade.md#post-upgrade-tasks
kind: section
title: Post-upgrade tasks
source: tasks/administer-cluster/cluster-upgrade.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/
heading: Post-upgrade tasks
parent: okf-structure/tasks/administer-cluster/cluster-upgrade
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cluster-upgrade.md#upgrade-approaches
next_sibling: null
word_count: 222
---

### Switch your cluster's storage API version

The objects that are serialized into etcd for a cluster's internal
representation of the Kubernetes resources active in the cluster are
written using a particular version of the API.

When the supported API changes, these objects may need to be rewritten
in the newer API. Failure to do this will eventually result in resources
that are no longer decodable or usable by the Kubernetes API server.

For each affected object, fetch it using the latest supported API and then
write it back also using the latest supported API.

### Update manifests

Upgrading to a new Kubernetes version can provide new APIs.

You can use `kubectl convert` command to convert manifests between different API versions.
For example:

```shell
kubectl convert -f pod.yaml --output-version v1
```

The `kubectl` tool replaces the contents of `pod.yaml` with a manifest that sets `kind` to
Pod (unchanged), but with a revised `apiVersion`.

### Device Plugins

If your cluster is running device plugins and the node needs to be upgraded to a Kubernetes
release with a newer device plugin API version, device plugins must be upgraded to support
both version before the node is upgraded in order to guarantee that device allocations
continue to complete successfully during the upgrade.

Refer to API compatibility and Kubelet Device Manager API Versions for more details.
