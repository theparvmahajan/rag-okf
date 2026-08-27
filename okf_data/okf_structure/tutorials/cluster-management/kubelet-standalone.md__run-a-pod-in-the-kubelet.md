---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#run-a-pod-in-the-kubelet
kind: section
title: Run a Pod in the kubelet
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Run a Pod in the kubelet
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#download-install-and-configure-the-components
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#where-to-look-for-more-details
word_count: 197
---

In standalone mode, you can run Pods using Pod manifests. The manifests can either
be on the local filesystem, or fetched via HTTP from a configuration source.

Create a manifest for a Pod:

```shell
cat <<EOF > static-web.yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-web
spec:
  containers:
    - name: web
      image: nginx
      ports:
        - name: web
          containerPort: 80
          protocol: TCP
EOF
```

Copy the `static-web.yaml` manifest file to the `/etc/kubernetes/manifests` directory.

```shell
sudo cp static-web.yaml /etc/kubernetes/manifests/
```

### Find out information about the kubelet and the Pod {#find-out-information}

The Pod networking plugin creates a network bridge (`cni0`) and a pair of `veth` interfaces
for each Pod (one of the pair is inside the newly made Pod, and the other is at the host level).

Query the kubelet's API endpoint at `http://localhost:10255/pods`:

```shell
curl http://localhost:10255/pods | jq '.'
```

To obtain the IP address of the `static-web` Pod:

```shell
curl http://localhost:10255/pods | jq '.items[].status.podIP'
```

The output is similar to:

```
"10.85.0.4"
```

Connect to the `nginx` server Pod on `http://<IP>:<Port>` (port 80 is the default), in this case:

```shell
curl http://10.85.0.4
```

The output is similar to:

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```
