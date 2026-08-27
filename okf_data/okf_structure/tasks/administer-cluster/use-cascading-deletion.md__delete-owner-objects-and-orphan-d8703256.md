---
id: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#delete-owner-objects-and-orphan-dependents-set-orphan-deletion-policy
kind: section
title: Delete owner objects and orphan dependents {#set-orphan-deletion-policy}
source: tasks/administer-cluster/use-cascading-deletion.md
url: https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/
heading: Delete owner objects and orphan dependents {#set-orphan-deletion-policy}
parent: okf-structure/tasks/administer-cluster/use-cascading-deletion
children: []
prev_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-background-cascading-deletion-use-background-cascading-deletion
next_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#whatsnext
word_count: 136
---

By default, when you tell Kubernetes to delete an object, the
controller also deletes
dependent objects. You can make Kubernetes *orphan* these dependents using
`kubectl` or the Kubernetes API, depending on the Kubernetes version your
cluster runs. 

**Using kubectl**

Run the following command:

```shell
kubectl delete deployment nginx-deployment --cascade=orphan
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```shell
   kubectl proxy --port=8080
   ```

1. Use `curl` to trigger deletion:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
       -H "Content-Type: application/json"
   ```

   The output contains `orphan` in the `finalizers` field, similar to this:

   ```
   "kind": "Deployment",
   "apiVersion": "apps/v1",
   "namespace": "default",
   "uid": "6f577034-42a0-479d-be21-78018c466f1f",
   "creationTimestamp": "2021-07-09T16:46:37Z",
   "deletionTimestamp": "2021-07-09T16:47:08Z",
   "deletionGracePeriodSeconds": 0,
   "finalizers": [
     "orphan"
   ],
   ...
   ```

You can check that the Pods managed by the Deployment are still running:

```shell
kubectl get pods -l app=nginx
```
