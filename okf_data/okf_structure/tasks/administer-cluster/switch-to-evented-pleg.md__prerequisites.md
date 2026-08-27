---
id: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/switch-to-evented-pleg.md
url: https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/switch-to-evented-pleg
children: []
prev_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#why-switch-to-evented-pleg
word_count: 98
---

* You need to run a version of Kubernetes that provides this feature.
  Kubernetes v1.27 includes beta support for event-based container
  status updates. The feature is beta but is _disabled_ by default
  because it requires support from the container runtime.
* 
  If you are running a different version of Kubernetes, check the documentation for that release.
* The container runtime in use must support container lifecycle events.
  The kubelet automatically switches back to the legacy generic PLEG
  mechanism if the container runtime does not announce support for
  container lifecycle events, even if you have this feature gate enabled.
