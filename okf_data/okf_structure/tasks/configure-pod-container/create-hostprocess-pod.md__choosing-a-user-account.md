---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#choosing-a-user-account
kind: section
title: Choosing a user account
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: Choosing a user account
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#resource-limits
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#base-image-for-hostprocess-containers
word_count: 304
---

### System accounts

By default, HostProcess containers support the ability to run as one of three supported Windows service accounts:

- **LocalSystem**
- **LocalService**
- **NetworkService**

You should select an appropriate Windows service account for each HostProcess
container, aiming to limit the degree of privileges so as to avoid accidental (or even
malicious) damage to the host. The LocalSystem service account has the highest level
of privilege of the three and should be used only if absolutely necessary. Where possible,
use the LocalService service account as it is the least privileged of the three options.

### Local accounts {#local-accounts}

If configured, HostProcess containers can also run as local user accounts which allows for node operators to give
fine-grained access to workloads.

To run HostProcess containers as a local user; A local usergroup must first be created on the node
and the name of that local usergroup must be specified in the `runAsUserName` field in the deployment.
Prior to initializing the HostProcess container, a new **ephemeral** local user account to be created and joined to the specified usergroup, from which the container is run.
This provides a number a benefits including eliminating the need to manage passwords for local user accounts.
An initial HostProcess container running as a service account can be used to
prepare the user groups for later HostProcess containers.

Running HostProcess containers as local user accounts requires containerd v1.7+

Example:

1. Create a local user group on the node (this can be done in another HostProcess container).

    ```cmd
    net localgroup hpc-localgroup /add
    ```

1. Grant access to desired resources on the node to the local usergroup.
   This can be done with tools like icacls.

1. Set `runAsUserName` to the name of the local usergroup for the pod or individual containers.

    ```yaml
    securityContext:
      windowsOptions:
        hostProcess: true
        runAsUserName: hpc-localgroup
    ```

1. Schedule the pod!
