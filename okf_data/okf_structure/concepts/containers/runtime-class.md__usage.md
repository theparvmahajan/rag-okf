---
id: okf-structure/concepts/containers/runtime-class.md#usage
kind: section
title: Usage
source: concepts/containers/runtime-class.md
url: https://kubernetes.io/docs/concepts/containers/runtime-class/
heading: Usage
parent: okf-structure/concepts/containers/runtime-class
children: []
prev_sibling: okf-structure/concepts/containers/runtime-class.md#setup
next_sibling: okf-structure/concepts/containers/runtime-class.md#scheduling
word_count: 180
---

Once RuntimeClasses are configured for the cluster, you can specify a
`runtimeClassName` in the Pod spec to use it. For example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  # ...
```

This will instruct the kubelet to use the named RuntimeClass to run this pod. If the named
RuntimeClass does not exist, or the CRI cannot run the corresponding handler, the pod will enter the
`Failed` terminal phase. Look for a
corresponding event for an
error message.

If no `runtimeClassName` is specified, the default RuntimeHandler will be used, which is equivalent
to the behavior when the RuntimeClass feature is disabled.

### CRI Configuration

For more details on setting up CRI runtimes, see CRI installation.

#### containerd

Runtime handlers are configured through containerd's configuration at
`/etc/containerd/config.toml`. Valid handlers are configured under the runtimes section:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.${HANDLER_NAME}]
```

See containerd's config documentation
for more details:

#### cri o

Runtime handlers are configured through CRI-O's configuration at `/etc/crio/crio.conf`. Valid
handlers are configured under the
crio.runtime table:

```
[crio.runtime.runtimes.${HANDLER_NAME}]
  runtime_path = "${PATH_TO_BINARY}"
```

See CRI-O's config documentation for more details.
