---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-via-a-shell-on-the-node-node-shell-session
kind: section
title: Debugging via a shell on the node {#node-shell-session}
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Debugging via a shell on the node {#node-shell-session}
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-using-a-copy-of-the-pod
next_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-a-pod-or-node-while-applying-a-profile-debugging-profiles
word_count: 326
---

If none of these approaches work, you can find the Node on which the Pod is
running and create a Pod running on the Node. To create
an interactive shell on a Node using `kubectl debug`, run:

```shell
kubectl debug node/mynode -it --image=ubuntu
```

```
Creating debugging pod node-debugger-mynode-pdx84 with container debugger on node mynode.
If you don't see a command prompt, try pressing enter.
root@ek8s:/#
```

When creating a debugging session on a node, keep in mind that:

* `kubectl debug` automatically generates the name of the new Pod based on
  the name of the Node.
* The root filesystem of the Node will be mounted at `/host`.
* The container runs in the host IPC, Network, and PID namespaces, although
  the pod isn't privileged, so reading some process information may fail,
  and `chroot /host` may fail.
* If you need a privileged pod, create it manually or use the `--profile=sysadmin` flag.

Don't forget to clean up the debugging Pod when you're finished with it:

```shell
kubectl delete pod node-debugger-mynode-pdx84
```

### Capturing and analyzing Node/Pod traffic

When debugging networking issues, capturing and analyzing network traffic from Nodes/Pods can provide valuable insights
into connectivity problems, DNS resolution failures, or unexpected network behavior.

You can use `kubectl debug` with the `--profile=sysadmin` flag to run network capture tools on a node.
First, create a debugging session on the node where your Pod is running:

```shell
kubectl debug --profile=sysadmin node/${NODE_NAME} -it --image=ubuntu:latest
```

Once inside the debug container, install tcpdump and capture traffic on the node's network interfaces:

```shell
apt-get update && apt-get install -y tcpdump
tcpdump -i any -n
```

Don't forget to clean up the debugging Pod when you're finished with it:

```shell
kubectl delete pod node-debugger-mynode-pdx84
```

You can also capture traffic from a specific Pod:

```shell
kubectl debug --profile=sysadmin pod/${POD_NAME} -n ${NAMESPACE} -it --image=ubuntu:latest
```

And then perform the same `tcpdump` command inside the debug container to capture traffic from the Pod's network namespace.
