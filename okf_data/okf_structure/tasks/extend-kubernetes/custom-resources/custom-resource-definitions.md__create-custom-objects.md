---
id: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#create-custom-objects
kind: section
title: Create custom objects
source: tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
heading: Create custom objects
parent: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#create-a-customresourcedefinition
next_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md#delete-a-customresourcedefinition
word_count: 230
---

After the CustomResourceDefinition object has been created, you can create
custom objects. Custom objects can contain custom fields. These fields can
contain arbitrary JSON.
In the following example, the `cronSpec` and `image` custom fields are set in a
custom object of kind `CronTab`.  The kind `CronTab` comes from the spec of the
CustomResourceDefinition object you created above.

If you save the following YAML to `my-crontab.yaml`:

```yaml
apiVersion: "stable.example.com/v1"
kind: CronTab
metadata:
  name: my-new-cron-object
spec:
  cronSpec: "* * * * */5"
  image: my-awesome-cron-image
```

and create it:

```shell
kubectl apply -f my-crontab.yaml
```

You can then manage your CronTab objects using kubectl. For example:

```shell
kubectl get crontab
```

Should print a list like this:

```none
NAME                 AGE
my-new-cron-object   6s
```

Resource names are not case-sensitive when using kubectl, and you can use either
the singular or plural forms defined in the CRD, as well as any short names.

You can also view the raw YAML data:

```shell
kubectl get ct -o yaml
```

You should see that it contains the custom `cronSpec` and `image` fields
from the YAML you used to create it:

```yaml
apiVersion: v1
items:
- apiVersion: stable.example.com/v1
  kind: CronTab
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"stable.example.com/v1","kind":"CronTab","metadata":{"annotations":{},"name":"my-new-cron-object","namespace":"default"},"spec":{"cronSpec":"* * * * */5","image":"my-awesome-cron-image"}}
    creationTimestamp: "2021-06-20T07:35:27Z"
    generation: 1
    name: my-new-cron-object
    namespace: default
    resourceVersion: "1326"
    uid: 9aab1d66-628e-41bb-a422-57b8b3b1f5a9
  spec:
    cronSpec: '* * * * */5'
    image: my-awesome-cron-image
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
```
