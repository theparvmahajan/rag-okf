---
id: okf-structure/concepts/cluster-administration/compatibility-version.md#emulated-version
kind: section
title: Emulated Version
source: concepts/cluster-administration/compatibility-version.md
url: https://kubernetes.io/docs/concepts/cluster-administration/compatibility-version/
heading: Emulated Version
parent: okf-structure/concepts/cluster-administration/compatibility-version
children: []
prev_sibling: okf-structure/concepts/cluster-administration/compatibility-version.md#introduction
next_sibling: null
word_count: 124
---

The emulation option is set by the `--emulated-version` flag of control plane components. It allows the component to emulate the behavior (APIs, features, ...) of an earlier version of Kubernetes.

When used, the capabilities available will match the emulated version: 
* Any capabilities present in the binary version that were introduced after the emulation version will be unavailable. 
* Any capabilities removed after the emulation version will be available. 

This enables a binary from a particular Kubernetes release to emulate the behavior of a previous version with sufficient fidelity that interoperability with other system components can be defined in terms of the emulated version.

The `--emulated-version` must be <= `binaryVersion`. See the help message of the `--emulated-version` flag for supported range of emulated versions.
