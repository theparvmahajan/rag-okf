---
id: okf-structure/concepts/windows/intro.md#windows-os-version-compatibility-windows-os-version-support
kind: section
title: Windows OS version compatibility {#windows-os-version-support}
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Windows OS version compatibility {#windows-os-version-support}
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#container-runtimes-container-runtime
next_sibling: okf-structure/concepts/windows/intro.md#hardware-recommendations-and-considerations-windows-hardware-recommendations
word_count: 52
---

On Windows nodes, strict compatibility rules apply where the host OS version must
match the container base image OS version.

For Kubernetes v, operating system compatibility for Windows nodes (and Pods)
is as follows:

Windows Server LTSC release
: Windows Server 2022
: Windows Server 2025

The Kubernetes version-skew policy also applies.
