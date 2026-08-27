---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-with-an-ephemeral-debug-container-ephemeral-container
kind: section
title: Debugging with an ephemeral debug container {#ephemeral-container}
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Debugging with an ephemeral debug container {#ephemeral-container}
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-with-container-exec-container-exec
next_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-using-a-copy-of-the-pod
word_count: 353
---

Ephemeral containers
are useful for interactive troubleshooting when `kubectl exec` is insufficient
because a container has crashed or a container image doesn't include debugging
utilities, such as with distroless images.

### Example debugging using ephemeral containers {#ephemeral-container-example}

You can use the `kubectl debug` command to add ephemeral containers to a
running Pod. First, create a pod for the example:

```shell
kubectl run ephemeral-demo --image=registry.k8s.io/pause:3.1 --restart=Never
```

The examples in this section use the `pause` container image because it does not
contain debugging utilities, but this method works with all container
images.

If you attempt to use `kubectl exec` to create a shell you will see an error
because there is no shell in this container image.

```shell
kubectl exec -it ephemeral-demo -- sh
```

```
OCI runtime exec failed: exec failed: container_linux.go:346: starting container process caused "exec: \"sh\": executable file not found in $PATH": unknown
```

You can instead add a debugging container using `kubectl debug`. If you
specify the `-i`/`--interactive` argument, `kubectl` will automatically attach
to the console of the Ephemeral Container.

```shell
kubectl debug -it ephemeral-demo --image=busybox:1.28 --target=ephemeral-demo
```

```
Defaulting debug container name to debugger-8xzrl.
If you don't see a command prompt, try pressing enter.
/ #
```

This command adds a new busybox container and attaches to it. The `--target`
parameter targets the process namespace of another container. It's necessary
here because `kubectl run` does not enable process namespace sharing in the pod it
creates.

The `--target` parameter must be supported by the Container Runtime. When not supported,
the Ephemeral Container may not be started, or it may be started with an
isolated process namespace so that `ps` does not reveal processes in other
containers.

You can view the state of the newly created ephemeral container using `kubectl describe`:

```shell
kubectl describe pod ephemeral-demo
```

```
...
Ephemeral Containers:
  debugger-8xzrl:
    Container ID:   docker://b888f9adfd15bd5739fefaa39e1df4dd3c617b9902082b1cfdc29c4028ffb2eb
    Image:          busybox
    Image ID:       docker-pullable://busybox@sha256:1828edd60c5efd34b2bf5dd3282ec0cc04d47b2ff9caa0b6d4f07a21d1c08084
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Wed, 12 Feb 2020 14:25:42 +0100
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:         <none>
...
```

Use `kubectl delete` to remove the Pod when you're finished:

```shell
kubectl delete pod ephemeral-demo
```
