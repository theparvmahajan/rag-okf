---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#overwrite-the-configuration
kind: section
title: Overwrite the configuration
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: Overwrite the configuration
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#enabling-node-problem-detector
next_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#problem-daemons
word_count: 117
---

The default configuration
is embedded when building the Docker image of Node Problem Detector.

However, you can use a `ConfigMap`
to overwrite the configuration:

1. Change the configuration files in `config/`
1. Create the `ConfigMap` `node-problem-detector-config`:

   ```shell
   kubectl create configmap node-problem-detector-config --from-file=config/
   ```

1. Change the `node-problem-detector.yaml` to use the `ConfigMap`:

   

1. Recreate the Node Problem Detector with the new configuration file:

   ```shell
   # If you have a node-problem-detector running, delete before recreating
   kubectl delete -f https://k8s.io/examples/debug/node-problem-detector.yaml
   kubectl apply -f https://k8s.io/examples/debug/node-problem-detector-configmap.yaml
   ```

This approach only applies to a Node Problem Detector started with `kubectl`.

Overwriting a configuration is not supported if a Node Problem Detector runs as a cluster Addon.
The Addon manager does not support `ConfigMap`.
