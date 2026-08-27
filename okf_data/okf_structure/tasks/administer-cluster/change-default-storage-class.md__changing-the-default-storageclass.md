---
id: okf-structure/tasks/administer-cluster/change-default-storage-class.md#changing-the-default-storageclass
kind: section
title: Changing the default StorageClass
source: tasks/administer-cluster/change-default-storage-class.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/
heading: Changing the default StorageClass
parent: okf-structure/tasks/administer-cluster/change-default-storage-class
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-default-storage-class.md#why-change-the-default-storage-class
next_sibling: okf-structure/tasks/administer-cluster/change-default-storage-class.md#whatsnext
word_count: 220
---

1. List the StorageClasses in your cluster:

   ```bash
   kubectl get storageclass
   ```

   The output is similar to this:

   ```bash
   NAME                 PROVISIONER               AGE
   standard (default)   kubernetes.io/gce-pd      1d
   gold                 kubernetes.io/gce-pd      1d
   ```

   The default StorageClass is marked by `(default)`.

1. Mark the default StorageClass as non-default:

   The default StorageClass has an annotation
   `storageclass.kubernetes.io/is-default-class` set to `true`. Any other value
   or absence of the annotation is interpreted as `false`.

   To mark a StorageClass as non-default, you need to change its value to `false`:

   ```bash
   kubectl patch storageclass standard -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
   ```

   where `standard` is the name of your chosen StorageClass.

1. Mark a StorageClass as default:

   Similar to the previous step, you need to add/set the annotation
   `storageclass.kubernetes.io/is-default-class=true`.

   ```bash
   kubectl patch storageclass gold -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
   ```

   Please note you can have multiple `StorageClass` marked as default. If more 
   than one `StorageClass` is marked as default, a `PersistentVolumeClaim` without 
   an explicitly defined `storageClassName` will be created using the most recently 
   created default `StorageClass`.
   When a `PersistentVolumeClaim` is created with a specified `volumeName`, it remains 
   in a pending state if the static volume's `storageClassName` does not match the 
   `StorageClass` on the `PersistentVolumeClaim`.

1. Verify that your chosen StorageClass is default:

   ```bash
   kubectl get storageclass
   ```

   The output is similar to this:

   ```bash
   NAME             PROVISIONER               AGE
   standard         kubernetes.io/gce-pd      1d
   gold (default)   kubernetes.io/gce-pd      1d
   ```
