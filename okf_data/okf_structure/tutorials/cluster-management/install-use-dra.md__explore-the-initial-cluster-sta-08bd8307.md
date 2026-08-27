---
id: okf-structure/tutorials/cluster-management/install-use-dra.md#explore-the-initial-cluster-state-explore-initial-state
kind: section
title: Explore the initial cluster state {#explore-initial-state}
source: tutorials/cluster-management/install-use-dra.md
url: https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/
heading: Explore the initial cluster state {#explore-initial-state}
parent: okf-structure/tutorials/cluster-management/install-use-dra
children: []
prev_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#prerequisites
next_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#install-an-example-dra-driver-install-example-driver
word_count: 162
---

You can spend some time to observe the initial state of a cluster with DRA
enabled, especially if you have not used these APIs extensively before. If you
set up a new cluster for this tutorial, with no driver installed and no Pod
claims yet to satisfy, the output of these commands won't show any resources.

1.  Get a list of DeviceClasses:

    ```shell
    kubectl get deviceclasses
    ```
    The output is similar to this:
    ```
    No resources found
    ```

1.  Get a list of  ResourceSlices:

    ```shell
    kubectl get resourceslices
    ```
    The output is similar to this:
    ```
    No resources found
    ```

1.  Get a list of ResourceClaims and ResourceClaimTemplates

    ```shell
    kubectl get resourceclaims -A
    kubectl get resourceclaimtemplates -A
    ```
    The output is similar to this:
    ```
    No resources found
    No resources found
    ```

At this point, you have confirmed that DRA is enabled and configured properly in
the cluster, and that no DRA drivers have advertised any resources to the DRA
APIs yet.
