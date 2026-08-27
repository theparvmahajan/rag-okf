---
id: okf-structure/tutorials/kubernetes-basics/update/update-intro.md#updating-an-application
kind: section
title: Updating an application
source: tutorials/kubernetes-basics/update/update-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/
heading: Updating an application
parent: okf-structure/tutorials/kubernetes-basics/update/update-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/update/update-intro.md#prerequisites
next_sibling: okf-structure/tutorials/kubernetes-basics/update/update-intro.md#rolling-updates-overview
word_count: 178
---

_Rolling updates allow Deployments' update to take place with zero downtime by
incrementally updating Pods instances with new ones._

Users expect applications to be available all the time, and developers are expected
to deploy new versions of them several times a day. In Kubernetes this is done with
rolling updates. A **rolling update** allows a Deployment update to take place with
zero downtime. It does this by incrementally replacing the current Pods with new ones.
The new Pods are scheduled on Nodes with available resources, and Kubernetes waits
for those new Pods to start before removing the old Pods.

In the previous module we scaled our application to run multiple instances. This
is a requirement for performing updates without affecting application availability.
By default, the maximum number of Pods that can be unavailable during the update
and the maximum number of new Pods that can be created, is one. Both options can
be configured to either numbers or percentages (of Pods). In Kubernetes, updates are
versioned and any Deployment update can be reverted to a previous (stable) version.
