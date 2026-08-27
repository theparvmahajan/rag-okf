---
id: okf-structure/setup/best-practices/node-conformance.md#node-prerequisite
kind: section
title: Node Prerequisite
source: setup/best-practices/node-conformance.md
url: https://kubernetes.io/docs/setup/best-practices/node-conformance/
heading: Node Prerequisite
parent: okf-structure/setup/best-practices/node-conformance
children: []
prev_sibling: okf-structure/setup/best-practices/node-conformance.md#node-conformance-test
next_sibling: okf-structure/setup/best-practices/node-conformance.md#running-node-conformance-test
word_count: 40
---

To run node conformance test, a node must satisfy the same prerequisites as a
standard Kubernetes node. At a minimum, the node should have the following
daemons installed:

* CRI-compatible container runtimes such as Docker, containerd and CRI-O
* kubelet
