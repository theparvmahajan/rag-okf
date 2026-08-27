---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-create-objects
kind: section
title: How to create objects
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: How to create objects
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#trade-offs
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-update-objects
word_count: 196
---

The `kubectl` tool supports verb-driven commands for creating some of the most common
object types. The commands are named to be recognizable to users unfamiliar with
the Kubernetes object types.

- `run`: Create a new Pod to run a Container.
- `expose`: Create a new Service object to load balance traffic across Pods.
- `autoscale`: Create a new Autoscaler object to automatically horizontally scale a controller, such as a Deployment.

The `kubectl` tool also supports creation commands driven by object type.
These commands support more object types and are more explicit about
their intent, but require users to know the type of objects they intend
to create.

- `create <objecttype> [<subtype>] <instancename>`

Some objects types have subtypes that you can specify in the `create` command.
For example, the Service object has several subtypes including ClusterIP,
LoadBalancer, and NodePort. Here's an example that creates a Service with
subtype NodePort:

```shell
kubectl create service nodeport <myservicename>
```

In the preceding example, the `create service nodeport` command is called
a subcommand of the `create service` command.

You can use the `-h` flag to find the arguments and flags supported by
a subcommand:

```shell
kubectl create service nodeport -h
```
