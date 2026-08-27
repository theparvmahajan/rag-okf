---
id: okf-structure/concepts/cluster-administration/networking.md#introduction
kind: section
title: Cluster Networking
source: concepts/cluster-administration/networking.md
url: https://kubernetes.io/docs/concepts/cluster-administration/networking/
heading: null
parent: okf-structure/concepts/cluster-administration/networking
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/networking.md#kubernetes-ip-address-ranges
word_count: 179
---

Networking is a central part of Kubernetes, but it can be challenging to
understand exactly how it is expected to work.  There are 4 distinct networking
problems to address:

1. Highly-coupled container-to-container communications: this is solved by
   Pods and `localhost` communications.
2. Pod-to-Pod communications: this is the primary focus of this document.
3. Pod-to-Service communications: this is covered by Services.
4. External-to-Service communications: this is also covered by Services.

Kubernetes is all about sharing machines among applications.  Typically,
sharing machines requires ensuring that two applications do not try to use the
same ports.  Coordinating ports across multiple developers is very difficult to
do at scale and exposes users to cluster-level issues outside of their control.

Dynamic port allocation brings a lot of complications to the system - every
application has to take ports as flags, the API servers have to know how to
insert dynamic port numbers into configuration blocks, services have to know
how to find each other, etc.  Rather than deal with this, Kubernetes takes a
different approach.

To learn about the Kubernetes networking model, see here.
