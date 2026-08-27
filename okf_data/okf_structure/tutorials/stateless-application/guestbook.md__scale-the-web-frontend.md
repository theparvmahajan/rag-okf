---
id: okf-structure/tutorials/stateless-application/guestbook.md#scale-the-web-frontend
kind: section
title: Scale the Web Frontend
source: tutorials/stateless-application/guestbook.md
url: https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
heading: Scale the Web Frontend
parent: okf-structure/tutorials/stateless-application/guestbook
children: []
prev_sibling: okf-structure/tutorials/stateless-application/guestbook.md#set-up-and-expose-the-guestbook-frontend
next_sibling: okf-structure/tutorials/stateless-application/guestbook.md#cleanup
word_count: 192
---

You can scale up or down as needed because your servers are defined as a
Service that uses a Deployment controller.

1. Run the following command to scale up the number of frontend Pods:

   ```shell
   kubectl scale deployment frontend --replicas=5
   ```

1. Query the list of Pods to verify the number of frontend Pods running:

   ```shell
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5df5m        1/1     Running   0          83s
   frontend-85595f5bf9-7zmg5        1/1     Running   0          83s
   frontend-85595f5bf9-cpskg        1/1     Running   0          15m
   frontend-85595f5bf9-l2l54        1/1     Running   0          14m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          14m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          97m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          97m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          108m
   ```

1. Run the following command to scale down the number of frontend Pods:

   ```shell
   kubectl scale deployment frontend --replicas=2
   ```

1. Query the list of Pods to verify the number of frontend Pods running:

   ```shell
   kubectl get pods
   ```

   The response should look similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-cpskg        1/1     Running   0          16m
   frontend-85595f5bf9-l9c8z        1/1     Running   0          15m
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          98m
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          98m
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          109m
   ```
