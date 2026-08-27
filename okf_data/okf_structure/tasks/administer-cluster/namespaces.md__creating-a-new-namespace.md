---
id: okf-structure/tasks/administer-cluster/namespaces.md#creating-a-new-namespace
kind: section
title: Creating a new namespace
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Creating a new namespace
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#viewing-namespaces
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#deleting-a-namespace
word_count: 125
---

Avoid creating namespace with prefix `kube-`, since it is reserved for Kubernetes system namespaces.

Create a new YAML file called `my-namespace.yaml` with the contents:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: <insert-namespace-name-here>
```
Then run:

```shell
kubectl create -f ./my-namespace.yaml
```

Alternatively, you can create namespace using below command:

```shell
kubectl create namespace <insert-namespace-name-here>
``` 

The name of your namespace must be a valid
DNS label.

There is an optional field `finalizers`, which allows observables to purge resources whenever the
namespace is deleted. Keep in mind that if you specify a nonexistent finalizer, the namespace will
be created but will get stuck in the `Terminating` state if the user tries to delete it.

More information on `finalizers` can be found in the namespace
design doc.
