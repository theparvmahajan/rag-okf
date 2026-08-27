---
id: okf-structure/tutorials/cluster-management/install-use-dra.md#install-an-example-dra-driver-install-example-driver
kind: section
title: Install an example DRA driver {#install-example-driver}
source: tutorials/cluster-management/install-use-dra.md
url: https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/
heading: Install an example DRA driver {#install-example-driver}
parent: okf-structure/tutorials/cluster-management/install-use-dra
children: []
prev_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#explore-the-initial-cluster-state-explore-initial-state
next_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#claim-resources-and-deploy-a-pod-claim-resources-pod
word_count: 607
---

DRA drivers are third-party applications that run on each node of your cluster
to interface with the hardware of that node and Kubernetes' built-in DRA
components. The installation procedure depends on the driver you choose, but is
likely deployed as a daemonset to all or a
selection of the nodes (using selectors or similar mechanisms) in your cluster.

Check your driver's documentation for specific installation instructions, which
might include a Helm chart, a set of manifests, or other deployment tooling.

This tutorial uses an example driver which can be found in the
kubernetes-sigs/dra-example-driver
repository to demonstrate driver installation. This example driver advertises
simulated GPUs to Kubernetes for your Pods to interact with.

### Prepare your cluster for driver installation {#prepare-cluster-driver}

To simplify cleanup, create a namespace named dra-tutorial:

1.  Create the namespace:

    ```shell
    kubectl create namespace dra-tutorial 
    ```

In a production environment, you would likely be using a previously released or
qualified image from the driver vendor or your own organization, and your nodes
would need to have access to the image registry where the driver image is
hosted. In this tutorial, you will use a publicly released image of the
dra-example-driver to simulate access to a DRA driver image.

1.  Confirm your nodes have access to the image by running the following
from within one of your cluster's nodes:

    ```shell
    docker pull registry.k8s.io/dra-example-driver/dra-example-driver:v0.2.0
    ```

### Deploy the DRA driver components

For this tutorial, you will install the critical example resource driver
components individually with `kubectl`.

1.  Create the DeviceClass representing the device types this DRA driver
   supports:

    

    ```shell
    kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/deviceclass.yaml
    ```

1.  Create the ServiceAccount, ClusterRole and ClusterRoleBinding that will
be used by the driver to gain permissions to interact with the Kubernetes API
on this cluster:

      1.  Create the Service Account: 

          

          ```shell
          kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/serviceaccount.yaml
          ```

      1.  Create the ClusterRole: 

          

          ```shell
          kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/clusterrole.yaml
          ```

      1.  Create the ClusterRoleBinding:

          

          ```shell
          kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/clusterrolebinding.yaml
          ```

1.  Create a priority class for the DRA
    driver. The PriorityClass prevents preemption of th  DRA driver component,
    which is responsible for important lifecycle operations for Pods with
    claims. Learn more about pod priority and preemption
    here.

    

    ```shell
    kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/priorityclass.yaml
    ```

1.  Deploy the actual DRA driver as a DaemonSet configured to run the example
   driver binary with the permissions provisioned above. The DaemonSet has the
   permissions that you granted to the ServiceAccount in the previous steps.

    

    ```shell
    kubectl apply --server-side -f http://k8s.io/examples/dra/driver-install/daemonset.yaml
    ```
    The DaemonSet is configured with
      the volume mounts necessary to interact with the underlying Container Device
      Interface (CDI) directory, and to expose its socket to `kubelet` via the
      `kubelet/plugins` directory.

### Verify the DRA driver installation {#verify-driver-install}

1.  Get a list of the Pods of the DRA driver DaemonSet across all worker nodes:

    ```shell
    kubectl get pod -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
    ```
    The output is similar to this:
    ```
    NAME                                     READY   STATUS    RESTARTS   AGE
    dra-example-driver-kubeletplugin-4sk2x   1/1     Running   0          13s
    dra-example-driver-kubeletplugin-cttr2   1/1     Running   0          13s
    ```

1.  The initial responsibility of each node's local DRA driver is to update the
cluster with what devices are available to Pods on that node, by publishing its
metadata to the ResourceSlices API. You can check that API to see that each node
with a driver is advertising the device class it represents. 

    Check for available ResourceSlices: 

    ```shell
    kubectl get resourceslices
    ```
    The output is similar to this:
    ```
    NAME                                 NODE           DRIVER            POOL           AGE
    kind-worker-gpu.example.com-k69gd    kind-worker    gpu.example.com   kind-worker    19s
    kind-worker2-gpu.example.com-qdgpn   kind-worker2   gpu.example.com   kind-worker2   19s
    ```

At this point, you have successfully installed the example DRA driver, and
confirmed its initial configuration. You're now ready to use DRA to schedule
Pods.
