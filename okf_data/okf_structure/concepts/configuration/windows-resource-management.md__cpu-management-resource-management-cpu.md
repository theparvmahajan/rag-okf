---
id: okf-structure/concepts/configuration/windows-resource-management.md#cpu-management-resource-management-cpu
kind: section
title: CPU management {#resource-management-cpu}
source: concepts/configuration/windows-resource-management.md
url: https://kubernetes.io/docs/concepts/configuration/windows-resource-management/
heading: CPU management {#resource-management-cpu}
parent: okf-structure/concepts/configuration/windows-resource-management
children: []
prev_sibling: okf-structure/concepts/configuration/windows-resource-management.md#memory-management-resource-management-memory
next_sibling: okf-structure/concepts/configuration/windows-resource-management.md#resource-reservation-resource-reservation
word_count: 96
---

Windows can limit the amount of CPU time allocated for different processes but cannot
guarantee a minimum amount of CPU time.

On Windows, the kubelet supports a command-line flag to set the
scheduling priority of the
kubelet process: `--windows-priorityclass`. This flag allows the kubelet process to get
more CPU time slices when compared to other processes running on the Windows host.
More information on the allowable values and their meaning is available at
Windows Priority Classes.
To ensure that running Pods do not starve the kubelet of CPU cycles, set this flag to `ABOVE_NORMAL_PRIORITY_CLASS` or above.
