---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#using-set-commands-to-modify-objects-before-creation
kind: section
title: Using `set` commands to modify objects before creation
source: tasks/manage-kubernetes-objects/imperative-command.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-command/
heading: Using `set` commands to modify objects before creation
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-command
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#how-to-view-an-object
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-command.md#using-edit-to-modify-objects-before-creation
word_count: 164
---

There are some object fields that don't have a flag you can use
in a `create` command. In some of those cases, you can use a combination of
`set` and `create` to specify a value for the field before object
creation. This is done by piping the output of the `create` command to the
`set` command, and then back to the `create` command. Here's an example:

```sh
kubectl create service clusterip my-svc --clusterip="None" -o yaml --dry-run=client | kubectl set selector --local -f - 'environment=qa' -o yaml | kubectl create -f -
```

1. The `kubectl create service -o yaml --dry-run=client` command creates the configuration for the Service, but prints it to stdout as YAML instead of sending it to the Kubernetes API server.
1. The `kubectl set selector --local -f - -o yaml` command reads the configuration from stdin, and writes the updated configuration to stdout as YAML.
1. The `kubectl create -f -` command creates the object using the configuration provided via stdin.
