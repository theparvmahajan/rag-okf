---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-blocks-waiting-for-control-plane-during-installation
kind: section
title: kubeadm blocks waiting for control plane during installation
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: kubeadm blocks waiting for control plane during installation
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#ebtables-or-some-similar-executable-not-found-during-installation
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubeadm-blocks-when-removing-managed-containers
word_count: 114
---

If you notice that `kubeadm init` hangs after printing out the following line:

```console
[apiclient] Created API client, waiting for the control plane to become ready
```

This may be caused by a number of problems. The most common are:

- network connection problems. Check that your machine has full network connectivity before continuing.
- the cgroup driver of the container runtime differs from that of the kubelet. To understand how to
  configure it properly, see Configuring a cgroup driver.
- control plane containers are crashlooping or hanging. You can check this by running `docker ps`
  and investigating each container by running `docker logs`. For other container runtime, see
  Debugging Kubernetes nodes with crictl.
