---
id: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-a-configmap-in-a-multi-container-pod-rollout-configmap-multiple-containers
kind: section
title: Update configuration via a ConfigMap in a multi-container Pod {#rollout-configmap-multiple-containers}
source: tutorials/configuration/updating-configuration-via-a-configmap.md
url: https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/
heading: Update configuration via a ConfigMap in a multi-container Pod {#rollout-configmap-multiple-containers}
parent: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap
children: []
prev_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-environment-variables-of-a-pod-via-a-configmap-rollout-configmap-env
next_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-a-configmap-in-a-pod-possessing-a-sidecar-container-rollout-configmap-sidecar
word_count: 450
---

Use the `kubectl create configmap` command to create a ConfigMap from
literal values:

```shell
kubectl create configmap color --from-literal=color=red
```

Below is an example manifest for a Deployment that manages a set of Pods, each with two containers.
The two containers share an `emptyDir` volume that they use to communicate.
The first container runs a web server (`nginx`). The mount path for the shared volume in the
web server container is `/usr/share/nginx/html`. The second helper container is based on `alpine`,
and for this container the `emptyDir` volume is mounted at `/pod-data`. The helper container writes
a file in HTML that has its content based on a ConfigMap. The web server container serves the HTML via HTTP.

Create the Deployment:

```shell
kubectl apply -f https://k8s.io/examples/deployments/deployment-with-configmap-two-containers.yaml
```

Check the pods for this Deployment to ensure they are ready (matching by
selector):

```shell
kubectl get pods --selector=app.kubernetes.io/name=configmap-two-containers
```

You should see an output similar to:

```
NAME                                        READY   STATUS    RESTARTS   AGE
configmap-two-containers-565fb6d4f4-2xhxf   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-g5v4j   2/2     Running   0          20s
configmap-two-containers-565fb6d4f4-mzsmf   2/2     Running   0          20s
```

Expose the Deployment (the `kubectl` tool creates a
Service for you):

```shell
kubectl expose deployment configmap-two-containers --name=configmap-service --port=8080 --target-port=80
```

Use `kubectl` to forward the port:

```shell
# this stays running in the background
kubectl port-forward service/configmap-service 8080:8080 &
```

Access the service.

```shell
curl http://localhost:8080
```

You should see an output similar to:

```
Fri Jan  5 08:08:22 UTC 2024 My preferred color is red
```

Edit the ConfigMap:

```shell
kubectl edit configmap color
```

In the editor that appears, change the value of key `color` from `red` to `blue`. Save your changes.
The kubectl tool updates the ConfigMap accordingly (if you see an error, try again).

Here's an example of how that manifest could look after you edit it:

```yaml
apiVersion: v1
data:
  color: blue
kind: ConfigMap
# You can leave the existing metadata as they are.
# The values you'll see won't exactly match these.
metadata:
  creationTimestamp: "2024-01-05T08:12:05Z"
  name: color
  namespace: configmap
  resourceVersion: "1801272"
  uid: 80d33e4a-cbb4-4bc9-ba8c-544c68e425d6
```

Loop over the service URL for few seconds.

```shell
# Cancel this when you're happy with it (Ctrl-C)
while true; do curl --connect-timeout 7.5 http://localhost:8080; sleep 10; done
```

You should see the output change as follows:

```
Fri Jan  5 08:14:00 UTC 2024 My preferred color is red
Fri Jan  5 08:14:02 UTC 2024 My preferred color is red
Fri Jan  5 08:14:20 UTC 2024 My preferred color is red
Fri Jan  5 08:14:22 UTC 2024 My preferred color is red
Fri Jan  5 08:14:32 UTC 2024 My preferred color is blue
Fri Jan  5 08:14:43 UTC 2024 My preferred color is blue
Fri Jan  5 08:15:00 UTC 2024 My preferred color is blue
```
