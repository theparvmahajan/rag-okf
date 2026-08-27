---
id: okf-structure/tasks/configure-pod-container/user-namespaces.md#run-a-pod-that-uses-a-user-namespace-create-pod
kind: section
title: Run a Pod that uses a user namespace {#create-pod}
source: tasks/configure-pod-container/user-namespaces.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/
heading: Run a Pod that uses a user namespace {#create-pod}
parent: okf-structure/tasks/configure-pod-container/user-namespaces
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/user-namespaces.md#prerequisites
next_sibling: null
word_count: 181
---

A user namespace for a pod is enabled setting the `hostUsers` field of `.spec`
to `false`. For example:

1. Create the pod on your cluster:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/user-namespaces-stateless.yaml
   ```

1. Exec into the pod and run `readlink /proc/self/ns/user`:

   ```shell
   kubectl exec -ti userns -- bash
   ```

Run this command:

```shell
readlink /proc/self/ns/user
```

The output is similar to:

```shell
user:[4026531837]
```

Also run:

```shell
cat /proc/self/uid_map
```

The output is similar to:
```shell
0  833617920      65536
```

Then, open a shell in the host and run the same commands.

The `readlink` command shows the user namespace the process is running in. It
should be different when it is run on the host and inside the container.

The last number of the `uid_map` file inside the container must be 65536, on the
host it must be a bigger number.

If you are running the kubelet inside a user namespace, you need to compare the
output from running the command in the pod to the output of running in the host:

```shell
readlink /proc/$pid/ns/user
```

replacing `$pid` with the kubelet PID.
