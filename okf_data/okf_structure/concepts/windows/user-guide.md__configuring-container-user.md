---
id: okf-structure/concepts/windows/user-guide.md#configuring-container-user
kind: section
title: Configuring container user
source: concepts/windows/user-guide.md
url: https://kubernetes.io/docs/concepts/windows/user-guide/
heading: Configuring container user
parent: okf-structure/concepts/windows/user-guide
children: []
prev_sibling: okf-structure/concepts/windows/user-guide.md#observability
next_sibling: okf-structure/concepts/windows/user-guide.md#taints-and-tolerations
word_count: 117
---

### Using configurable Container usernames

Windows containers can be configured to run their entrypoints and processes
with different usernames than the image defaults.
Learn more about it here.

### Managing Workload Identity with Group Managed Service Accounts

Windows container workloads can be configured to use Group Managed Service Accounts (GMSA).
Group Managed Service Accounts are a specific type of Active Directory account that provide automatic password management,
simplified service principal name (SPN) management, and the ability to delegate the management to other administrators across multiple servers.
Containers configured with a GMSA can access external Active Directory Domain resources while carrying the identity configured with the GMSA.
Learn more about configuring and using GMSA for Windows containers here.
