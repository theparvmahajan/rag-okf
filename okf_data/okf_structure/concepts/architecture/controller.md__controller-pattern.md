---
id: okf-structure/concepts/architecture/controller.md#controller-pattern
kind: section
title: Controller pattern
source: concepts/architecture/controller.md
url: https://kubernetes.io/docs/concepts/architecture/controller/
heading: Controller pattern
parent: okf-structure/concepts/architecture/controller
children: []
prev_sibling: okf-structure/concepts/architecture/controller.md#introduction
next_sibling: okf-structure/concepts/architecture/controller.md#desired-versus-current-state-desired-vs-current
word_count: 530
---

A controller tracks at least one Kubernetes resource type.
These objects
have a spec field that represents the desired state. The
controller(s) for that resource are responsible for making the current
state come closer to that desired state.

The controller might carry the action out itself; more commonly, in Kubernetes,
a controller will send messages to the
API server that have
useful side effects. You'll see examples of this below.

Some built-in controllers, such as the namespace controller, act on objects
that do not have a spec. For simplicity, this page omits explaining that
detail.

### Control via API server

The job controller is an example of a
Kubernetes built-in controller. Built-in controllers manage state by
interacting with the cluster API server.

Job is a Kubernetes resource that runs a
pod, or perhaps several Pods, to carry out
a task and then stop.

(Once scheduled, Pod objects become part of the
desired state for a kubelet).

When the Job controller sees a new task it makes sure that, somewhere
in your cluster, the kubelets on a set of Nodes are running the right
number of Pods to get the work done.
The Job controller does not run any Pods or containers
itself. Instead, the Job controller tells the API server to create or remove
Pods.
Other components in the
control plane
act on the new information (there are new Pods to schedule and run),
and eventually the work is done.

After you create a new Job, the desired state is for that Job to be completed.
The Job controller makes the current state for that Job be nearer to your
desired state: creating Pods that do the work you wanted for that Job, so that
the Job is closer to completion.

Controllers also update the objects that configure them.
For example: once the work is done for a Job, the Job controller
updates that Job object to mark it `Finished`.

(This is a bit like how some thermostats turn a light off to
indicate that your room is now at the temperature you set).

### Direct control

In contrast with Job, some controllers need to make changes to
things outside of your cluster.

For example, if you use a control loop to make sure there
are enough Nodes
in your cluster, then that controller needs something outside the
current cluster to set up new Nodes when needed.

Controllers that interact with external state find their desired state from
the API server, then communicate directly with an external system to bring
the current state closer in line.

(There actually is a controller
that horizontally scales the nodes in your cluster.)

The important point here is that the controller makes some changes to bring about
your desired state, and then reports the current state back to your cluster's API server.
Other control loops can observe that reported data and take their own actions.

In the thermostat example, if the room is very cold then a different controller
might also turn on a frost protection heater. With Kubernetes clusters, the control
plane indirectly works with IP address management tools, storage services,
cloud provider APIs, and other services by
extending Kubernetes to implement that.
