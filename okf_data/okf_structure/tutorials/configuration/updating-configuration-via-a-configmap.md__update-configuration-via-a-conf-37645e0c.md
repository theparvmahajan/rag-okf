---
id: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-a-configmap-in-a-pod-possessing-a-sidecar-container-rollout-configmap-sidecar
kind: section
title: Update configuration via a ConfigMap in a Pod possessing a sidecar container
  {#rollout-configmap-sidecar}
source: tutorials/configuration/updating-configuration-via-a-configmap.md
url: https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/
heading: Update configuration via a ConfigMap in a Pod possessing a sidecar container
  {#rollout-configmap-sidecar}
parent: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap
children: []
prev_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-a-configmap-in-a-multi-container-pod-rollout-configmap-multiple-containers
next_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-an-immutable-configmap-that-is-mounted-as-a-volume-rollout-configmap-immutable-volume
word_count: 546
---

The above scenario can be replicated by using a Sidecar Container
as a helper container to write the HTML file.  
As a Sidecar Container is conceptually an Init Container, it is guaranteed to start before the main web server container.  
This ensures that the HTML file is always available when the web server is ready to serve it.  

If you are continuing from the previous scenario, you can reuse the ConfigMap named `color` for this scenario.  
If you are executing this scenario independently, use the `kubectl create configmap` command to create a ConfigMap
from literal values:

```shell
kubectl create configmap color --from-literal=color=blue
```

Below is an example manifest for a Deployment that manages a set of Pods, each with a main container and
a sidecar container. The two containers share an `emptyDir` volume that they use to communicate.
The main container runs a web server (NGINX). The mount path for the shared volume in the web server container
is `/usr/share/nginx/html`. The second container is a Sidecar Container based on Alpine Linux which acts as
a helper container. For this container the `emptyDir` volume is mounted at `/pod-data`. The Sidecar Container
writes a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

Create the Deployment:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-and-sidecar-container.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
selector):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-sidecar-container
```

You should see an output similar to:

```
NAME                                           READY   STATUS    RESTARTS   AGE
configmap-sidecar-container-5fb59f558b-87rp7   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-ccs7s   2/2     Running   0          94s
configmap-sidecar-container-5fb59f558b-wnmgk   2/2     Running   0          94s
```

Expose the Deployment (the `kubectl` tool creates a
Service for you):

```shell
kubectl expose deployment configmap-sidecar-container --name=configmap-sidecar-service --port=8081 --target-port=80
```

Use `kubectl` to forward the port:

```shell
# this stays running in the background
kubectl port-forward service/configmap-sidecar-service 8081:8081 &
```

Access the service.

```shell
curl http://localhost:8081
```

You should see an output similar to:

```
Sat Feb 17 13:09:05 UTC 2024 My preferred color is blue
```

Edit the ConfigMap:

```shell
kubectl edit configmap color
```

In the editor that appears, change the value of key `color` from `blue` to `green`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```yaml
apiVersion: v1
data:
  color: green
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-02-17T12:20:30Z"
  name: color
  namespace: default
  resourceVersion: "1054"
  uid: e40bb34c-58df-4280-8bea-6ed16edccfaa
```

Loop over the service URL for few seconds.

```shell
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8081; sleep 10; done
```

You should see the output change as follows:

```
Sat Feb 17 13:12:35 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:45 UTC 2024 My preferred color is blue
Sat Feb 17 13:12:55 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:05 UTC 2024 My preferred color is blue
Sat Feb 17 13:13:15 UTC 2024 My preferred color is green
Sat Feb 17 13:13:25 UTC 2024 My preferred color is green
Sat Feb 17 13:13:35 UTC 2024 My preferred color is green
```
