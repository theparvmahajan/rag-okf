---
id: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#caveats
kind: section
title: Caveats
source: tasks/administer-cluster/kubelet-in-userns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/
heading: Caveats
parent: okf-structure/tasks/administer-cluster/kubelet-in-userns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#manually-deploy-a-node-that-runs-the-kubelet-in-a-user-namespace-userns-the-hard-way
next_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#seealso
word_count: 56
---

- Most of "non-local" volume drivers such as `nfs` and `iscsi` do not work.
  Local volumes like `local`, `hostPath`, `emptyDir`, `configMap`, `secret`, and `downwardAPI` are known to work.

- Some CNI plugins may not work. Flannel (VXLAN) is known to work.

For more on this, see the Caveats and Future work page
on the rootlesscontaine.rs website.
