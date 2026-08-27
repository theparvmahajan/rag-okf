---
id: okf-structure/tasks/configure-pod-container/static-pod.md#observe-static-pod-behavior-behavior-of-static-pods
kind: section
title: Observe static pod behavior {#behavior-of-static-pods}
source: tasks/configure-pod-container/static-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/
heading: Observe static pod behavior {#behavior-of-static-pods}
parent: okf-structure/tasks/configure-pod-container/static-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#create-a-static-pod-static-pod-creation
next_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#dynamic-addition-and-removal-of-static-pods
word_count: 402
---

When the kubelet starts, it automatically starts all defined static Pods. As you have
defined a static Pod and restarted the kubelet, the new static Pod should
already be running.

You can view running containers (including static Pods) by running (on the node):
```shell
# Run this command on the node where the kubelet is running
crictl ps
```

The output might be something like:

```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
129fd7d382018   docker.io/library/nginx@sha256:...    11 minutes ago    Running    web     0          34533c6729106
```

`crictl` outputs the image URI and SHA-256 checksum. `NAME` will look more like:
`docker.io/library/nginx@sha256:0d17b565c37bcbd895e9d92315a05c1c3c9a29f762b011a10c54a66cd53c9b31`.

You can see the mirror Pod on the API server:

```shell
kubectl get pods
```
```console
NAME                  READY   STATUS    RESTARTS        AGE
static-web-my-node1   1/1     Running   0               2m
```

Make sure the kubelet has permission to create the mirror Pod in the API server.
If not, the creation request is rejected by the API server.

Labels from the static Pod are
propagated into the mirror Pod. You can use those labels as normal via
selectors, etc.

If you try to use `kubectl` to delete the mirror Pod from the API server,
the kubelet _doesn't_ remove the static Pod:

```shell
kubectl delete pod static-web-my-node1
```
```console
pod "static-web-my-node1" deleted
```
You can see that the Pod is still running:
```shell
kubectl get pods
```
```console
NAME                  READY   STATUS    RESTARTS   AGE
static-web-my-node1   1/1     Running   0          4s
```

Back on your node where the kubelet is running, you can try to stop the container manually.
You'll see that, after a time, the kubelet will notice and will restart the Pod
automatically:

```shell
# Run these commands on the node where the kubelet is running
crictl stop 129fd7d382018 # replace with the ID of your container
sleep 20
crictl ps
```

```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
89db4553e1eeb   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```
Once you identify the right container, you can get the logs for that container with `crictl`:

```shell
# Run these commands on the node where the container is running
crictl logs <container_id>
```

```console
10.240.0.48 - - [16/Nov/2022:12:45:49 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nov/2022:12:45:50 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
10.240.0.48 - - [16/Nove/2022:12:45:51 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.47.0" "-"
```

To find more about how to debug using `crictl`, please visit
_Debugging Kubernetes nodes with crictl_.
