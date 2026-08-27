---
id: okf-structure/tasks/administer-cluster/kubelet-config-file.md#create-the-config-file
kind: section
title: Create the config file
source: tasks/administer-cluster/kubelet-config-file.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/
heading: Create the config file
parent: okf-structure/tasks/administer-cluster/kubelet-config-file
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#start-a-kubelet-process-configured-via-the-config-file
word_count: 269
---

The subset of the kubelet's configuration that can be configured via a file
is defined by the
`KubeletConfiguration`
struct.

The configuration file must be a JSON or YAML representation of the parameters
in this struct. Make sure the kubelet has read permissions on the file.

Here is an example of what this file might look like:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
address: "192.168.0.8"
port: 20250
serializeImagePulls: false
evictionHard:
    memory.available:  "100Mi"
    nodefs.available:  "10%"
    nodefs.inodesFree: "5%"
    imagefs.available: "15%"
    imagefs.inodesFree: "5%"
```

In this example, the kubelet is configured with the following settings:

1. `address`: The kubelet will serve on IP address `192.168.0.8`.
1. `port`: The kubelet will serve on port `20250`.
1. `serializeImagePulls`: Image pulls will be done in parallel.
1. `evictionHard`: The kubelet will evict Pods under one of the following conditions:

   - When the node's available memory drops below 100MiB.
   - When the node's main filesystem's available space is less than 10%.
   - When the image filesystem's available space is less than 15%.
   - When more than 95% of the node's main filesystem's inodes are in use.

In the example, by changing the default value of only one parameter for
evictionHard, the default values of other parameters will not be inherited and
will be set to zero. In order to provide custom values, you should provide all
the threshold values respectively.
Alternatively, you can set the MergeDefaultEvictionSettings to true in the kubelet
configuration file, if any parameter is changed then the other parameters will inherit
their default values instead of 0.

The `imagefs` is an optional filesystem that container runtimes use to store container
images and container writable layers.
