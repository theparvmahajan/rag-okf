---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configure-multiple-feature-gates
kind: section
title: Configure multiple feature gates
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: Configure multiple feature gates
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configuration
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#verify-feature-gate-configuration
word_count: 65
---

Use comma-separated lists for command-line flags:

```shell
--feature-gates=FeatureA=true,FeatureB=false,FeatureC=true
```

For components that support configuration files (kubelet, kube-proxy):

```yaml
featureGates:
  FeatureA: true
  FeatureB: false
  FeatureC: true
```

In kubeadm clusters, control plane components (kube-apiserver, kube-controller-manager, 
and kube-scheduler) are typically configured via command-line flags in their static pod 
manifests located at `/etc/kubernetes/manifests/`. While these components support 
configuration files via the `--config` flag, kubeadm primarily uses command-line flags.
