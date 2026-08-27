---
id: okf-structure/tasks/configure-pod-container/static-pod.md#dynamic-addition-and-removal-of-static-pods
kind: section
title: Dynamic addition and removal of static pods
source: tasks/configure-pod-container/static-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/
heading: Dynamic addition and removal of static pods
parent: okf-structure/tasks/configure-pod-container/static-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#observe-static-pod-behavior-behavior-of-static-pods
next_sibling: okf-structure/tasks/configure-pod-container/static-pod.md#whatsnext
word_count: 89
---

The running kubelet periodically scans the configured directory
(`/etc/kubernetes/manifests` in our example) for changes and
adds/removes Pods as files appear/disappear in this directory.

```shell
# This assumes you are using filesystem-hosted static Pod configuration
# Run these commands on the node where the container is running
mv /etc/kubernetes/manifests/static-web.yaml /tmp
sleep 20
crictl ps
# You see that no nginx container is running
mv /tmp/static-web.yaml  /etc/kubernetes/manifests/
sleep 20
crictl ps
```
```console
CONTAINER       IMAGE                                 CREATED           STATE      NAME    ATTEMPT    POD ID
f427638871c35   docker.io/library/nginx@sha256:...    19 seconds ago    Running    web     1          34533c6729106
```
