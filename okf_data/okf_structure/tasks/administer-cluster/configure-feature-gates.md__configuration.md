---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configuration
kind: section
title: Configuration
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: Configuration
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#identify-which-components-need-the-feature-gate
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configure-multiple-feature-gates
word_count: 174
---

### During cluster initialization

Create a configuration file to enable feature gates across relevant components:

```yaml
apiVersion: kubeadm.k8s.io/v1beta4
kind: ClusterConfiguration
apiServer:
  extraArgs:
    feature-gates: "FeatureName=true"
controllerManager:
  extraArgs:
    feature-gates: "FeatureName=true"
scheduler:
  extraArgs:
    feature-gates: "FeatureName=true"
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  FeatureName: true
```

Initialize the cluster:

```shell
kubeadm init --config kubeadm-config.yaml
```

### On an existing cluster

For kubeadm clusters, feature gate configuration can be set in several locations 
including manifest files, configuration files, and kubeadm configuration.

Edit control plane component manifests in `/etc/kubernetes/manifests/`:

1. For kube-apiserver, kube-controller-manager, or kube-scheduler, add the flag to the command:

   ```yaml
   spec:
     containers:
     - command:
       - kube-apiserver
       - --feature-gates=FeatureName=true
       # ... other flags
   ```

   Save the file. The pod restarts automatically.

2. For kubelet, edit `/var/lib/kubelet/config.yaml`:

   ```yaml
   apiVersion: kubelet.config.k8s.io/v1beta1
   kind: KubeletConfiguration
   featureGates:
     FeatureName: true
   ```

   Restart kubelet:

   ```shell
   sudo systemctl restart kubelet
   ```

3. For kube-proxy, edit the ConfigMap:

   ```shell
   kubectl -n kube-system edit configmap kube-proxy
   ```

   Add feature gates to the configuration:

   ```yaml
   featureGates:
     FeatureName: true
   ```

   Restart the DaemonSet:

   ```shell
   kubectl -n kube-system rollout restart daemonset kube-proxy
   ```
