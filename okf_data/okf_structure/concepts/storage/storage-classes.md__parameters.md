---
id: okf-structure/concepts/storage/storage-classes.md#parameters
kind: section
title: Parameters
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: Parameters
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: okf-structure/concepts/storage/storage-classes.md#allowed-topologies
next_sibling: null
word_count: 1417
---

StorageClasses have parameters that describe volumes belonging to the storage
class. Different parameters may be accepted depending on the `provisioner`.
When a parameter is omitted, some default is used.

There can be at most 512 parameters defined for a StorageClass.
The total length of the parameters object including its keys and values cannot
exceed 256 KiB.

### AWS EBS

Kubernetes  does not include a `awsElasticBlockStore` volume type.

The AWSElasticBlockStore in-tree storage driver was deprecated in the Kubernetes v1.19 release
and then removed entirely in the v1.27 release.

The Kubernetes project suggests that you use the AWS EBS
out-of-tree storage driver instead.

Here is an example StorageClass for the AWS EBS CSI driver:

`tagSpecification`: Tags with this prefix are applied to dynamically provisioned EBS volumes.

### AWS EFS

To configure AWS EFS storage, you can use the out-of-tree AWS_EFS_CSI_DRIVER.

- `provisioningMode`: The type of volume to be provisioned by Amazon EFS. Currently, only access point based provisioning is supported (`efs-ap`).
- `fileSystemId`: The file system under which the access point is created.
- `directoryPerms`: The directory permissions of the root directory created by the access point.

For more details, refer to the AWS_EFS_CSI_Driver Dynamic Provisioning documentation.

### NFS

To configure NFS storage, you can use the in-tree driver or the
NFS CSI driver for Kubernetes
(recommended).

- `server`: Server is the hostname or IP address of the NFS server.
- `path`: Path that is exported by the NFS server.
- `readOnly`: A flag indicating whether the storage will be mounted as read only (default false).

Kubernetes doesn't include an internal NFS provisioner.
You need to use an external provisioner to create a StorageClass for NFS.
Here are some examples:

- NFS Ganesha server and external provisioner
- NFS subdir external provisioner

### vSphere

There are two types of provisioners for vSphere storage classes:

- CSI provisioner: `csi.vsphere.vmware.com`
- vCP provisioner: `kubernetes.io/vsphere-volume`

In-tree provisioners are deprecated.
For more information on the CSI provisioner, see
Kubernetes vSphere CSI Driver and
vSphereVolume CSI migration.

#### CSI Provisioner {#vsphere-provisioner-csi}

The vSphere CSI StorageClass provisioner works with Tanzu Kubernetes clusters.
For an example, refer to the vSphere CSI repository.

#### vCP Provisioner

The following examples use the VMware Cloud Provider (vCP) StorageClass provisioner.

1. Create a StorageClass with a user specified disk format.

   ```yaml
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
   ```

   `diskformat`: `thin`, `zeroedthick` and `eagerzeroedthick`. Default: `"thin"`.

2. Create a StorageClass with a disk format on a user specified datastore.

   ```yaml
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
     datastore: VSANDatastore
   ```

   `datastore`: The user can also specify the datastore in the StorageClass.
   The volume will be created on the datastore specified in the StorageClass,
   which in this case is `VSANDatastore`. This field is optional. If the
   datastore is not specified, then the volume will be created on the datastore
   specified in the vSphere config file used to initialize the vSphere Cloud
   Provider.

3. Storage Policy Management inside kubernetes

   - Using existing vCenter SPBM policy

     One of the most important features of vSphere for Storage Management is
     policy based Management. Storage Policy Based Management (SPBM) is a
     storage policy framework that provides a single unified control plane
     across a broad range of data services and storage solutions. SPBM enables
     vSphere administrators to overcome upfront storage provisioning challenges,
     such as capacity planning, differentiated service levels and managing
     capacity headroom.

     The SPBM policies can be specified in the StorageClass using the
     `storagePolicyName` parameter.

   - Virtual SAN policy support inside Kubernetes

     Vsphere Infrastructure (VI) Admins will have the ability to specify custom
     Virtual SAN Storage Capabilities during dynamic volume provisioning. You
     can now define storage requirements, such as performance and availability,
     in the form of storage capabilities during dynamic volume provisioning.
     The storage capability requirements are converted into a Virtual SAN
     policy which are then pushed down to the Virtual SAN layer when a
     persistent volume (virtual disk) is being created. The virtual disk is
     distributed across the Virtual SAN datastore to meet the requirements.

     You can see Storage Policy Based Management for dynamic provisioning of volumes
     for more details on how to use storage policies for persistent volumes
     management.

### Ceph RBD (deprecated) {#ceph-rbd}

