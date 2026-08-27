---
id: okf-structure/tutorials/security/seccomp.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Prerequisites
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#objectives
next_sibling: okf-structure/tutorials/security/seccomp.md#download-example-seccomp-profiles-download-profiles
word_count: 155
---

In order to complete all steps in this tutorial, you must install
kind and kubectl.

The commands used in the tutorial assume that you are using
Docker as your container runtime. (The cluster that `kind` creates may
use a different container runtime internally). You could also use
Podman but in that case, you would have to follow specific
instructions in order to complete the tasks
successfully.

This tutorial shows some examples that are still beta (since v1.25) and
others that use only generally available seccomp functionality. You should
make sure that your cluster is
configured correctly
for the version you are using.

The tutorial also uses the `curl` tool for downloading examples to your computer.
You can adapt the steps to use a different tool if you prefer.

It is not possible to apply a seccomp profile to a container running with
`privileged: true` set in the container's `securityContext`. Privileged containers always
run as `Unconfined`.
