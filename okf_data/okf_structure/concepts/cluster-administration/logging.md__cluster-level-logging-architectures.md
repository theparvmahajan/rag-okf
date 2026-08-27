---
id: okf-structure/concepts/cluster-administration/logging.md#cluster-level-logging-architectures
kind: section
title: Cluster-level logging architectures
source: concepts/cluster-administration/logging.md
url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
heading: Cluster-level logging architectures
parent: okf-structure/concepts/cluster-administration/logging
children: []
prev_sibling: okf-structure/concepts/cluster-administration/logging.md#system-component-logs
next_sibling: okf-structure/concepts/cluster-administration/logging.md#whatsnext
word_count: 893
---

While Kubernetes does not provide a native solution for cluster-level logging, there are
several common approaches you can consider. Here are some options:

* Use a node-level logging agent that runs on every node.
* Include a dedicated sidecar container for logging in an application pod.
* Push logs directly to a backend from within an application.

### Using a node logging agent

Using a node level logging agent

You can implement cluster-level logging by including a _node-level logging agent_ on each node.
The logging agent is a dedicated tool that exposes logs or pushes logs to a backend.
Commonly, the logging agent is a container that has access to a directory with log files from all of the
application containers on that node.

Because the logging agent must run on every node, it is recommended to run the agent
as a `DaemonSet`.

Node-level logging creates only one agent per node and doesn't require any changes to the
applications running on the node.

Containers write to stdout and stderr, but with no agreed format. A node-level agent collects
these logs and forwards them for aggregation.

### Using a sidecar container with the logging agent {#sidecar-container-with-logging-agent}

You can use a sidecar container in one of the following ways:

* The sidecar container streams application logs to its own `stdout`.
* The sidecar container runs a logging agent, which is configured to pick up logs
  from an application container.

#### Streaming sidecar container

Sidecar container with a streaming container

By having your sidecar containers write to their own `stdout` and `stderr`
streams, you can take advantage of the kubelet and the logging agent that
already run on each node. The sidecar containers read logs from a file, a socket,
or journald. Each sidecar container prints a log to its own `stdout` or `stderr` stream.

This approach allows you to separate several log streams from different
parts of your application, some of which can lack support
for writing to `stdout` or `stderr`. The logic behind redirecting logs
is minimal, so it's not a significant overhead. Additionally, because
`stdout` and `stderr` are handled by the kubelet, you can use built-in tools
like `kubectl logs`.

For example, a pod runs a single container, and the container
writes to two different log files using two different formats. Here's a
manifest for the Pod:

It is not recommended to write log entries with different formats to the same log
stream, even if you managed to redirect both components to the `stdout` stream of
the container. Instead, you can create two sidecar containers. Each sidecar
container could tail a particular log file from a shared volume and then redirect
the logs to its own `stdout` stream.

Here's a manifest for a pod that has two sidecar containers:

Now when you run this pod, you can access each log stream separately by
running the following commands:

```shell
kubectl logs counter count-log-1
```

The output is similar to:

```console
0: Fri Apr  1 11:42:26 UTC 2022
1: Fri Apr  1 11:42:27 UTC 2022
2: Fri Apr  1 11:42:28 UTC 2022
...
```

```shell
kubectl logs counter count-log-2
```

The output is similar to:

```console
Fri Apr  1 11:42:29 UTC 2022 INFO 0
Fri Apr  1 11:42:30 UTC 2022 INFO 0
Fri Apr  1 11:42:31 UTC 2022 INFO 0
...
```

If you installed a node-level agent in your cluster, that agent picks up those log
streams automatically without any further configuration. If you like, you can configure
the agent to parse log lines depending on the source container.

Even for Pods that only have low CPU and memory usage (order of a couple of millicores
for cpu and order of several megabytes for memory), writing logs to a file and
then streaming them to `stdout` can double how much storage you need on the node.
If you have an application that writes to a single file, it's recommended to set
`/dev/stdout` as the destination rather than implement the streaming sidecar
container approach.

Sidecar containers can also be used to rotate log files that cannot be rotated by
the application itself. An example of this approach is a small container running
`logrotate` periodically.
However, it's more straightforward to use `stdout` and `stderr` directly, and
leave rotation and retention policies to the kubelet.

#### Sidecar container with a logging agent

Sidecar container with a logging agent

If the node-level logging agent is not flexible enough for your situation, you
can create a sidecar container with a separate logging agent that you have
configured specifically to run with your application.

Using a logging agent in a sidecar container can lead
to significant resource consumption. Moreover, you won't be able to access
those logs using `kubectl logs` because they are not controlled
by the kubelet.

Here are two example manifests that you can use to implement a sidecar container with a logging agent.
The first manifest contains a `ConfigMap`
to configure fluentd.

In the sample configurations, you can replace fluentd with any logging agent, reading
from any source inside an application container.

The second manifest describes a pod that has a sidecar container running fluentd.
The pod mounts a volume where fluentd can pick up its configuration data.

### Exposing logs directly from the application

Exposing logs directly from the application

Cluster-logging that exposes or pushes logs directly from every application is outside the scope
of Kubernetes.
