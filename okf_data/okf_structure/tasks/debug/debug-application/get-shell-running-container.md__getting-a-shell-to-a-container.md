---
id: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#getting-a-shell-to-a-container
kind: section
title: Getting a shell to a container
source: tasks/debug/debug-application/get-shell-running-container.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/
heading: Getting a shell to a container
parent: okf-structure/tasks/debug/debug-application/get-shell-running-container
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-application/get-shell-running-container.md#writing-the-root-page-for-nginx
word_count: 149
---

In this exercise, you create a Pod that has one container. The container
runs the nginx image. Here is the configuration file for the Pod:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/application/shell-demo.yaml
```

Verify that the container is running:

```shell
kubectl get pod shell-demo
```

Get a shell to the running container:

```shell
kubectl exec --stdin --tty shell-demo -- /bin/bash
```

The double dash (`--`) separates the arguments you want to pass to the command from the kubectl arguments.

In your shell, list the root directory:

```shell
# Run this inside the container
ls /
```

In your shell, experiment with other commands. Here are
some examples:

```shell
# You can run these example commands inside the container
ls /
cat /proc/mounts
cat /proc/1/maps
apt-get update
apt-get install -y tcpdump
tcpdump
apt-get install -y lsof
lsof
apt-get install -y procps
ps aux
ps aux | grep nginx
```
