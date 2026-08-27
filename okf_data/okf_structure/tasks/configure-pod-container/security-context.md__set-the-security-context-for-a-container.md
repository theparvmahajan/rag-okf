---
id: okf-structure/tasks/configure-pod-container/security-context.md#set-the-security-context-for-a-container
kind: section
title: Set the security context for a Container
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Set the security context for a Container
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#delegating-volume-permission-and-ownership-change-to-csi-driver
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#set-capabilities-for-a-container
word_count: 205
---

To specify security settings for a Container, include the `securityContext` field
in the Container manifest. The `securityContext` field is a
SecurityContext object.
Security settings that you specify for a Container apply only to
the individual Container, and they override settings made at the Pod level when
there is overlap. Container settings do not affect the Pod's Volumes.

Here is the configuration file for a Pod that has one Container. Both the Pod
and the Container have a `securityContext` field:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/security-context-2.yaml
```

Verify that the Pod's Container is running:

```shell
kubectl get pod security-context-demo-2
```

Get a shell into the running Container:

```shell
kubectl exec -it security-context-demo-2 -- sh
```

In your shell, list the running processes:

```shell
ps aux
```

The output shows that the processes are running as user 2000. This is the value
of `runAsUser` specified for the Container. It overrides the value 1000 that is
specified for the Pod.

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
2000         1  0.0  0.0   4336   764 ?        Ss   20:36   0:00 /bin/sh -c node server.js
2000         8  0.1  0.5 772124 22604 ?        Sl   20:36   0:00 node server.js
...
```

Exit your shell:

```shell
exit
```
