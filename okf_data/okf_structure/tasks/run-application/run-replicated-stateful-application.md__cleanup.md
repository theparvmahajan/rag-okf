---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#cleanup
kind: section
title: Cleanup
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Cleanup
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#scaling-the-number-of-replicas
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#whatsnext
word_count: 150
---

1. Cancel the `SELECT @@server_id` loop by pressing **Ctrl+C** in its terminal,
   or running the following from another terminal:

   ```shell
   kubectl delete pod mysql-client-loop --now
   ```

1. Delete the StatefulSet. This also begins terminating the Pods.

   ```shell
   kubectl delete statefulset mysql
   ```

1. Verify that the Pods disappear.
   They might take some time to finish terminating.

   ```shell
   kubectl get pods -l app=mysql
   ```

   You'll know the Pods have terminated when the above returns:

   ```
   No resources found.
   ```

1. Delete the ConfigMap, Services, and PersistentVolumeClaims.

   ```shell
   kubectl delete configmap,service,pvc -l app=mysql
   ```

1. If you manually provisioned PersistentVolumes, you also need to manually
   delete them, as well as release the underlying resources.
   If you used a dynamic provisioner, it automatically deletes the
   PersistentVolumes when it sees that you deleted the PersistentVolumeClaims.
   Some dynamic provisioners (such as those for EBS and PD) also release the
   underlying resources upon deleting the PersistentVolumes.
