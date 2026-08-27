---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#interact-with-the-frontend-service
kind: section
title: Interact with the frontend Service
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Interact with the frontend Service
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-frontend
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#send-traffic-through-the-frontend
word_count: 110
---

Once you've created a Service of type LoadBalancer, you can use this
command to find the external IP:

```shell
kubectl get service frontend --watch
```

This displays the configuration for the `frontend` Service and watches for
changes. Initially, the external IP is listed as `<pending>`:

```
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)  AGE
frontend   LoadBalancer   10.51.252.116   <pending>     80/TCP   10s
```

As soon as an external IP is provisioned, however, the configuration updates
to include the new IP under the `EXTERNAL-IP` heading:

```
NAME       TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)  AGE
frontend   LoadBalancer   10.51.252.116   XXX.XXX.XXX.XXX    80/TCP   1m
```

That IP can now be used to interact with the `frontend` service from outside the
cluster.
