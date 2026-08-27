---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#verify-feature-gate-configuration
kind: section
title: Verify feature gate configuration
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: Verify feature gate configuration
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configure-multiple-feature-gates
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#understanding-component-specific-requirements
word_count: 262
---

After configuring, verify the feature gates are active. The following methods apply 
to kubeadm clusters where control plane components run as static pods.

### Check control plane component manifests

View the feature gates configured in the static pod manifest:
```shell
kubectl -n kube-system get pod kube-apiserver-<node-name> -o yaml | grep feature-gates
```

### Check kubelet configuration

Use the kubelet's configz endpoint:
```shell
kubectl proxy --port=8001 &
curl -sSL "http://localhost:8001/api/v1/nodes/<node-name>/proxy/configz" | grep featureGates -A 5
```

Or check the configuration file directly on the node:
```shell
cat /var/lib/kubelet/config.yaml | grep -A 10 featureGates
```

### Check via metrics endpoint

Feature gate status is exposed in Prometheus-style metrics by Kubernetes components 
(available in Kubernetes 1.26+). Query the metrics endpoint to verify which feature 
gates are enabled:
```shell
kubectl get --raw /metrics | grep kubernetes_feature_enabled
```

To check a specific feature gate:
```shell
kubectl get --raw /metrics | grep kubernetes_feature_enabled | grep FeatureName
```

The metric shows `1` for enabled gates and `0` for disabled gates.

In kubeadm clusters, verify all relevant locations where feature gates might be 
configured, as the configuration is distributed across multiple files and locations.

### Check via /flagz endpoint

If you have access to a component's debugging endpoints, and the `ComponentFlagz`
feature gate is enabled for that component, you can inspect the command-line flags
that were used to start the component by visiting the `/flagz` endpoint. Feature
gates configured using command-line flags appear in this output.

The `/flagz` endpoint is part of Kubernetes *z-pages*, which provide human-readable
runtime debugging information for core components.

For more information, see the
z-pages documentation.
