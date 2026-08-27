---
id: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-background-cascading-deletion-use-background-cascading-deletion
kind: section
title: Use background cascading deletion {#use-background-cascading-deletion}
source: tasks/administer-cluster/use-cascading-deletion.md
url: https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/
heading: Use background cascading deletion {#use-background-cascading-deletion}
parent: okf-structure/tasks/administer-cluster/use-cascading-deletion
children: []
prev_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-foreground-cascading-deletion-use-foreground-cascading-deletion
next_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#delete-owner-objects-and-orphan-dependents-set-orphan-deletion-policy
word_count: 137
---

1. Create a sample Deployment.
1. Use either `kubectl` or the Kubernetes API to delete the Deployment,
   depending on the Kubernetes version your cluster runs. 

You can delete objects using background cascading deletion using `kubectl`
or the Kubernetes API.

Kubernetes uses background cascading deletion by default, and does so
even if you run the following commands without the `--cascade` flag or the
`propagationPolicy` argument.

**Using kubectl**

Run the following command:

```shell
kubectl delete deployment nginx-deployment --cascade=background
```

**Using the Kubernetes API**

1. Start a local proxy session:

   ```shell
   kubectl proxy --port=8080
   ```

1. Use `curl` to trigger deletion:

   ```shell
   curl -X DELETE localhost:8080/apis/apps/v1/namespaces/default/deployments/nginx-deployment \
       -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Background"}' \
       -H "Content-Type: application/json"
   ```

   The output is similar to this:

   ```
   "kind": "Status",
   "apiVersion": "v1",
   ...
   "status": "Success",
   "details": {
       "name": "nginx-deployment",
       "group": "apps",
       "kind": "deployments",
       "uid": "cc9eefb9-2d49-4445-b1c1-d261c9396456"
   }
   ```
