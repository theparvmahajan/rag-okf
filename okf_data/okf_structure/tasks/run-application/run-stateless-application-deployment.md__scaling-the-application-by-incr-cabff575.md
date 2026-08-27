---
id: okf-structure/tasks/run-application/run-stateless-application-deployment.md#scaling-the-application-by-increasing-the-replica-count
kind: section
title: Scaling the application by increasing the replica count
source: tasks/run-application/run-stateless-application-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
heading: Scaling the application by increasing the replica count
parent: okf-structure/tasks/run-application/run-stateless-application-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#updating-the-deployment
next_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#deleting-a-deployment
word_count: 108
---

You can increase the number of Pods in your Deployment by applying a new YAML
file. This YAML file sets `replicas` to 4, which specifies that the Deployment
should have four Pods:

1. Apply the new YAML file:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment-scale.yaml
   ```

1. Verify that the Deployment has four Pods:

   ```shell
   kubectl get pods -l app=nginx
   ```

   The output is similar to this:

   ```
   NAME                               READY     STATUS    RESTARTS   AGE
   nginx-deployment-148880595-4zdqq   1/1       Running   0          25s
   nginx-deployment-148880595-6zgi1   1/1       Running   0          25s
   nginx-deployment-148880595-fxcez   1/1       Running   0          2m
   nginx-deployment-148880595-rwovn   1/1       Running   0          2m
   ```

For detailed scaling procedures including scaling down and scaling to zero, see
Scale a Deployment Manually.
