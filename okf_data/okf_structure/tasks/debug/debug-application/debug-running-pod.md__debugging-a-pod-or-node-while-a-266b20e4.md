---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-a-pod-or-node-while-applying-a-profile-debugging-profiles
kind: section
title: Debugging a Pod or Node while applying a profile {#debugging-profiles}
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Debugging a Pod or Node while applying a profile {#debugging-profiles}
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-via-a-shell-on-the-node-node-shell-session
next_sibling: null
word_count: 607
---

When using `kubectl debug` to debug a node via a debugging Pod, a Pod via an ephemeral container, 
or a copied Pod, you can apply a profile to them.
By applying a profile, specific properties such as securityContext
are set, allowing for adaptation to various scenarios.
There are two types of profiles, static profile and custom profile.

### Applying a Static Profile {#static-profile}

A static profile is a set of predefined properties, and you can apply them using the `--profile` flag.
The available profiles are as follows:

| Profile      | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| legacy       | A set of properties backwards compatibility with 1.22 behavior |
| general      | A reasonable set of generic properties for each debugging journey |
| baseline     | A set of properties compatible with PodSecurityStandard baseline policy |
| restricted   | A set of properties compatible with PodSecurityStandard restricted policy |
| netadmin     | A set of properties including Network Administrator privileges |
| sysadmin     | A set of properties including System Administrator (root) privileges |

If you don't specify `--profile`, the `legacy` profile is used by default, but it is planned to be deprecated in the near future.
So it is recommended to use other profiles such as `general`.

Assume that you create a Pod and debug it.
First, create a Pod named `myapp` as an example:

```shell
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

Then, debug the Pod using an ephemeral container.
If the ephemeral container needs to have privilege, you can use the `sysadmin` profile:

```shell
kubectl debug -it myapp --image=busybox:1.28 --target=myapp --profile=sysadmin
```

```
Targeting container "myapp". If you don't see processes from this container it may be because the container runtime doesn't support this feature.
Defaulting debug container name to debugger-6kg4x.
If you don't see a command prompt, try pressing enter.
/ #
```

Check the capabilities of the ephemeral container process by running the following command inside the container:

```shell
/ # grep Cap /proc/$$/status
```

```
...
CapPrm:	000001ffffffffff
CapEff:	000001ffffffffff
...
```

This means the container process is granted full capabilities as a privileged container by applying `sysadmin` profile.
See more details about capabilities.

You can also check that the ephemeral container was created as a privileged container:

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].securityContext}'
```

```
{"privileged":true}
```

Clean up the Pod when you're finished with it:

```shell
kubectl delete pod myapp
```

### Applying Custom Profile {#custom-profile}

You can define a partial container spec for debugging as a custom profile in either YAML or JSON format, 
and apply it using the `--custom` flag.

Custom profile only supports the modification of the container spec, 
but modifications to `name`, `image`, `command`, `lifecycle` and `volumeDevices` fields of the container spec 
are not allowed.
It does not support the modification of the Pod spec.

Create a Pod named myapp as an example:

```shell
kubectl run myapp --image=busybox:1.28 --restart=Never -- sleep 1d
```

Create a custom profile in YAML or JSON format.
Here, create a YAML format file named `custom-profile.yaml`:

```yaml
env:
- name: ENV_VAR_1
  value: value_1
- name: ENV_VAR_2
  value: value_2
securityContext:
  capabilities:
    add:
    - NET_ADMIN
    - SYS_TIME

```

Run this command to debug the Pod using an ephemeral container with the custom profile:

```shell
kubectl debug -it myapp --image=busybox:1.28 --target=myapp --profile=general --custom=custom-profile.yaml
```

You can check that the ephemeral container has been added to the target Pod with the custom profile applied:

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].env}'
```

```
[{"name":"ENV_VAR_1","value":"value_1"},{"name":"ENV_VAR_2","value":"value_2"}]
```

```shell
kubectl get pod myapp -o jsonpath='{.spec.ephemeralContainers[0].securityContext}'
```

```
{"capabilities":{"add":["NET_ADMIN","SYS_TIME"]}}
```

Clean up the Pod when you're finished with it:

```shell
kubectl delete pod myapp
```
