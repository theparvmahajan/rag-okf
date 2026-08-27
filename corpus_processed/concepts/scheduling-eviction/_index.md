In Kubernetes, scheduling refers to making sure that Pods
are matched to Nodes so that the
kubelet can run them. Preemption
is the process of terminating Pods with lower Priority
so that Pods with higher Priority can schedule on Nodes. Eviction is the process
of terminating one or more Pods on Nodes.

## Scheduling

* Kubernetes Scheduler
* Assigning Pods to Nodes
* Pod Overhead
* Pod Topology Spread Constraints
* Taints and Tolerations
* Scheduling Framework
* Dynamic Resource Allocation
* Scheduler Performance Tuning
* Resource Bin Packing for Extended Resources
* Pod Scheduling Readiness
* PodGroup Scheduling
* Gang Scheduling
* Topology-aware Scheduling
* Workload-Aware preemption
* Descheduler
* Node Declared Features

## Pod Disruption

* Pod Priority and Preemption
* Node-pressure Eviction
* API-initiated Eviction