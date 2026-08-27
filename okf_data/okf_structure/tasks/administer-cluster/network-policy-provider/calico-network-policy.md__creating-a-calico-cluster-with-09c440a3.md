---
id: okf-structure/tasks/administer-cluster/network-policy-provider/calico-network-policy.md#creating-a-calico-cluster-with-google-kubernetes-engine-gke
kind: section
title: Creating a Calico cluster with Google Kubernetes Engine (GKE)
source: tasks/administer-cluster/network-policy-provider/calico-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/
heading: Creating a Calico cluster with Google Kubernetes Engine (GKE)
parent: okf-structure/tasks/administer-cluster/network-policy-provider/calico-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/calico-network-policy.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/calico-network-policy.md#creating-a-local-calico-cluster-with-kubeadm
word_count: 64
---

**Prerequisite**: gcloud.

1.  To launch a GKE cluster with Calico, include the `--enable-network-policy` flag.

    **Syntax**
    ```shell
    gcloud container clusters create [CLUSTER_NAME] --enable-network-policy
    ```

    **Example**
    ```shell
    gcloud container clusters create my-calico-cluster --enable-network-policy
    ```

1.  To verify the deployment, use the following command.

    ```shell
    kubectl get pods --namespace=kube-system
    ```

    The Calico pods begin with `calico`. Check to make sure each one has a status of `Running`.
