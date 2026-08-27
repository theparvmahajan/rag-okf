---
id: okf-structure/concepts/storage/volumes.md#types-of-volumes-volume-types
kind: section
title: Types of volumes {#volume-types}
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: Types of volumes {#volume-types}
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: okf-structure/concepts/storage/volumes.md#how-volumes-work
next_sibling: okf-structure/concepts/storage/volumes.md#using-subpath-using-subpath
word_count: 3401
---

Kubernetes supports several types of volumes.

### configMap

A ConfigMap
provides a way to inject configuration data into Pods.
The data stored in a ConfigMap can be referenced in a volume of type
`configMap` and then consumed by containerized applications running in a Pod.

When referencing a ConfigMap, you provide the name of the ConfigMap in the
volume. You can customize the path to use for a specific
entry in the ConfigMap. The following configuration shows how to mount
the `log-config` ConfigMap onto a Pod called `configmap-pod`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod
spec:
  containers:
    - name: test
      image: busybox:1.28
      command: ['sh', '-c', 'echo "The app is running!" && tail -f /dev/null']
      volumeMounts:
        - name: config-vol
          mountPath: /etc/config
  volumes:
    - name: config-vol
      configMap:
        name: log-config
        items:
          - key: log_level
            path: log_level.conf
```

The `log-config` ConfigMap is mounted as a volume, and all contents stored in
its `log_level` entry are mounted into the Pod at path `/etc/config/log_level.conf`.
Note that this path is derived from the volume's `mountPath` and the `path`
keyed with `log_level`.

* You must create a ConfigMap
  before you can use it.

* A ConfigMap is always mounted as `readOnly`.

* A container using a ConfigMap as a `subPath` volume mount will not
  receive updates when the ConfigMap changes.
  
* Text data is exposed as files using the UTF-8 character encoding.
  For other character encodings, use `binaryData`.

### downwardAPI {#downwardapi}

A `downwardAPI` volume makes downward API
data available to applications. Within the volume, you can find the exposed
data as read-only files in plain text format.

A container using the downward API as a `subPath` volume mount does not
receive updates when field values change.

See Expose Pod Information to Containers Through Files
to learn more.

### emptyDir {#emptydir}

For a Pod that defines an `emptyDir` volume, the volume is created when the Pod is assigned to a node.
As the name says, the `emptyDir` volume is initially empty. All containers in the Pod can read and write the same
files in the `emptyDir` volume, though that volume can be mounted at the same
or different paths in each container. When a Pod is removed from a node for
any reason, the data in the `emptyDir` is deleted permanently.

A container crashing does *not* remove a Pod from a node. The data in an `emptyDir` volume
is safe across container crashes.

Some uses for an `emptyDir` are:

* scratch space, such as for a disk-based merge sort
* checkpointing a long computation for recovery from crashes
* holding files that a content-manager container fetches while a webserver
  container serves the data

The `emptyDir.medium` field controls where `emptyDir` volumes are stored. By
default `emptyDir` volumes are stored on whatever medium that backs the node
such as disk, SSD, or network storage, depending on your environment. If you set
the `emptyDir.medium` field to `"Memory"`, Kubernetes mounts a tmpfs (RAM-backed
filesystem) for you instead. While tmpfs is very fast, be aware that, unlike
disks, files you write count against the memory limit of the container that wrote them.

A size limit can be specified for the default medium, which limits the capacity
of the `emptyDir` volume. The storage is allocated from
node ephemeral storage.
If that is filled up from another source (for example, log files or image overlays),
the `emptyDir` may run out of capacity before this limit.
If no size is specified, memory-backed volumes are sized to node allocatable memory.

Please check here
for points to note in terms of resource management when using memory-backed `emptyDir`.

#### emptyDir configuration example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      sizeLimit: 500Mi
```

#### emptyDir memory configuration example

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir:
      sizeLimit: 500Mi
      medium: Memory
```

### fc (fibre channel) {#fc}

An `fc` volume type allows an existing fibre channel block storage volume
to be mounted in a Pod. You can specify single or multiple target world wide names (WWNs)
using the parameter `targetWWNs` in your Volume configuration. If multiple WWNs are specified,
targetWWNs expect that those WWNs are from multi-path connections.

You must configure FC SAN Zoning to allocate and mask those LUNs (volumes) to the target WWNs
beforehand so that Kubernetes hosts can access them.

### gcePersistentDisk (deprecated) {#gcepersistentdisk}

In Kubernetes , all operations for the in-tree `gcePersistentDisk` type
are redirected to the `pd.csi.storage.gke.io` CSI driver.

The `gcePersistentDisk` in-tree storage driver was deprecated in the Kubernetes v1.17 release
and then removed entirely in the v1.28 release.

The Kubernetes project suggests that you use the
Google Compute Engine Persistent Disk CSI
third party storage driver instead.

### gitRepo (disabled) {#gitrepo}

Kubernetes  does *not* include the `gitRepo` volume
driver. The last version that provided a way to use this driver was Kubernetes
v1.35, and it has been deprecated since the v1.11 minor
release.

To provision a Pod that has a Git repository mounted, you can mount an
`emptyDir` volume into an init container
that clones the repo using Git, then mount the EmptyDir into the Pod's container.

---

You can restrict the use of `gitRepo` volumes in your cluster using
policies, such as
ValidatingAdmissionPolicy.
You can use the following Common Expression Language (CEL) expression as
part of a policy to reject use of `gitRepo` volumes:

```cel
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))
```

### hostPath {#hostpath}

A `hostPath` volume mounts a file or directory from the host node's filesystem
into your Pod. This is not something that most Pods will need, but it offers a
powerful escape hatch for some applications.

Using the `hostPath` volume type presents many security risks.
If you can avoid using a `hostPath` volume, you should. For example,
define a `local` PersistentVolume, and use that instead.

If you are restricting access to specific directories on the node using
admission-time validation, that restriction is only effective when you
additionally require that any mounts of that `hostPath` volume are
**read only**. If you allow a read-write mount of any host path by an
untrusted Pod, the containers in that Pod may be able to subvert the
read-write host mount.

---

Take care when using `hostPath` volumes, whether these are mounted as read-only
or as read-write, because:

* Access to the host filesystem can expose privileged system credentials (such as for the kubelet) or privileged APIs
  (such as the container runtime socket) that can be used for container escape or to attack other
  parts of the cluster.
* Pods with identical configuration (such as created from a PodTemplate) may
  behave differently on different nodes due to different files on the nodes.
* `hostPath` volume usage is not treated as ephemeral storage usage.
  You need to monitor the disk usage by yourself because excessive `hostPath` disk
  usage will lead to disk pressure on the node.

Some uses for a `hostPath` are:

* running a container that needs access to node-level system components
  (such as a container that transfers system logs to a central location,
  accessing those logs using a read-only mount of `/var/log`)
* making a configuration file stored on the host system available read-only
  to a static Pod;
  unlike normal Pods, static Pods cannot access ConfigMaps

#### `hostPath` volume types

In addition to the required `path` property, you can optionally specify a
`type` for a `hostPath` volume.

The available values for `type` are:

| Value | Behavior |
|:------|:---------|
| `‌""` | Empty string (default) is for backward compatibility, which means that no checks will be performed before mounting the `hostPath` volume. |
| `DirectoryOrCreate` | If nothing exists at the given path, an empty directory will be created there as needed with permission set to 0755, having the same group and ownership with Kubelet. |
| `Directory` | A directory must exist at the given path. |
| `FileOrCreate` | If nothing exists at the given path, an empty file will be created there as needed with permission set to 0644, having the same group and ownership with Kubelet. |
| `File` | A file must exist at the given path. |
| `Socket` | A UNIX socket must exist at the given path. |
| `CharDevice` | _(Linux nodes only)_ A character device must exist at the given path. |
| `BlockDevice` | _(Linux nodes only)_ A block device must exist at the given path. |

The `FileOrCreate` mode does **not** create the parent directory of the file. If the parent directory
of the mounted file does not exist, the Pod fails to start. To ensure that this mode works,
you can try to mount directories and files separately, as shown in the
`FileOrCreate` example for `hostPath`.

Some files or directories created on the underlying hosts might only be
accessible by root. You then either need to run your process as root in a
privileged container
or modify the file permissions on the host to read from or write to a `hostPath` volume.

#### hostPath configuration example

---
# This manifest mounts /data/foo on the host as /foo inside the
# single container that runs within the hostpath-example-linux Pod.
#
# The mount into the container is read-only.
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-example-linux
spec:
  os: { name: linux }
  nodeSelector:
    kubernetes.io/os: linux
  containers:
  - name: example-container
    image: registry.k8s.io/test-webserver
    volumeMounts:
    - mountPath: /foo
      name: example-volume
      readOnly: true
  volumes:
  - name: example-volume
    # mount /data/foo, but only if that directory already exists
    hostPath:
      path: /data/foo # directory location on host
      type: Directory # this field is optional

---
# This manifest mounts C:\Data\foo on the host as C:\foo, inside the
# single container that runs within the hostpath-example-windows Pod.
#
# The mount into the container is read-only.
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-example-windows
spec:
  os: { name: windows }
  nodeSelector:
    kubernetes.io/os: windows
  containers:
  - name: example-container
    image: microsoft/windowsservercore:1709
    volumeMounts:
    - name: example-volume
      mountPath: "C:\\foo"
      readOnly: true
  volumes:
    # mount C:\Data\foo from the host, but only if that directory already exists
  - name: example-volume
    hostPath:
      path: "C:\\Data\\foo" # directory location on host
      type: Directory       # this field is optional

#### hostPath FileOrCreate configuration example {#hostpath-fileorcreate-example}

The following manifest defines a Pod that mounts `/var/local/aaa`
inside the single container in the Pod. If the node does not
already have a path `/var/local/aaa`, the kubelet creates
it as a directory and then mounts it into the Pod.

If `/var/local/aaa` already exists but is not a directory,
the Pod fails. Additionally, the kubelet attempts to make
a file named `/var/local/aaa/1.txt` inside that directory
(as seen from the host); if something already exists at
that path and isn't a regular file, the Pod fails.

Here's the example manifest:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-webserver
spec:
  os: { name: linux }
  nodeSelector:
    kubernetes.io/os: linux
  containers:
  - name: test-webserver
    image: registry.k8s.io/test-webserver:latest
    volumeMounts:
    - mountPath: /var/local/aaa
      name: mydir
    - mountPath: /var/local/aaa/1.txt
      name: myfile
  volumes:
  - name: mydir
    hostPath:
      # Ensure the file directory is created.
      path: /var/local/aaa
      type: DirectoryOrCreate
  - name: myfile
    hostPath:
      path: /var/local/aaa/1.txt
      type: FileOrCreate
```

