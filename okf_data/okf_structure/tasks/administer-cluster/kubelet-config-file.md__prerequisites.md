---
id: okf-structure/tasks/administer-cluster/kubelet-config-file.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubelet-config-file.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubelet-config-file
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#create-the-config-file
word_count: 84
---

Some steps in this page use the `jq` tool. If you don't have `jq`, you can
install it via your operating system's software sources, or fetch it from
https://jqlang.github.io/jq/.

Some steps also involve installing `curl`, which can be installed via your
operating system's software sources.

A subset of the kubelet's configuration parameters may be
set via an on-disk config file, as a substitute for command-line flags.

Providing parameters via a config file is the recommended approach because
it simplifies node deployment and configuration management.
