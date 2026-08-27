---
id: okf-structure/concepts/architecture/controller.md#ways-of-running-controllers-running-controllers
kind: section
title: Ways of running controllers {#running-controllers}
source: concepts/architecture/controller.md
url: https://kubernetes.io/docs/concepts/architecture/controller/
heading: Ways of running controllers {#running-controllers}
parent: okf-structure/concepts/architecture/controller
children: []
prev_sibling: okf-structure/concepts/architecture/controller.md#design
next_sibling: okf-structure/concepts/architecture/controller.md#whatsnext
word_count: 121
---

Kubernetes comes with a set of built-in controllers that run inside
the kube controller manager. These
built-in controllers provide important core behaviors.

The Deployment controller and Job controller are examples of controllers that
come as part of Kubernetes itself ("built-in" controllers).
Kubernetes lets you run a resilient control plane, so that if any of the built-in
controllers were to fail, another part of the control plane will take over the work.

You can find controllers that run outside the control plane, to extend Kubernetes.
Or, if you want, you can write a new controller yourself.
You can run your own controller as a set of Pods,
or externally to Kubernetes. What fits best will depend on what that particular
controller does.
