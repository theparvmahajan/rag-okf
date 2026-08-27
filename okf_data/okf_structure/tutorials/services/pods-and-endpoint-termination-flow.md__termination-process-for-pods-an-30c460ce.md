---
id: okf-structure/tutorials/services/pods-and-endpoint-termination-flow.md#termination-process-for-pods-and-their-endpoints
kind: section
title: Termination process for Pods and their endpoints
source: tutorials/services/pods-and-endpoint-termination-flow.md
url: https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/
heading: Termination process for Pods and their endpoints
parent: okf-structure/tutorials/services/pods-and-endpoint-termination-flow
children: []
prev_sibling: okf-structure/tutorials/services/pods-and-endpoint-termination-flow.md#introduction
next_sibling: okf-structure/tutorials/services/pods-and-endpoint-termination-flow.md#example-flow-with-endpoint-termination
word_count: 64
---

There are often cases when you need to terminate a Pod - be it to upgrade or scale down.
In order to improve application availability, it may be important to implement
a proper active connections draining.

This tutorial explains the flow of Pod termination in connection with the
corresponding endpoint state and removal by using
a simple nginx web server to demonstrate the concept.