This internal provisioner of Ceph RBD is deprecated. Please use
CephFS RBD CSI driver.

- `monitors`: Ceph monitors, comma delimited. This parameter is required.
- `adminId`: Ceph client ID that is capable of creating images in the pool.
  Default is "admin".
- `adminSecretName`: Secret Name for `adminId`. This parameter is required.
  The provided secret must have type "kubernetes.io/rbd".
- `adminSecretNamespace`: The namespace for `adminSecretName`. Default is "default".
- `pool`: Ceph RBD pool. Default is "rbd".
- `userId`: Ceph client ID that is used to map the RBD image. Default is the
  same as `adminId`.
- `userSecretName`: The name of Ceph Secret for `userId` to map RBD image. It
  must exist in the same namespace as PVCs. This parameter is required.
  The provided secret must have type "kubernetes.io/rbd", for example created in this
  way:

  ```shell
  kubectl create secret generic ceph-secret --type="kubernetes.io/rbd" \
    --from-literal=key='QVFEQ1pMdFhPUnQrSmhBQUFYaERWNHJsZ3BsMmNjcDR6RFZST0E9PQ==' \
    --namespace=kube-system
  ```

- `userSecretNamespace`: The namespace for `userSecretName`.
- `fsType`: fsType that is supported by kubernetes. Default: `"ext4"`.
- `imageFormat`: Ceph RBD image format, "1" or "2". Default is "2".
- `imageFeatures`: This parameter is optional and should only be used if you
  set `imageFormat` to "2". Currently supported features are `layering` only.
  Default is "", and no features are turned on.

### Azure Disk

Kubernetes  does not include a `azureDisk` volume type.

The `azureDisk` in-tree storage driver was deprecated in the Kubernetes v1.19 release
and then removed entirely in the v1.27 release.

The Kubernetes project suggests that you use the Azure Disk third party
storage driver instead.

### Azure File (deprecated) {#azure-file}

- `skuName`: Azure storage account SKU tier. Default is empty.
- `location`: Azure storage account location. Default is empty.
- `storageAccount`: Azure storage account name. Default is empty. If a storage
  account is not provided, all storage accounts associated with the resource
  group are searched to find one that matches `skuName` and `location`. If a
  storage account is provided, it must reside in the same resource group as the
  cluster, and `skuName` and `location` are ignored.
- `secretNamespace`: the namespace of the secret that contains the Azure Storage
  Account Name and Key. Default is the same as the Pod.
- `secretName`: the name of the secret that contains the Azure Storage Account Name and
  Key. Default is `azure-storage-account-<accountName>-secret`
- `readOnly`: a flag indicating whether the storage will be mounted as read only.
  Defaults to false which means a read/write mount. This setting will impact the
  `ReadOnly` setting in VolumeMounts as well.

During storage provisioning, a secret named by `secretName` is created for the
mounting credentials. If the cluster has enabled both
RBAC and
Controller Roles,
add the `create` permission of resource `secret` for clusterrole
`system:controller:persistent-volume-binder`.

In a multi-tenancy context, it is strongly recommended to set the value for
`secretNamespace` explicitly, otherwise the storage account credentials may
be read by other users.

### Portworx volume (deprecated) {#portworx-volume}

- `fs`: filesystem to be laid out: `none/xfs/ext4` (default: `ext4`).
- `block_size`: block size in Kbytes (default: `32`).
- `repl`: number of synchronous replicas to be provided in the form of
  replication factor `1..3` (default: `1`) A string is expected here i.e.
  `"1"` and not `1`.
- `priority_io`: determines whether the volume will be created from higher
  performance or a lower priority storage `high/medium/low` (default: `low`).
- `snap_interval`: clock/time interval in minutes for when to trigger snapshots.
  Snapshots are incremental based on difference with the prior snapshot, 0
  disables snaps (default: `0`). A string is expected here i.e.
  `"70"` and not `70`.
- `aggregation_level`: specifies the number of chunks the volume would be
  distributed into, 0 indicates a non-aggregated volume (default: `0`). A string
  is expected here i.e. `"0"` and not `0`
- `ephemeral`: specifies whether the volume should be cleaned-up after unmount
  or should be persistent. `emptyDir` use case can set this value to true and
  `persistent volumes` use case such as for databases like Cassandra should set
  to false, `true/false` (default `false`). A string is expected here i.e.
  `"true"` and not `true`.

### Local

Local volumes do not support dynamic provisioning in Kubernetes ;
however a StorageClass should still be created to delay volume binding until a Pod is actually
scheduled to the appropriate node. This is specified by the `WaitForFirstConsumer` volume
binding mode.

Delaying volume binding allows the scheduler to consider all of a Pod's
scheduling constraints when choosing an appropriate PersistentVolume for a
PersistentVolumeClaim.