### image

An `image` volume source represents an OCI object (a container image or
artifact) which is available on the kubelet's host machine.

An example of using the `image` volume source is:

The volume is resolved at Pod startup, depending on which `pullPolicy` value is
provided:

`Always`
: The kubelet always attempts to pull the reference. If the pull fails,
  the kubelet sets the Pod to `Failed`.

`Never`
: The kubelet never pulls the reference and only uses a local image or artifact.
  The Pod becomes `Failed` if any layers of the image aren't already present locally,
  or if the manifest for that image isn't already cached.

`IfNotPresent`
: The kubelet pulls if the reference isn't already present on disk. The Pod becomes
  `Failed` if the reference isn't present and the pull fails.

The volume gets re-resolved if the Pod gets deleted and recreated, which means
that new remote content will become available on Pod recreation. A failure to
resolve or pull the image during Pod startup will block containers from starting
and may add significant latency. Failures will be retried using normal volume
backoff and will be reported on the Pod reason and message.

The types of objects that may be mounted by this volume are defined by the
container runtime implementation on a host machine. At a minimum, they must include
all valid types supported by the container image field. The OCI object gets
mounted in a single directory (`spec.containers[*].volumeMounts[*].mountPath`)
and will be mounted read-only.

Besides that:

- `subPath` or
  `subPathExpr`
  mounts for containers (`spec.containers[*].volumeMounts[*].subPath`, `spec.containers[*].volumeMounts[*].subPathExpr`)
  are only supported from Kubernetes v1.33.
