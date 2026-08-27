---
id: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#create-deviceclasses-create-deviceclasses
kind: section
title: Create DeviceClasses {#create-deviceclasses}
source: tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/
heading: Create DeviceClasses {#create-deviceclasses}
parent: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#install-device-drivers-install-drivers
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#clean-up-clean-up
word_count: 198
---

You can define categories of devices that your application operators can
claim in workloads by creating
DeviceClasses. Some device
driver providers might also instruct you to create DeviceClasses during driver
installation.

The ResourceSlices that your driver publishes contain information about the
devices that the driver manages, such as capacity, metadata, and attributes. You
can use cel to filter for properties in your
DeviceClasses, which can make finding devices easier for your workload
operators.

1.  To find the device properties that you can select in DeviceClasses by using
    CEL expressions, get the specification of a ResourceSlice:

    ```shell
    kubectl get resourceslice <resourceslice-name> -o yaml
    ```
    The output is similar to the following:

    ```yaml
    apiVersion: resource.k8s.io/v1
    kind: ResourceSlice
    # lines omitted for clarity
    spec:
      devices:
      - attributes:
          type:
            string: gpu
        capacity:
          memory:
            value: 64Gi
        name: gpu-0
      - attributes:
          type:
            string: gpu
        capacity:
          memory:
            value: 64Gi
        name: gpu-1
      driver: driver.example.com
      nodeName: cluster-1-node-1
    # lines omitted for clarity
    ```
    You can also check the driver provider's documentation for available
    properties and values.

1.  Review the following example DeviceClass manifest, which selects any device
    that's managed by the `driver.example.com` device driver:

    

1.  Create the DeviceClass in your cluster:

    ```shell
    kubectl apply -f https://k8s.io/examples/dra/deviceclass.yaml
    ```
