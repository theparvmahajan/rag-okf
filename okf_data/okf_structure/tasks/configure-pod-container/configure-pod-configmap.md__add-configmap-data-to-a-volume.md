---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#add-configmap-data-to-a-volume
kind: section
title: Add ConfigMap data to a Volume
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Add ConfigMap data to a Volume
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#use-configmap-defined-environment-variables-in-pod-commands
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#understanding-configmaps-and-pods
word_count: 513
---

As explained in Create ConfigMaps from files, when you create
a ConfigMap using `--from-file`, the filename becomes a key stored in the `data` section of
the ConfigMap. The file contents become the key's value.

The examples in this section refer to a ConfigMap named `special-config`:

Create the ConfigMap:

```shell
kubectl create -f https://kubernetes.io/examples/configmap/configmap-multikeys.yaml
```

### Populate a Volume with data stored in a ConfigMap

Add the ConfigMap name under the `volumes` section of the Pod specification.
This adds the ConfigMap data to the directory specified as `volumeMounts.mountPath` (in this
case, `/etc/config`). The `command` section lists directory files with names that match the
keys in ConfigMap.

Create the Pod:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-volume.yaml
```

When the pod runs, the command `ls /etc/config/` produces the output below:

```
SPECIAL_LEVEL
SPECIAL_TYPE
```

Text data is exposed as files using the UTF-8 character encoding. To use some other
character encoding, use `binaryData`
(see ConfigMap object for more details).

If there are any files in the `/etc/config` directory of that container image, the volume
mount will make those files from the image inaccessible.

Once you're happy to move on, delete that Pod:
```shell
kubectl delete pod dapi-test-pod --now
```

### Add ConfigMap data to a specific path in the Volume

Use the `path` field to specify the desired file path for specific ConfigMap items.
In this case, the `SPECIAL_LEVEL` item will be mounted in the `config-volume` volume at `/etc/config/keys`.

Create the Pod:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-volume-specific-key.yaml
```

When the pod runs, the command `cat /etc/config/keys` produces the output below:

```
very
```

Like before, all previous files in the `/etc/config/` directory will be deleted.

Delete that Pod:
```shell
kubectl delete pod dapi-test-pod --now
```

### Project keys to specific paths and file permissions

You can project keys to specific paths. Refer to the corresponding section in the Secrets guide for the syntax.  
You can set POSIX permissions for keys. Refer to the corresponding section in the Secrets guide for the syntax.

### Optional references

A ConfigMap reference may be marked _optional_. If the ConfigMap is non-existent, the mounted
volume will be empty. If the ConfigMap exists, but the referenced key is non-existent, the path
will be absent beneath the mount point. See Optional ConfigMaps for more
details.

### Mounted ConfigMaps are updated automatically

When a mounted ConfigMap is updated, the projected content is eventually updated too.
This applies in the case where an optionally referenced ConfigMap comes into
existence after a pod has started.

Kubelet checks whether the mounted ConfigMap is fresh on every periodic sync. However,
it uses its local TTL-based cache for getting the current value of the ConfigMap. As a
result, the total delay from the moment when the ConfigMap is updated to the moment
when new keys are projected to the pod can be as long as kubelet sync period (1
minute by default) + TTL of ConfigMaps cache (1 minute by default) in kubelet. You
can trigger an immediate refresh by updating one of the pod's annotations.

A container using a ConfigMap as a subPath
volume will not receive ConfigMap updates.
