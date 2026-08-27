---
id: okf-structure/concepts/storage/persistent-volumes.md#claims-as-volumes
kind: section
title: Claims As Volumes
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Claims As Volumes
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#persistentvolumeclaims
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#raw-block-volume-support
word_count: 137
---

Pods access storage by using the claim as a volume. Claims must exist in the
same namespace as the Pod using the claim. The cluster finds the claim in the
Pod's namespace and uses it to get the PersistentVolume backing the claim.
The volume is then mounted to the host and into the Pod.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

### A Note on Namespaces

PersistentVolumes binds are exclusive, and since PersistentVolumeClaims are
namespaced objects, mounting claims with "Many" modes (`ROX`, `RWX`) is only
possible within one namespace.

### PersistentVolumes typed `hostPath`

A `hostPath` PersistentVolume uses a file or directory on the Node to emulate
network-attached storage. See
an example of `hostPath` typed volume.
