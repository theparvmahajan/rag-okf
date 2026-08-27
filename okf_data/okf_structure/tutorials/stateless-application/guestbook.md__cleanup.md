---
id: okf-structure/tutorials/stateless-application/guestbook.md#cleanup
kind: section
title: Cleanup
source: tutorials/stateless-application/guestbook.md
url: https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
heading: Cleanup
parent: okf-structure/tutorials/stateless-application/guestbook
children: []
prev_sibling: okf-structure/tutorials/stateless-application/guestbook.md#scale-the-web-frontend
next_sibling: okf-structure/tutorials/stateless-application/guestbook.md#whatsnext
word_count: 105
---

Deleting the Deployments and Services also deletes any running Pods. Use
labels to delete multiple resources with one command.

1. Run the following commands to delete all Pods, Deployments, and Services.

   ```shell
   kubectl delete deployment -l app=redis
   kubectl delete service -l app=redis
   kubectl delete deployment frontend
   kubectl delete service frontend
   ```

   The response should look similar to this:

   ```
   deployment.apps "redis-follower" deleted
   deployment.apps "redis-leader" deleted
   deployment.apps "frontend" deleted
   service "frontend" deleted
   ```

1. Query the list of Pods to verify that no Pods are running:

   ```shell
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   No resources found in default namespace.
   ```
