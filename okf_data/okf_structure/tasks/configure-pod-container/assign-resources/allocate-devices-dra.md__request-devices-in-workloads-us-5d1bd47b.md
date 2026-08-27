---
id: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#request-devices-in-workloads-using-dra-request-devices-workloads
kind: section
title: Request devices in workloads using DRA {#request-devices-workloads}
source: tasks/configure-pod-container/assign-resources/allocate-devices-dra.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/
heading: Request devices in workloads using DRA {#request-devices-workloads}
parent: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#claim-resources-claim-resources
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#clean-up-clean-up
word_count: 227
---

To request device allocation, specify a ResourceClaim or a ResourceClaimTemplate
in the `resourceClaims` field of the Pod specification. Then, request a specific
claim by name in the `resources.claims` field of a container in that Pod.
You can specify multiple entries in the `resourceClaims` field and use specific
claims in different containers.

1. Review the following example Job:

   

   Each Pod in this Job has the following properties:
   
   * Makes a ResourceClaimTemplate named `separate-gpu-claim` and a
     ResourceClaim named `shared-gpu-claim` available to containers.
   * Runs the following containers:
       * `container0` requests the devices from the `separate-gpu-claim` 
         ResourceClaimTemplate. 
       * `container1` and `container2` share access to the devices from the
         `shared-gpu-claim` ResourceClaim.

1. Create the Job: 

   ```shell
   kubectl apply -f https://k8s.io/examples/dra/dra-example-job.yaml
   ```

Try the following troubleshooting steps:

1. When the workload does not start as expected, drill down from Job
   to Pods to ResourceClaims and check the objects
   at each level with `kubectl describe` to see whether there are any
   status fields or events which might explain why the workload is
   not starting.
1. When creating a Pod fails with `must specify one of: resourceClaimName,
   resourceClaimTemplateName`, check that all entries in `pod.spec.resourceClaims`
   have exactly one of those fields set. If they do, then it is possible
   that the cluster has a mutating Pod webhook installed which was built
   against APIs from Kubernetes < 1.32. Work with your cluster administrator
   to check this.
