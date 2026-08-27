---
id: okf-structure/concepts/architecture/controller.md#design
kind: section
title: Design
source: concepts/architecture/controller.md
url: https://kubernetes.io/docs/concepts/architecture/controller/
heading: Design
parent: okf-structure/concepts/architecture/controller
children: []
prev_sibling: okf-structure/concepts/architecture/controller.md#desired-versus-current-state-desired-vs-current
next_sibling: okf-structure/concepts/architecture/controller.md#ways-of-running-controllers-running-controllers
word_count: 195
---

As a tenet of its design, Kubernetes uses lots of controllers that each manage
a particular aspect of cluster state. Most commonly, a particular control loop
(controller) uses one kind of resource as its desired state, and has a different
kind of resource that it manages to make that desired state happen. For example,
a controller for Jobs tracks Job objects (to discover new work) and Pod objects
(to run the Jobs, and then to see when the work is finished). In this case
something else creates the Jobs, whereas the Job controller creates Pods.

It's useful to have simple controllers rather than one, monolithic set of control
loops that are interlinked. Controllers can fail, so Kubernetes is designed to
allow for that.

There can be several controllers that create or update the same kind of object.
Behind the scenes, Kubernetes controllers make sure that they only pay attention
to the resources linked to their controlling resource.

For example, you can have Deployments and Jobs; these both create Pods.
The Job controller does not delete the Pods that your Deployment created,
because there is information (labels)
the controllers can use to tell those Pods apart.
