---
id: okf-structure/tasks/configure-pod-container/configure-runasusername.md#set-the-username-for-a-container
kind: section
title: Set the Username for a Container
source: tasks/configure-pod-container/configure-runasusername.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/
heading: Set the Username for a Container
parent: okf-structure/tasks/configure-pod-container/configure-runasusername
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#set-the-username-for-a-pod
next_sibling: okf-structure/tasks/configure-pod-container/configure-runasusername.md#windows-username-limitations
word_count: 149
---

To specify the username with which to execute a Container's processes, include the `securityContext` field (SecurityContext) in the Container manifest, and within it, the `windowsOptions` (WindowsSecurityContextOptions) field containing the `runAsUserName` field.

The Windows security context options that you specify for a Container apply only to that individual Container, and they override the settings made at the Pod level.

Here is the configuration file for a Pod that has one Container, and the `runAsUserName` field is set at the Pod level and the Container level:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/windows/run-as-username-container.yaml
```

Verify that the Pod's Container is running:

```shell
kubectl get pod run-as-username-container-demo
```

Get a shell to the running Container:

```shell
kubectl exec -it run-as-username-container-demo -- powershell
```

Check that the shell is running user the correct username (the one set at the Container level):

```powershell
echo $env:USERNAME
```

The output should be:

```
ContainerAdministrator
```
