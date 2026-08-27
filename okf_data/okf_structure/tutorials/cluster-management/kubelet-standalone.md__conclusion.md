---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#conclusion
kind: section
title: Conclusion
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Conclusion
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#clean-up
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#whatsnext
word_count: 65
---

This page covered the basic aspects of deploying a kubelet in standalone mode.
You are now ready to deploy Pods and test additional functionality.

Notice that in standalone mode the kubelet does *not* support fetching Pod
configurations from the control plane (because there is no control plane connection).

You also cannot use a ConfigMap or a
Secret to configure the containers
in a static Pod.
