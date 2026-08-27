This page shows a couple of quick ways to create a Calico cluster on Kubernetes.

## Prerequisites

Decide whether you want to deploy a cloud or local cluster.

## Creating a Calico cluster with Google Kubernetes Engine (GKE)

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

## Creating a local Calico cluster with kubeadm

To get a local single-host Calico cluster in fifteen minutes using kubeadm, refer to the 
Calico Quickstart.

## Whatsnext

Once your cluster is running, you can follow the Declare Network Policy to try out Kubernetes NetworkPolicy.