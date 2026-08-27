---
id: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-that-causes-violation
kind: section
title: Create a Pod with a seccomp profile that causes violation
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Create a Pod with a seccomp profile that causes violation
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-for-syscall-auditing
next_sibling: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-that-only-allows-necessary-syscalls
word_count: 147
---

For demonstration, apply a profile to the Pod that does not allow for any
syscalls.

The manifest for this demonstration is:

Attempt to create the Pod in the cluster:

```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/violation-pod.yaml
```

The Pod creates, but there is an issue.
If you check the status of the Pod, you should see that it failed to start.

```shell
kubectl get pod violation-pod
```

```
NAME            READY   STATUS             RESTARTS   AGE
violation-pod   0/1     CrashLoopBackOff   1          6s
```

As seen in the previous example, the `http-echo` process requires quite a few
syscalls. Here seccomp has been instructed to error on any syscall by setting
`"defaultAction": "SCMP_ACT_ERRNO"`. This is extremely secure, but removes the
ability to do anything meaningful. What you really want is to give workloads
only the privileges they need.

Delete the Pod before moving to the next section:

```shell
kubectl delete pod violation-pod --wait --now
```
