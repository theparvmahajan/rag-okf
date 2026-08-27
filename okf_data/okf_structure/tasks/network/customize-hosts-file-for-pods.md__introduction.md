---
id: okf-structure/tasks/network/customize-hosts-file-for-pods.md#introduction
kind: section
title: Adding entries to Pod /etc/hosts with HostAliases
source: tasks/network/customize-hosts-file-for-pods.md
url: https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/
heading: null
parent: okf-structure/tasks/network/customize-hosts-file-for-pods
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/network/customize-hosts-file-for-pods.md#default-hosts-file-content
word_count: 81
---

Adding entries to a Pod's `/etc/hosts` file provides Pod-level override of hostname resolution when DNS and other options are not applicable. You can add these custom entries with the HostAliases field in PodSpec.

The Kubernetes project recommends modifying DNS configuration using the `hostAliases` field
(part of the `.spec` for a Pod), and not by using an init container or other means to edit `/etc/hosts`
directly.
Change made in other ways may be overwritten by the kubelet during Pod creation or restart.
