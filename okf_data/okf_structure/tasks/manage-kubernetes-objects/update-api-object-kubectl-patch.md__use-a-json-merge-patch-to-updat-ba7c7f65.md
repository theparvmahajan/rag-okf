---
id: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#use-a-json-merge-patch-to-update-a-deployment
kind: section
title: Use a JSON merge patch to update a Deployment
source: tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/
heading: Use a JSON merge patch to update a Deployment
parent: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#use-a-strategic-merge-patch-to-update-a-deployment
next_sibling: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#use-strategic-merge-patch-to-update-a-deployment-using-the-retainkeys-strategy
word_count: 261
---

A strategic merge patch is different from a
JSON merge patch.
With a JSON merge patch, if you
want to update a list, you have to specify the entire new list. And the new list completely
replaces the existing list.

The `kubectl patch` command has a `type` parameter that you can set to one of these values:

  Parameter valueMerge type
  jsonJSON Patch, RFC 6902
  mergeJSON Merge Patch, RFC 7386
  strategicStrategic merge patch

For a comparison of JSON patch and JSON merge patch, see
JSON Patch and JSON Merge Patch.

The default value for the `type` parameter is `strategic`. So in the preceding exercise, you
did a strategic merge patch.

Next, do a JSON merge patch on your same Deployment. Create a file named `patch-file-2.yaml`
that has this content:

```yaml
spec:
  template:
    spec:
      containers:
      - name: patch-demo-ctr-3
        image: gcr.io/google-samples/hello-app:2.0
```

In your patch command, set `type` to `merge`:

```shell
kubectl patch deployment patch-demo --type merge --patch-file patch-file-2.yaml
```

View the patched Deployment:

```shell
kubectl get deployment patch-demo --output yaml
```

The `containers` list that you specified in the patch has only one Container.
The output shows that your list of one Container replaced the existing `containers` list.

```yaml
spec:
  containers:
  - image: gcr.io/google-samples/hello-app:2.0
    ...
    name: patch-demo-ctr-3
```

List the running Pods:

```shell
kubectl get pods
```

In the output, you can see that the existing Pods were terminated, and new Pods
were created. The `1/1` indicates that each new Pod is running only one Container.

```shell
NAME                          READY     STATUS    RESTARTS   AGE
patch-demo-1307768864-69308   1/1       Running   0          1m
patch-demo-1307768864-c86dc   1/1       Running   0          1m
```
