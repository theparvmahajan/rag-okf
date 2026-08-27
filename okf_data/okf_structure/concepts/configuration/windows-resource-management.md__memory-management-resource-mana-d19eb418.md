---
id: okf-structure/concepts/configuration/windows-resource-management.md#memory-management-resource-management-memory
kind: section
title: Memory management {#resource-management-memory}
source: concepts/configuration/windows-resource-management.md
url: https://kubernetes.io/docs/concepts/configuration/windows-resource-management/
heading: Memory management {#resource-management-memory}
parent: okf-structure/concepts/configuration/windows-resource-management
children: []
prev_sibling: okf-structure/concepts/configuration/windows-resource-management.md#introduction
next_sibling: okf-structure/concepts/configuration/windows-resource-management.md#cpu-management-resource-management-cpu
word_count: 80
---

Windows does not have an out-of-memory process killer as Linux does. Windows always
treats all user-mode memory allocations as virtual, and pagefiles are mandatory.

Windows nodes do not overcommit memory for processes. The
net effect is that Windows won't reach out of memory conditions the same way Linux
does, and processes page to disk instead of being subject to out of memory (OOM)
termination. If memory is over-provisioned and all physical memory is exhausted,
then paging can slow down performance.
