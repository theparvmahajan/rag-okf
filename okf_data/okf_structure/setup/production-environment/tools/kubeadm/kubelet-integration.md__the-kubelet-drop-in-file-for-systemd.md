---
id: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#the-kubelet-drop-in-file-for-systemd
kind: section
title: The kubelet drop-in file for systemd
source: setup/production-environment/tools/kubeadm/kubelet-integration.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/
heading: The kubelet drop-in file for systemd
parent: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#configure-kubelets-using-kubeadm
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#kubernetes-binaries-and-package-contents
word_count: 309
---

`kubeadm` ships with configuration for how systemd should run the kubelet.
Note that the kubeadm CLI command never touches this drop-in file.

This configuration file installed by the `kubeadm`
package is written to
`/usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf` and is used by systemd.
It augments the basic
`kubelet.service`.

If you want to override that further, you can make a directory `/etc/systemd/system/kubelet.service.d/`
(not `/usr/lib/systemd/system/kubelet.service.d/`) and put your own customizations into a file there.
For example, you might add a new local file `/etc/systemd/system/kubelet.service.d/local-overrides.conf`
to override the unit settings configured by `kubeadm`.

Here is what you are likely to find in `/usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf`:

The contents below are just an example. If you don't want to use a package manager
follow the guide outlined in the (Without a package manager)
section.

```none
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
# This is a file that "kubeadm init" and "kubeadm join" generate at runtime, populating
# the KUBELET_KUBEADM_ARGS variable dynamically
EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
# This is a file that the user can use for overrides of the kubelet args as a last resort. Preferably,
# the user should use the .NodeRegistration.KubeletExtraArgs object in the configuration files instead.
# KUBELET_EXTRA_ARGS should be sourced from this file.
EnvironmentFile=-/etc/default/kubelet
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
```

This file specifies the default locations for all of the files managed by kubeadm for the kubelet.

- The KubeConfig file to use for the TLS Bootstrap is `/etc/kubernetes/bootstrap-kubelet.conf`,
  but it is only used if `/etc/kubernetes/kubelet.conf` does not exist.
- The KubeConfig file with the unique kubelet identity is `/etc/kubernetes/kubelet.conf`.
- The file containing the kubelet's ComponentConfig is `/var/lib/kubelet/config.yaml`.
- The dynamic environment file that contains `KUBELET_KUBEADM_ARGS` is sourced from `/var/lib/kubelet/kubeadm-flags.env`.
- The file that can contain user-specified flag overrides with `KUBELET_EXTRA_ARGS` is sourced from
  `/etc/default/kubelet` (for DEBs), or `/etc/sysconfig/kubelet` (for RPMs). `KUBELET_EXTRA_ARGS`
  is last in the flag chain and has the highest priority in the event of conflicting settings.
