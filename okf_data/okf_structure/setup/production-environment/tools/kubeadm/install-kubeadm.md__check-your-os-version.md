---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-your-os-version
kind: section
title: Check your OS version
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Check your OS version
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#prerequisites
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#verify-the-mac-address-and-productuuid-are-unique-for-every-node-verify-mac-address
word_count: 161
---

* The kubeadm project supports LTS kernels. See List of LTS kernels.
* You can get the kernel version using the command `uname -r`

For more information, see Linux Kernel Requirements.

* The kubeadm project supports recent kernel versions. For a list of recent kernels, see Windows Server Release Information.
* You can get the kernel version (also called the OS version) using the command `systeminfo`

For more information, see Windows OS version compatibility.

A Kubernetes cluster created by kubeadm depends on software that use kernel features.
This software includes, but is not limited to the
container runtime,
the kubelet, and a Container Network Interface plugin.

To help you avoid unexpected errors as a result of an unsupported kernel version, kubeadm runs the `SystemVerification`
pre-flight check. This check fails if the kernel version is not supported.

You may choose to skip the check, if you know that your kernel
provides the required features, even though kubeadm does not support its version.
