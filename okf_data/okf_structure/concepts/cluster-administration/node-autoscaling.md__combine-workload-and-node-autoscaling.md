---
id: okf-structure/concepts/cluster-administration/node-autoscaling.md#combine-workload-and-node-autoscaling
kind: section
title: Combine workload and Node autoscaling
source: concepts/cluster-administration/node-autoscaling.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
heading: Combine workload and Node autoscaling
parent: okf-structure/concepts/cluster-administration/node-autoscaling
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#autoscalers-autoscalers
next_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#related-components
word_count: 341
---

### Horizontal workload autoscaling {#horizontal-workload-autoscaling}

Node autoscaling usually works in response to Pods—it provisions new Nodes to accommodate
unschedulable Pods, and then consolidates the Nodes once they're no longer needed.

Horizontal workload autoscaling
automatically scales the number of workload replicas to maintain a desired average resource
utilization across the replicas. In other words, it automatically creates new Pods in response to
application load, and then removes the Pods once the load decreases.

You can use Node autoscaling together with horizontal workload autoscaling to autoscale the Nodes in
your cluster based on the average real resource utilization of your Pods.

If the application load increases, the average utilization of its Pods should also increase,
prompting workload autoscaling to create new Pods. Node autoscaling should then provision new Nodes
to accommodate the new Pods.

Once the application load decreases, workload autoscaling should remove unnecessary Pods. Node
autoscaling should, in turn, consolidate the Nodes that are no longer needed.

If configured correctly, this pattern ensures that your application always has the Node capacity to
handle load spikes if needed, but you don't have to pay for the capacity when it's not needed.

### Vertical workload autoscaling {#vertical-workload-autoscaling}

When using Node autoscaling, it's important to set Pod resource requests correctly. If the requests
of a given Pod are too low, provisioning a new Node for it might not help the Pod actually run.
If the requests of a given Pod are too high, it might incorrectly prevent consolidating its Node.

Vertical workload autoscaling
automatically adjusts the resource requests of your Pods based on their historical resource usage.

You can use Node autoscaling together with vertical workload autoscaling in order to adjust the
resource requests of your Pods while preserving Node autoscaling capabilities in your cluster.

When using Node autoscaling, it's not recommended to set up vertical workload autoscaling for
DaemonSet Pods. Autoscalers have to predict what DaemonSet Pods on a new Node will look like in
order to predict available Node resources. Vertical workload autoscaling might make these
predictions unreliable, leading to incorrect scaling decisions.
