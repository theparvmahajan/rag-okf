---
id: okf-structure/setup/best-practices/multiple-zones.md#background
kind: section
title: Background
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Background
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#introduction
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#control-plane-behavior
word_count: 81
---

Kubernetes is designed so that a single Kubernetes cluster can run
across multiple failure zones, typically where these zones fit within
a logical grouping called a _region_. Major cloud providers define a region
as a set of failure zones (also called _availability zones_) that provide
a consistent set of features: within a region, each zone offers the same
APIs and services.

Typical cloud architectures aim to minimize the chance that a failure in
one zone also impairs services in another zone.
