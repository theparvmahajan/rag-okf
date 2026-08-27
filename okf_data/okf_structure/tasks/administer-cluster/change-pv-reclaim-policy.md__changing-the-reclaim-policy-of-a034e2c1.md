---
id: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#changing-the-reclaim-policy-of-a-persistentvolume
kind: section
title: Changing the reclaim policy of a PersistentVolume
source: tasks/administer-cluster/change-pv-reclaim-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/
heading: Changing the reclaim policy of a PersistentVolume
parent: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#why-change-reclaim-policy-of-a-persistentvolume
next_sibling: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#whatsnext
word_count: 240
---

1. List the PersistentVolumes in your cluster:

   ```shell
   kubectl get pv
   ```

   The output is similar to this:

   ```none
   NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
   pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
   pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
   pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
   ```

   This list also includes the name of the claims that are bound to each volume
   for easier identification of dynamically provisioned volumes.

1. Choose one of your PersistentVolumes and change its reclaim policy:

   ```shell
   kubectl patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
   ```

   where `<your-pv-name>` is the name of your chosen PersistentVolume.

   
   On Windows, you must _double_ quote any JSONPath template that contains spaces (not single
   quote as shown above for bash). This in turn means that you must use a single quote or escaped
   double quote around any literals in the template. For example:

   ```cmd
   kubectl patch pv <your-pv-name> -p "{\"spec\":{\"persistentVolumeReclaimPolicy\":\"Retain\"}}"
   ```
   

1. Verify that your chosen PersistentVolume has the right policy:

   ```shell
   kubectl get pv
   ```

   The output is similar to this:

   ```none
   NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
   pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     40s
   pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     36s
   pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     33s
   ```

   In the preceding output, you can see that the volume bound to claim
   `default/claim3` has reclaim policy `Retain`. It will not be automatically
   deleted when a user deletes claim `default/claim3`.
