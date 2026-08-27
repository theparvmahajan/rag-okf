---
id: okf-structure/tasks/administer-cluster/running-cloud-controller.md#examples
kind: section
title: Examples
source: tasks/administer-cluster/running-cloud-controller.md
url: https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/
heading: Examples
parent: okf-structure/tasks/administer-cluster/running-cloud-controller
children: []
prev_sibling: okf-structure/tasks/administer-cluster/running-cloud-controller.md#administration
next_sibling: okf-structure/tasks/administer-cluster/running-cloud-controller.md#limitations
word_count: 78
---

If you are using a cloud that is currently supported in Kubernetes core and would
like to adopt cloud controller manager, see the
cloud controller manager in kubernetes core.

For cloud controller managers not in Kubernetes core, you can find the respective
projects in repositories maintained by cloud vendors or by SIGs.

For providers already in Kubernetes core, you can run the in-tree cloud controller
manager as a DaemonSet in your cluster, use the following as a guideline:
