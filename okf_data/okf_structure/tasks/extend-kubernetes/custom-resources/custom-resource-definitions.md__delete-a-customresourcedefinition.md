---
id: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#delete-a-customresourcedefinition
kind: section
title: Delete a CustomResourceDefinition
source: tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
heading: Delete a CustomResourceDefinition
parent: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#create-custom-objects
next_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#specifying-a-structural-schema
word_count: 64
---

When you delete a CustomResourceDefinition, the server will uninstall the RESTful API endpoint
and delete all custom objects stored in it.

```shell
kubectl delete -f resourcedefinition.yaml
kubectl get crontabs
```

```none
Error from server (NotFound): Unable to list {"stable.example.com" "v1" "crontabs"}: the server could not
find the requested resource (get crontabs.stable.example.com)
```

If you later recreate the same CustomResourceDefinition, it will start out empty.
