---
id: okf-structure/tasks/access-application-cluster/service-access-application-cluster.md#cleanup
kind: section
title: Cleanup
source: tasks/access-application-cluster/service-access-application-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/
heading: Cleanup
parent: okf-structure/tasks/access-application-cluster/service-access-application-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/service-access-application-cluster.md#using-a-service-configuration-file
next_sibling: okf-structure/tasks/access-application-cluster/service-access-application-cluster.md#whatsnext
word_count: 34
---

To delete the Service, enter this command:

    kubectl delete services example-service

To delete the Deployment, the ReplicaSet, and the Pods that are running
the Hello World application, enter this command:

    kubectl delete deployment hello-world
