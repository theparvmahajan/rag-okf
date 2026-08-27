---
id: okf-structure/tasks/administer-cluster/kubelet-config-file.md#start-a-kubelet-process-configured-via-the-config-file
kind: section
title: Start a kubelet process configured via the config file
source: tasks/administer-cluster/kubelet-config-file.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/
heading: Start a kubelet process configured via the config file
parent: okf-structure/tasks/administer-cluster/kubelet-config-file
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#create-the-config-file
next_sibling: okf-structure/tasks/administer-cluster/kubelet-config-file.md#drop-in-directory-for-kubelet-configuration-files-kubelet-conf-d
word_count: 158
---

If you use kubeadm to initialize your cluster, use the kubelet-config while creating your cluster with `kubeadm init`.
See configuring kubelet using kubeadm for details.

Start the kubelet with the `--config` flag set to the path of the kubelet's config file.
The kubelet will then load its config from this file.

Note that command line flags which target the same value as a config file will override that value.
This helps ensure backwards compatibility with the command-line API.

Note that relative file paths in the kubelet config file are resolved relative to the
location of the kubelet config file, whereas relative paths in command line flags are resolved
relative to the kubelet's current working directory.

Note that some default values differ between command-line flags and the kubelet config file.
If `--config` is provided and the values are not specified via the command line, the
defaults for the `KubeletConfiguration` version apply.
In the above example, this version is `kubelet.config.k8s.io/v1beta1`.
