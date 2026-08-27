---
id: okf-structure/tasks/run-application/run-stateless-application-deployment.md#updating-the-deployment
kind: section
title: Updating the deployment
source: tasks/run-application/run-stateless-application-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
heading: Updating the deployment
parent: okf-structure/tasks/run-application/run-stateless-application-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#creating-and-exploring-an-nginx-deployment
next_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#scaling-the-application-by-increasing-the-replica-count
word_count: 58
---

You can update the deployment by applying a new YAML file. This YAML file
specifies that the deployment should be updated to use nginx 1.16.1.

1. Apply the new YAML file:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment-update.yaml
   ```

1. Watch the deployment create pods with new names and delete the old pods:

   ```shell
   kubectl get pods -l app=nginx
   ```