- The field `spec.securityContext.fsGroupChangePolicy` has no effect on this
  volume type.
- The `AlwaysPullImages` Admission Controller
  does also work for this volume source like for container images.

The following fields are available for the `image` type:

`reference`
: Artifact reference to be used. For example, you could specify
  `registry.k8s.io/conformance:v` to load the
  files from the Kubernetes conformance test image. Behaves in the same way as
  `pod.spec.containers[*].image`. Pull secrets will be assembled in the same way
  as for the container image by looking up node credentials, service account image
  pull secrets, and Pod spec image pull secrets. This field is optional to allow
  higher level config management to default or override container images in
  workload controllers like Deployments and StatefulSets.
  More info about container images.

`pullPolicy`
: Policy for pulling OCI objects. Possible values are: `Always`, `Never`, or
  `IfNotPresent`. Defaults to `Always` if `:latest` tag is specified, or
  `IfNotPresent` otherwise.

See the _Use an Image Volume With a Pod_
example for more details on how to use the volume source.

#### Pod status and `image` volumes {#image-volume-pod-status}

If the `ImageVolumeWithDigest` feature gate
is enabled in your cluster,
then whenever you specify an `image` volume for a Pod,
the kubelet updates the Pod status to record the _digest_
of the container image that's being used as a volume source.

