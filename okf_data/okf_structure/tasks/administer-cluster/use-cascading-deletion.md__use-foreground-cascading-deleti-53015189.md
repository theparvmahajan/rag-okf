---
id: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-foreground-cascading-deletion-use-foreground-cascading-deletion
kind: section
title: Use foreground cascading deletion {#use-foreground-cascading-deletion}
source: tasks/administer-cluster/use-cascading-deletion.md
url: https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/
heading: Use foreground cascading deletion {#use-foreground-cascading-deletion}
parent: okf-structure/tasks/administer-cluster/use-cascading-deletion
children: []
prev_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#check-owner-references-on-your-pods
next_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-background-cascading-deletion-use-background-cascading-deletion
word_count: 129
---

By default, Kubernetes uses background cascading deletion
to delete dependents of an object. You can switch to foreground cascading deletion
using either `kubectl` or the Kubernetes API, depending on the Kubernetes
version your cluster runs. 

You can delete objects using foreground cascading deletion using `kubectl` or the
Kubernetes API.

**Using kubectl**

Run the following command:

```shell
kubectl delete deployment nginx-deployment --cascade=foreground
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```shell
   kubectl proxy --port=8080
   ```

1. Use `curl` to trigger deletion:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
       -H "Content-Type: application/json"
   ```

   The output contains a `foregroundDeletion` finalizer
   like this:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "metadata": {
       "name": "nginx-deployment",
       "namespace": "default",
       "uid": "d1ce1b02-cae8-4288-8a53-30e84d8fa505",
       "resourceVersion": "1363097",
       "creationTimestamp": "2021-07-08T20:24:37Z",
       "deletionTimestamp": "2021-07-08T20:27:39Z",
       "finalizers": [
         "foregroundDeletion"
       ]
       ...
   ```
