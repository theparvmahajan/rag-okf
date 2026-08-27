---
id: okf-structure/tutorials/stateless-application/guestbook.md#set-up-and-expose-the-guestbook-frontend
kind: section
title: Set up and Expose the Guestbook Frontend
source: tutorials/stateless-application/guestbook.md
url: https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
heading: Set up and Expose the Guestbook Frontend
parent: okf-structure/tutorials/stateless-application/guestbook
children: []
prev_sibling: okf-structure/tutorials/stateless-application/guestbook.md#start-up-the-redis-database
next_sibling: okf-structure/tutorials/stateless-application/guestbook.md#scale-the-web-frontend
word_count: 538
---

Now that you have the Redis storage of your guestbook up and running, start
the guestbook web servers. Like the Redis followers, the frontend is deployed
using a Kubernetes Deployment.

The guestbook app uses a PHP frontend. It is configured to communicate with
either the Redis follower or leader Services, depending on whether the request
is a read or a write. The frontend exposes a JSON interface, and serves a
jQuery-Ajax-based UX.

### Creating the Guestbook Frontend Deployment

1. Apply the frontend Deployment from the `frontend-deployment.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-deployment.yaml
   ```

1. Query the list of Pods to verify that the three frontend replicas are running:

   ```shell
   kubectl get pods -l app=guestbook -l tier=frontend
   ```

   The response should be similar to this:

   ```
   NAME                        READY   STATUS    RESTARTS   AGE
   frontend-85595f5bf9-5tqhb   1/1     Running   0          47s
   frontend-85595f5bf9-qbzwm   1/1     Running   0          47s
   frontend-85595f5bf9-zchwc   1/1     Running   0          47s
   ```

### Creating the Frontend Service

The `Redis` Services you applied is only accessible within the Kubernetes
cluster because the default type for a Service is
ClusterIP.
`ClusterIP` provides a single IP address for the set of Pods the Service is
pointing to. This IP address is accessible only within the cluster.

If you want guests to be able to access your guestbook, you must configure the
frontend Service to be externally visible, so a client can request the Service
from outside the Kubernetes cluster. However a Kubernetes user can use
`kubectl port-forward` to access the service even though it uses a
`ClusterIP`.

Some cloud providers, like Google Compute Engine or Google Kubernetes Engine,
support external load balancers. If your cloud provider supports load
balancers and you want to use it, uncomment `type: LoadBalancer`.

1. Apply the frontend Service from the `frontend-service.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/frontend-service.yaml
   ```

1. Query the list of Services to verify that the frontend Service is running:

   ```shell
   kubectl get services
   ```

   The response should be similar to this:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   frontend         ClusterIP   10.97.28.230    <none>        80/TCP     19s
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   5m48s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   11m
   ```

### Viewing the Frontend Service via `kubectl port-forward`

1. Run the following command to forward port `8080` on your local machine to port `80` on the service.

   ```shell
   kubectl port-forward svc/frontend 8080:80
   ```

   The response should be similar to this:

   ```
   Forwarding from 127.0.0.1:8080 -> 80
   Forwarding from [::1]:8080 -> 80
   ```

1. Load the page http://localhost:8080 in your browser to view your guestbook.

### Viewing the Frontend Service via `LoadBalancer`

If you deployed the `frontend-service.yaml` manifest with type: `LoadBalancer`
you need to find the IP address to view your Guestbook.

1. Run the following command to get the IP address for the frontend Service.

   ```shell
   kubectl get service frontend
   ```

   The response should be similar to this:

   ```
   NAME       TYPE           CLUSTER-IP      EXTERNAL-IP        PORT(S)        AGE
   frontend   LoadBalancer   10.51.242.136   109.197.92.229     80:32372/TCP   1m
   ```

1. Copy the external IP address, and load the page in your browser to view your guestbook.

Try adding some guestbook entries by typing in a message, and clicking Submit.
The message you typed appears in the frontend. This message indicates that
data is successfully added to Redis through the Services you created earlier.
