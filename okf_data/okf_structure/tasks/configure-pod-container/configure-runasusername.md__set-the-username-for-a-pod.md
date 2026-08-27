---
id: okf-structure/tasks/configure-pod-container/configure-runasusername.md#set-the-username-for-a-pod
kind: section
title: Set the Username for a Pod
source: tasks/configure-pod-container/configure-runasusername.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/
heading: Set the Username for a Pod
parent: okf-structure/tasks/configure-pod-container/configure-runasusername
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#set-the-username-for-a-container
word_count: 126
---

To specify the username with which to execute the Pod's container processes, include the `securityContext` field (PodSecurityContext) in the Pod specification, and within it, the `windowsOptions` (WindowsSecurityContextOptions) field containing the `runAsUserName` field.

The Windows security context options that you specify for a Pod apply to all Containers and init Containers in the Pod.

Here is a configuration file for a Windows Pod that has the `runAsUserName` field set:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/windows/run-as-username-pod.yaml
```

Verify that the Pod's Container is running:

```shell
kubectl get pod run-as-username-pod-demo
```

Get a shell to the running Container:

```shell
kubectl exec -it run-as-username-pod-demo -- powershell
```

Check that the shell is running user the correct username:

```powershell
echo $env:USERNAME
```

The output should be:

```
ContainerUser
```