Here's a simplified example of a running Pod, represented as YAML, including the status update.
Note the new `ImageRef` field under `volumeMounts` in the container status.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: docker.io/library/debian:12
    volumeMounts:
    - name: artifact
      mountPath: /data
  volumes:
  - name: artifact
    image:
      reference: quay.io/crio/artifact:v2
      pullPolicy: IfNotPresent
status:
  containerStatuses:
  - containerID: containerd://examplecontainerid1234567890abcdef
    image: docker.io/library/debian:12
    imageID: docker-pullable://docker.io/library/debian@sha256:3f1d6c17773a45c97bd8f158d665c9709d7b29ed7917ac934086ad96f92e4510
    volumeMounts:
    - name: artifact
      mountPath: /data
      readOnly: true
      imageRef: quay.io/crio/artifact@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

### iscsi

An `iscsi` volume allows an existing iSCSI (SCSI over IP) volume to be mounted
into your Pod. Unlike `emptyDir`, which is erased when a Pod is removed, the
contents of an `iscsi` volume are preserved, and the volume is merely
unmounted. This means that an iscsi volume can be pre-populated with data, and
that data can be shared between Pods.

You must have your own iSCSI server running with the volume created before you can use it.

A feature of iSCSI is that it can be mounted as read-only by multiple consumers
simultaneously. This means that you can pre-populate a volume with your dataset
and then serve it in parallel from as many Pods as you need. Unfortunately,
iSCSI volumes can only be mounted by a single consumer in read-write mode.
Simultaneous writers are not allowed.

### local

A `local` volume represents a mounted local storage device such as a disk,
partition or directory.

Local volumes can only be used as a statically created PersistentVolume. Dynamic
provisioning is not supported.

Compared to `hostPath` volumes, `local` volumes are used in a durable and
portable manner without manually scheduling Pods to nodes. The system is aware
of the volume's node constraints by looking at the node affinity on the PersistentVolume.

However, `local` volumes are subject to the availability of the underlying
node and are not suitable for all applications. If a node becomes unhealthy,
then the `local` volume becomes inaccessible to the Pod. The Pod using this volume
is unable to run. Applications using `local` volumes must be able to tolerate this
reduced availability, as well as potential data loss, depending on the
durability characteristics of the underlying disk.

