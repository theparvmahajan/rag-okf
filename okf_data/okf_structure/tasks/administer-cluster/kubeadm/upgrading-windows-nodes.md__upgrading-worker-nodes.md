---
id: okf-structure/tasks/administer-cluster/kubeadm/upgrading-windows-nodes.md#upgrading-worker-nodes
kind: section
title: Upgrading worker nodes
source: tasks/administer-cluster/kubeadm/upgrading-windows-nodes.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/
heading: Upgrading worker nodes
parent: okf-structure/tasks/administer-cluster/kubeadm/upgrading-windows-nodes
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/upgrading-windows-nodes.md#prerequisites
next_sibling: null
word_count: 226
---

### Upgrade kubeadm

1.  From the Windows node, upgrade kubeadm:

    ```powershell
    # replace  with your desired version
    curl.exe -Lo <path-to-kubeadm.exe>  "https://dl.k8s.io/v/bin/windows/amd64/kubeadm.exe"
    ```

### Drain the node

1.  From a machine with access to the Kubernetes API,
    prepare the node for maintenance by marking it unschedulable and evicting the workloads:

    ```shell
    # replace <node-to-drain> with the name of your node you are draining
    kubectl drain <node-to-drain> --ignore-daemonsets
    ```

    You should see output similar to this:

    ```
    node/ip-172-31-85-18 cordoned
    node/ip-172-31-85-18 drained
    ```

### Upgrade the kubelet configuration

1.  From the Windows node, call the following command to sync new kubelet configuration:

    ```powershell
    kubeadm upgrade node
    ```

### Upgrade kubelet and kube-proxy

1.  From the Windows node, upgrade and restart the kubelet:

    ```powershell
    stop-service kubelet
    curl.exe -Lo <path-to-kubelet.exe> "https://dl.k8s.io/v/bin/windows/amd64/kubelet.exe"
    restart-service kubelet
    ```

2. From the Windows node, upgrade and restart the kube-proxy.

    ```powershell
    stop-service kube-proxy
    curl.exe -Lo <path-to-kube-proxy.exe> "https://dl.k8s.io/v/bin/windows/amd64/kube-proxy.exe"
    restart-service kube-proxy
    ```

If you are running kube-proxy in a HostProcess container within a Pod, and not as a Windows Service,
you can upgrade kube-proxy by applying a newer version of your kube-proxy manifests.

### Uncordon the node

1.  From a machine with access to the Kubernetes API,
bring the node back online by marking it schedulable:

    ```shell
    # replace <node-to-drain> with the name of your node
    kubectl uncordon <node-to-drain>
    ```
 ## Whatsnext

* See how to Upgrade Linux nodes.
