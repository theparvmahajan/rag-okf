---
id: okf-structure/concepts/workloads/pods/_index.md#working-with-pods
kind: section
title: Working with Pods
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Working with Pods
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#using-pods
next_sibling: okf-structure/concepts/workloads/pods/_index.md#pod-update-and-replacement
word_count: 819
---

You'll rarely create individual Pods directly in Kubernetes—even singleton Pods. This
is because Pods are designed as relatively ephemeral, disposable entities. When
a Pod gets created (directly by you, or indirectly by a
controller), the new Pod is
scheduled to run on a node in your cluster.
The Pod remains on that node until the Pod finishes execution, the Pod object is deleted,
the Pod is *evicted* for lack of resources, or the node fails.

Restarting a container in a Pod should not be confused with restarting a Pod. A Pod
is not a process, but an environment for running container(s). A Pod persists until
it is deleted.

The name of a Pod must be a valid
DNS subdomain
value, but this can produce unexpected results for the Pod hostname.  For best compatibility,
the name should follow the more restrictive rules for a
DNS label.

### Pod OS

You should set the `.spec.os.name` field to either `windows` or `linux` to indicate the
operating system that the containers in that Pod require. These two are the only operating
systems supported for now by Kubernetes. In the future, this list may be expanded.

The kubelet refuses to run a Pod if the value of `.spec.os.name` does not match the
operating system of the node. However, in Kubernetes
v, the value of `.spec.os.name` does not affect
how the kube-scheduler
picks a node for the Pod to run on. In any cluster where there is more than one operating system for
running nodes, you should set the
kubernetes.io/os
label correctly on each node, and define pods with a `nodeSelector` based on the operating system
label. The kube-scheduler assigns your pod to a node based on other criteria and may or may not
succeed in picking a suitable node placement where the node OS is right for the containers in that Pod.
The Pod security standards also use this
field to avoid enforcing policies that aren't relevant to the operating system.

### Pods and controllers

You can use workload resources to create and manage multiple Pods for you. A controller
for the resource handles replication and rollout and automatic healing in case of
Pod failure. For example, if a Node fails, a controller notices that Pods on that
Node have stopped working and creates a replacement Pod. The scheduler places the
replacement Pod onto a healthy Node.

Here are some examples of workload resources that manage one or more Pods:

* Deployment
* StatefulSet
* DaemonSet

### Specifying a scheduling group

By default, Kubernetes schedules every Pod individually. However, some tightly-coupled applications
need a group of Pods to be scheduled simultaneously to function correctly.

You can link a Pod to a PodGroup using the
scheduling group field
(`spec.schedulingGroup`). This tells the `kube-scheduler` that the `Pod` belongs to a specific
group, enabling it to apply group-level coordinated placement decisions for the entire group at once.

### Pod templates

Controllers for workload resources create Pods
from a _pod template_ and manage those Pods on your behalf.

PodTemplates are specifications for creating Pods, and are included in workload resources such as
Deployments,
Jobs, and
DaemonSets.

Each controller for a workload resource uses the `PodTemplate` inside the workload
object to make actual Pods. The `PodTemplate` is part of the desired state of whatever
workload resource you used to run your app.

When you create a Pod, you can include
environment variables
in the Pod template for the containers that run in the Pod.

The sample below is a manifest for a simple Job with a `template` that starts one
container. The container in that Pod prints a message then pauses.

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello
spec:
  template:
    # This is the pod template
    spec:
      containers:
      - name: hello
        image: busybox:1.28
        command: ['sh', '-c', 'echo "Hello, Kubernetes!" && sleep 3600']
      restartPolicy: OnFailure
    # The pod template ends here
```

Modifying the pod template or switching to a new pod template has no direct effect
on the Pods that already exist. If you change the pod template for a workload
resource, that resource needs to create replacement Pods that use the updated template.

For example, the StatefulSet controller ensures that the running Pods match the current
pod template for each StatefulSet object. If you edit the StatefulSet to change its pod
template, the StatefulSet starts to create new Pods based on the updated template.
Eventually, all of the old Pods are replaced with new Pods, and the update is complete.

Each workload resource implements its own rules for handling changes to the Pod template.
If you want to read more about StatefulSet specifically, read
Update strategy in the StatefulSet Basics tutorial.

On Nodes, the kubelet does not
directly observe or manage any of the details around pod templates and updates; those
details are abstracted away. That abstraction and separation of concerns simplifies
system semantics, and makes it feasible to extend the cluster's behavior without
changing existing code.
