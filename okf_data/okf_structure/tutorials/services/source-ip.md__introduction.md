---
id: okf-structure/tutorials/services/source-ip.md#introduction
kind: section
title: Using Source IP
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: null
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/services/source-ip.md#prerequisites
word_count: 48
---

Applications running in a Kubernetes cluster find and communicate with each
other, and the outside world, through the Service abstraction. This document
explains what happens to the source IP of packets sent to different types
of Services, and how you can toggle this behavior according to your needs.
