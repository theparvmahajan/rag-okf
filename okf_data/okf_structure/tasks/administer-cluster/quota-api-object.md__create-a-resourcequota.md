---
id: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-resourcequota
kind: section
title: Create a ResourceQuota
source: tasks/administer-cluster/quota-api-object.md
url: https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/
heading: Create a ResourceQuota
parent: okf-structure/tasks/administer-cluster/quota-api-object
children: []
prev_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-persistentvolumeclaim
word_count: 78
---

Here is the configuration file for a ResourceQuota object:

Create the ResourceQuota:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects.yaml --namespace=quota-object-example
```

View detailed information about the ResourceQuota:

```shell
kubectl get resourcequota object-quota-demo --namespace=quota-object-example --output=yaml
```

The output shows that in the quota-object-example namespace, there can be at most
one PersistentVolumeClaim, at most two Services of type LoadBalancer, and no Services
of type NodePort.

```yaml
status:
  hard:
    persistentvolumeclaims: "1"
    services.loadbalancers: "2"
    services.nodeports: "0"
  used:
    persistentvolumeclaims: "0"
    services.loadbalancers: "0"
    services.nodeports: "0"
```
