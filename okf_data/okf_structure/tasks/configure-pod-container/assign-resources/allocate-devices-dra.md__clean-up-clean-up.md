---
id: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#clean-up-clean-up
kind: section
title: Clean up {#clean-up}
source: tasks/configure-pod-container/assign-resources/allocate-devices-dra.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/
heading: Clean up {#clean-up}
parent: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#request-devices-in-workloads-using-dra-request-devices-workloads
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#whatsnext
word_count: 57
---

To delete the Kubernetes objects that you created in this task, follow these
steps:

1.  Delete the example Job:

    ```shell
    kubectl delete -f https://k8s.io/examples/dra/dra-example-job.yaml
    ```

1.  To delete your resource claims, run one of the following commands:

    * Delete the ResourceClaimTemplate:

      ```shell
      kubectl delete -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml
      ```
    * Delete the ResourceClaim:

      ```shell
      kubectl delete -f https://k8s.io/examples/dra/resourceclaim.yaml
      ```