The following example shows a PersistentVolume using a `local` volume and
`nodeAffinity`:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: example-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Delete
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - example-node
```

You must set a PersistentVolume `nodeAffinity` when using `local` volumes.
The Kubernetes scheduler uses the PersistentVolume `nodeAffinity` to schedule
these Pods to the correct node.

PersistentVolume `volumeMode` can be set to "Block" (instead of the default
value "Filesystem") to expose the local volume as a raw block device.

When using local volumes, it is recommended to create a StorageClass with
`volumeBindingMode` set to `WaitForFirstConsumer`. For more details, see the
local StorageClass example.
Delaying volume binding ensures that the PersistentVolumeClaim binding decision
will also be evaluated with any other node constraints the Pod may have,
such as node resource requirements, node selectors, Pod affinity, and Pod anti-affinity.

An external static provisioner can be run separately for improved management of
the local volume lifecycle. Note that this provisioner does not support dynamic
provisioning yet. For an example on how to run an external local provisioner, see the
local volume provisioner user guide.

The local PersistentVolume requires manual cleanup and deletion by the
user if the external static provisioner is not used to manage the volume
lifecycle.

### nfs

An `nfs` volume allows an existing NFS (Network File System) share to be
mounted into a Pod. Unlike `emptyDir`, which is erased when a Pod is
removed, the contents of an `nfs` volume are preserved, and the volume is merely
unmounted. This means that an NFS volume can be pre-populated with data, and
that data can be shared between Pods. NFS can be mounted by multiple
writers simultaneously.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /my-nfs-data
      name: test-volume
  volumes:
  - name: test-volume
    nfs:
      server: my-nfs-server.example.com
      path: /my-nfs-volume
      readOnly: true
```

You must have your own NFS server running with the share exported before you can use it.

Also note that you can't specify NFS mount options in a Pod spec. You can either set mount options server-side or
use /etc/nfsmount.conf.
You can also mount NFS volumes via PersistentVolumes, which do allow you to set mount options.

### persistentVolumeClaim {#persistentvolumeclaim}

A `persistentVolumeClaim` volume is used to mount a
PersistentVolume into a Pod. PersistentVolumeClaims
are a way for users to "claim" durable storage (such as an iSCSI volume)
without knowing the details of the particular cloud environment.

See the information about PersistentVolumes for more
details.

### portworxVolume (deprecated) {#portworxvolume}

A `portworxVolume` is an elastic block storage layer that runs hyperconverged with
Kubernetes. Portworx fingerprints storage
in a server, tiers based on capabilities, and aggregates capacity across multiple servers.
Portworx runs in-guest in virtual machines or on bare metal Linux nodes.

A `portworxVolume` can be dynamically created through Kubernetes, or it can also
be pre-provisioned and referenced inside a Pod.
Here is an example Pod referencing a pre-provisioned Portworx volume:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-portworx-volume-pod
spec:
  containers:
  - image: registry.k8s.io/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /mnt
      name: pxvol
  volumes:
  - name: pxvol
    # This Portworx volume must already exist.
    portworxVolume:
      volumeID: "pxvol"
      fsType: "<fs-type>"
```

Make sure you have an existing PortworxVolume with the name `pxvol`
before using it in the Pod.

#### Portworx CSI migration

In Kubernetes , all operations for the in-tree
Portworx volumes are redirected to the `pxd.portworx.com` 
Container Storage Interface (CSI) Driver by default.  
Portworx CSI Driver
must be installed on the cluster.

### projected

A projected volume maps several existing volume sources into the same
directory. For more details, see projected volumes.

### secret

A `secret` volume is used to pass sensitive information, such as passwords, to
Pods. You can store secrets in the Kubernetes API and mount them as files for
use by Pods without coupling to Kubernetes directly. `secret` volumes are
backed by tmpfs (a RAM-backed filesystem), so they are never written to
non-volatile storage.

* You must create a Secret in the Kubernetes API before you can use it.

* A Secret is always mounted as `readOnly`.

* A container using a Secret as a `subPath` volume mount will not
  receive Secret updates.

For more details, see Configuring Secrets.
