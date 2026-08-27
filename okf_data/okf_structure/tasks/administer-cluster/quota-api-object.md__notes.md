---
id: okf-structure/tasks/administer-cluster/quota-api-object.md#notes
kind: section
title: Notes
source: tasks/administer-cluster/quota-api-object.md
url: https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/
heading: Notes
parent: okf-structure/tasks/administer-cluster/quota-api-object
children: []
prev_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#attempt-to-create-a-second-persistentvolumeclaim
next_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#clean-up
word_count: 32
---

These are the strings used to identify API resources that can be constrained
by quotas:

StringAPI Object
"pods"Pod
"services"Service
"replicationcontrollers"ReplicationController
"resourcequotas"ResourceQuota
"secrets"Secret
"configmaps"ConfigMap
"persistentvolumeclaims"PersistentVolumeClaim
"services.nodeports"Service of type NodePort
"services.loadbalancers"Service of type LoadBalancer
