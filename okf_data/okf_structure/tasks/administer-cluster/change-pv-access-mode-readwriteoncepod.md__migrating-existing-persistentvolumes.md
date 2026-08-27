---
id: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#migrating-existing-persistentvolumes
kind: section
title: Migrating existing PersistentVolumes
source: tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/
heading: Migrating existing PersistentVolumes
parent: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#why-should-i-use-readwriteoncepod
next_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#whatsnext
word_count: 469
---

If you have existing PersistentVolumes, they can be migrated to use
`ReadWriteOncePod`. Only migrations from `ReadWriteOnce` to `ReadWriteOncePod`
are supported.

In this example, there is already a `ReadWriteOnce` "cat-pictures-pvc"
PersistentVolumeClaim that is bound to a "cat-pictures-pv" PersistentVolume,
and a "cat-pictures-writer" Deployment that uses this PersistentVolumeClaim.

If your storage plugin supports
Dynamic provisioning,
the "cat-pictures-pv" will be created for you, but its name may differ. To get
your PersistentVolume's name run:

```shell
kubectl get pvc cat-pictures-pvc -o jsonpath='{.spec.volumeName}'
```

And you can view the PVC before you make changes. Either view the manifest
locally, or run `kubectl get pvc <name-of-pvc> -o yaml`. The output is similar
to:

```yaml
# cat-pictures-pvc.yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: cat-pictures-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Here's an example Deployment that relies on that PersistentVolumeClaim:

```yaml
# cat-pictures-writer-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cat-pictures-writer
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cat-pictures-writer
  template:
    metadata:
      labels:
        app: cat-pictures-writer
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        volumeMounts:
        - name: cat-pictures
          mountPath: /mnt
      volumes:
      - name: cat-pictures
        persistentVolumeClaim:
          claimName: cat-pictures-pvc
          readOnly: false
```

As a first step, you need to edit your PersistentVolume's
`spec.persistentVolumeReclaimPolicy` and set it to `Retain`. This ensures your
PersistentVolume will not be deleted when you delete the corresponding
PersistentVolumeClaim:

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

Next you need to stop any workloads that are using the PersistentVolumeClaim
bound to the PersistentVolume you want to migrate, and then delete the
PersistentVolumeClaim. Avoid making any other changes to the
PersistentVolumeClaim, such as volume resizes, until after the migration is
complete.

Once that is done, you need to clear your PersistentVolume's `spec.claimRef.uid`
to ensure PersistentVolumeClaims can bind to it upon recreation:

```shell
kubectl scale --replicas=0 deployment cat-pictures-writer
kubectl delete pvc cat-pictures-pvc
kubectl patch pv cat-pictures-pv -p '{"spec":{"claimRef":{"uid":""}}}'
```

After that, replace the PersistentVolume's list of valid access modes to be
(only) `ReadWriteOncePod`:

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"accessModes":["ReadWriteOncePod"]}}'
```

The `ReadWriteOncePod` access mode cannot be combined with other access modes.
Make sure `ReadWriteOncePod` is the only access mode on the PersistentVolume
when updating, otherwise the request will fail.

Next you need to modify your PersistentVolumeClaim to set `ReadWriteOncePod` as
the only access mode. You should also set the PersistentVolumeClaim's
`spec.volumeName` to the name of your PersistentVolume to ensure it binds to
this specific PersistentVolume.

Once this is done, you can recreate your PersistentVolumeClaim and start up your
workloads:

```shell
# IMPORTANT: Make sure to edit your PVC in cat-pictures-pvc.yaml before applying. You need to:
# - Set ReadWriteOncePod as the only access mode
# - Set spec.volumeName to "cat-pictures-pv"

kubectl apply -f cat-pictures-pvc.yaml
kubectl apply -f cat-pictures-writer-deployment.yaml
```

Lastly you may edit your PersistentVolume's `spec.persistentVolumeReclaimPolicy`
and set to it back to `Delete` if you previously changed it.

```shell
kubectl patch pv cat-pictures-pv -p '{"spec":{"persistentVolumeReclaimPolicy":"Delete"}}'
```
