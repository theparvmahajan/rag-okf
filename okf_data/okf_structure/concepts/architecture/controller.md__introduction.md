---
id: okf-structure/concepts/architecture/controller.md#introduction
kind: section
title: Controllers
source: concepts/architecture/controller.md
url: https://kubernetes.io/docs/concepts/architecture/controller/
heading: null
parent: okf-structure/concepts/architecture/controller
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/controller.md#controller-pattern
word_count: 71
---

In robotics and automation, a _control loop_ is
a non-terminating loop that regulates the state of a system.

Here is one example of a control loop: a thermostat in a room.

When you set the temperature, that's telling the thermostat
about your *desired state*. The actual room temperature is the
*current state*. The thermostat acts to bring the current state
closer to the desired state, by turning equipment on or off.
