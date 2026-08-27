---
id: okf-structure/tasks/manage-daemon/create-daemon-set.md#define-the-daemonset
kind: section
title: Define the DaemonSet
source: tasks/manage-daemon/create-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/create-daemon-set/
heading: Define the DaemonSet
parent: okf-structure/tasks/manage-daemon/create-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/create-daemon-set.md#prerequisites
next_sibling: okf-structure/tasks/manage-daemon/create-daemon-set.md#cleanup
word_count: 165
---

In this task, a basic DaemonSet is created which ensures that the copy of a Pod is scheduled on every node.
The Pod will use an init container to read and log the contents of `/etc/machine-id` from the host,
while the main container will be a `pause` container, which keeps the Pod running.

1. Create a DaemonSet based on the (YAML) manifest:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/basic-daemonset.yaml
   ```

1. Once applied, you can verify that the DaemonSet is running a Pod on every node in the cluster:

   ```shell
   kubectl get pods -o wide
   ```

   The output will list one Pod per node, similar to:

   ```
   NAME                                READY   STATUS    RESTARTS   AGE    IP       NODE
   example-daemonset-xxxxx             1/1     Running   0          5m     x.x.x.x  node-1
   example-daemonset-yyyyy             1/1     Running   0          5m     x.x.x.x  node-2
   ```

1. You can inspect the contents of the logged `/etc/machine-id` file by checking
   the log directory mounted from the host:

   ```shell
   kubectl exec <pod-name> -- cat /var/log/machine-id.log
   ```

   Where `<pod-name>` is the name of one of your Pods.
