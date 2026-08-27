---
id: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#enabling-node-problem-detector
kind: section
title: Enabling Node Problem Detector
source: tasks/debug/debug-cluster/monitor-node-health.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/monitor-node-health/
heading: Enabling Node Problem Detector
parent: okf-structure/tasks/debug/debug-cluster/monitor-node-health
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#limitations
next_sibling: okf-structure/tasks/debug/debug-cluster/monitor-node-health.md#overwrite-the-configuration
word_count: 158
---

Some cloud providers enable Node Problem Detector as an Addon.
You can also enable Node Problem Detector with `kubectl` or by creating an Addon DaemonSet.

### Using kubectl to enable Node Problem Detector {#using-kubectl}

`kubectl` provides the most flexible management of Node Problem Detector.
You can overwrite the default configuration to fit it into your environment or
to detect customized node problems. For example:

1. Create a Node Problem Detector configuration similar to `node-problem-detector.yaml`:

   

   
   You should verify that the system log directory is right for your operating system distribution.
   

1. Start node problem detector with `kubectl`:

   ```shell
   kubectl apply -f https://k8s.io/examples/debug/node-problem-detector.yaml
   ```

### Using an Addon pod to enable Node Problem Detector {#using-addon-pod}

If you are using a custom cluster bootstrap solution and don't need
to overwrite the default configuration, you can leverage the Addon pod to
further automate the deployment.

Create `node-problem-detector.yaml`, and save the configuration in the Addon pod's
directory `/etc/kubernetes/addons/node-problem-detector` on a control plane node.
