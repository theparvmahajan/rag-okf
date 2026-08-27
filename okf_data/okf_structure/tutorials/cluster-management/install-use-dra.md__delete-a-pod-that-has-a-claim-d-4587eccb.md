---
id: okf-structure/tutorials/cluster-management/install-use-dra.md#delete-a-pod-that-has-a-claim-delete-pod-claim
kind: section
title: Delete a Pod that has a claim {#delete-pod-claim}
source: tutorials/cluster-management/install-use-dra.md
url: https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/
heading: Delete a Pod that has a claim {#delete-pod-claim}
parent: okf-structure/tutorials/cluster-management/install-use-dra
children: []
prev_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#claim-resources-and-deploy-a-pod-claim-resources-pod
next_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#cleanup
word_count: 223
---

When a Pod with a claim is deleted, the DRA driver deallocates the resource so
it can be available for future scheduling. To validate this behavior, delete the
Pod that you created in the previous steps and watch the corresponding changes
to the ResourceClaim and driver.

1.  Delete the `pod0` Pod:

    ```shell
    kubectl delete pod pod0 -n dra-tutorial
    ```

    The output is similar to this:

    ```
    pod "pod0" deleted
    ```

### Observe the DRA state

When the Pod is deleted, the driver deallocates the device from the
ResourceClaim and updates the ResourceClaim resource in the Kubernetes API. The
ResourceClaim has a `pending` state until it's referenced in a new Pod.

1.  Check the state of the `some-gpu` ResourceClaim:

    ```shell
    kubectl get resourceclaims -n dra-tutorial
    ```

    The output is similar to this:
    ```
    NAME       STATE     AGE
    some-gpu   pending   76s
    ```

1.  Verify that the driver has processed unpreparing the device for this claim by
   checking the driver logs:

    ```shell
    kubectl logs -l app.kubernetes.io/name=dra-example-driver -n dra-tutorial
    ```
    The output is similar to this:
    ```
    I0820 18:22:15.629376       1 driver.go:138] UnprepareResourceClaims is called: number of claims: 1
    ```

You have now deleted a Pod that had a claim, and observed that the driver took
action to unprepare the underlying hardware resource and update the DRA APIs to
reflect that the resource is available again for future scheduling.
