---
id: okf-structure/concepts/containers/_index.md#container-images
kind: section
title: Container images
source: concepts/containers/_index.md
url: https://kubernetes.io/docs/concepts/containers/
heading: Container images
parent: okf-structure/concepts/containers/_index
children: []
prev_sibling: okf-structure/concepts/containers/_index.md#introduction
next_sibling: okf-structure/concepts/containers/_index.md#container-runtimes
word_count: 88
---

A container image is a ready-to-run
software package containing everything needed to run an application:
the code and any runtime it requires, application and system libraries,
and default values for any essential settings.

Containers are intended to be stateless and
immutable:
you should not change
the code of a container that is already running. If you have a containerized
application and want to make changes, the correct process is to build a new
image that includes the change, then recreate the container to start from the
updated image.
