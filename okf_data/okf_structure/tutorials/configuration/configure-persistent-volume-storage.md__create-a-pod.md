---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-a-pod
kind: section
title: Create a Pod
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: Create a Pod
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#create-a-persistentvolumeclaim
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#clean-up
word_count: 178
---

The next step is to create a Pod that uses your PersistentVolumeClaim as a volume.

Here is the configuration file for the Pod:

Notice that the Pod's configuration file specifies a PersistentVolumeClaim, but
it does not specify a PersistentVolume. From the Pod's point of view, the claim
is a volume.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/storage/pv-pod.yaml
```

Verify that the container in the Pod is running:

```shell
kubectl get pod task-pv-pod
```

Get a shell to the container running in your Pod:

```shell
kubectl exec -it task-pv-pod -- /bin/bash
```

In your shell, verify that nginx is serving the `index.html` file from the
hostPath volume:

```shell
# Be sure to run these 3 commands inside the root shell that comes from
# running "kubectl exec" in the previous step
apt update
apt install curl
curl http://localhost/
```

The output shows the text that you wrote to the `index.html` file on the
hostPath volume:

```
Hello from Kubernetes storage
```

If you see that message, you have successfully configured a Pod to
use storage from a PersistentVolumeClaim.
