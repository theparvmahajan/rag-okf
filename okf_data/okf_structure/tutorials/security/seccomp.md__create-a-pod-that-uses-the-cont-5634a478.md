---
id: okf-structure/tutorials/security/seccomp.md#create-a-pod-that-uses-the-container-runtime-default-seccomp-profile
kind: section
title: Create a Pod that uses the container runtime default seccomp profile
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: Create a Pod that uses the container runtime default seccomp profile
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: okf-structure/tutorials/security/seccomp.md#create-a-local-kubernetes-cluster-with-kind
next_sibling: okf-structure/tutorials/security/seccomp.md#create-a-pod-with-a-seccomp-profile-for-syscall-auditing
word_count: 134
---

Most container runtimes provide a sane set of default syscalls that are allowed
or not. You can adopt these defaults for your workload by setting the seccomp
type in the security context of a pod or container to `RuntimeDefault`.

If you have the `seccompDefault` configuration
enabled, then Pods use the `RuntimeDefault` seccomp profile whenever
no other seccomp profile is specified. Otherwise, the default is `Unconfined`.

Here's a manifest for a Pod that requests the `RuntimeDefault` seccomp profile
for all its containers:

Create that Pod:
```shell
kubectl apply -f https://k8s.io/examples/pods/security/seccomp/ga/default-pod.yaml
```

```shell
kubectl get pod default-pod
```

The Pod should be showing as having started successfully:
```
NAME        READY   STATUS    RESTARTS   AGE
default-pod 1/1     Running   0          20s
```

Delete the Pod before moving to the next section:

```shell
kubectl delete pod default-pod --wait --now
```
