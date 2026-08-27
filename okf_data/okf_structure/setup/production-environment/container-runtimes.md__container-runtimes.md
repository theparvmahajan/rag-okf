---
id: okf-structure/setup/production-environment/container-runtimes.md#container-runtimes
kind: section
title: Container runtimes
source: setup/production-environment/container-runtimes.md
url: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
heading: Container runtimes
parent: okf-structure/setup/production-environment/container-runtimes
children: []
prev_sibling: okf-structure/setup/production-environment/container-runtimes.md#cri-version-support-cri-versions
next_sibling: okf-structure/setup/production-environment/container-runtimes.md#whatsnext
word_count: 690
---

### containerd

This section outlines the necessary steps to use containerd as CRI runtime.

To install containerd on your system, follow the instructions on
getting started with containerd.
Return to this step once you've created a valid `config.toml` configuration file.

You can find this file under the path `/etc/containerd/config.toml`.

You can find this file under the path `C:\Program Files\containerd\config.toml`.

On Linux the default CRI socket for containerd is `/run/containerd/containerd.sock`.
On Windows the default CRI endpoint is `npipe://./pipe/containerd-containerd`.

#### Configuring the `systemd` cgroup driver {#containerd-systemd}

To use the `systemd` cgroup driver in `/etc/containerd/config.toml` with `runc`,
set the following config based on your Containerd version

Containerd versions 1.x:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  ...
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true
```

Containerd versions 2.x:

```
[plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc]
  ...
  [plugins.'io.containerd.cri.v1.runtime'.containerd.runtimes.runc.options]
    SystemdCgroup = true
```

The `systemd` cgroup driver is recommended if you use cgroup v2.

If you installed containerd from a package (for example, RPM or `.deb`), you may find
that the CRI integration plugin is disabled by default.

You need CRI support enabled to use containerd with Kubernetes. Make sure that `cri`
is not included in the`disabled_plugins` list within `/etc/containerd/config.toml`;
if you made changes to that file, also restart `containerd`.

If you experience container crash loops after the initial cluster installation or after
installing a CNI, the containerd configuration provided with the package might contain
incompatible configuration parameters. Consider resetting the containerd configuration
with `containerd config default > /etc/containerd/config.toml` as specified in
getting-started.md
and then set the configuration parameters specified above accordingly.

If you apply this change, make sure to restart containerd:

```shell
sudo systemctl restart containerd
```

When using kubeadm, manually configure the
cgroup driver for kubelet.

In Kubernetes v1.28, you can enable automatic detection of the
cgroup driver as an alpha feature. See systemd cgroup driver
for more details.

#### Overriding the sandbox (pause) image {#override-pause-image-containerd}

In your containerd config you can overwrite the
sandbox image by setting the following config:

```toml
[plugins."io.containerd.grpc.v1.cri"]
  sandbox_image = "registry.k8s.io/pause:3.10"
```

You might need to restart `containerd` as well once you've updated the config file: `systemctl restart containerd`.

### CRI-O

This section contains the necessary steps to install CRI-O as a container runtime.

To install CRI-O, follow CRI-O Install Instructions.

#### cgroup driver

CRI-O uses the systemd cgroup driver per default, which is likely to work fine
for you. To switch to the `cgroupfs` cgroup driver, either edit
`/etc/crio/crio.conf` or place a drop-in configuration in
`/etc/crio/crio.conf.d/02-cgroup-manager.conf`, for example:

```toml
[crio.runtime]
conmon_cgroup = "pod"
cgroup_manager = "cgroupfs"
```

You should also note the changed `conmon_cgroup`, which has to be set to the value
`pod` when using CRI-O with `cgroupfs`. It is generally necessary to keep the
cgroup driver configuration of the kubelet (usually done via kubeadm) and CRI-O
in sync.

In Kubernetes v1.28, you can enable automatic detection of the
cgroup driver as an alpha feature. See systemd cgroup driver
for more details.

For CRI-O, the CRI socket is `/var/run/crio/crio.sock` by default.

#### Overriding the sandbox (pause) image {#override-pause-image-cri-o}

In your CRI-O config you can set the following
config value:

```toml
[crio.image]
pause_image="registry.k8s.io/pause:3.10"
```

This config option supports live configuration reload to apply this change: `systemctl reload crio` or by sending
`SIGHUP` to the `crio` process.

### Docker Engine {#docker}

These instructions assume that you are using the
`cri-dockerd` adapter to integrate
Docker Engine with Kubernetes.

1. On each of your nodes, install Docker for your Linux distribution as per
  Install Docker Engine.

2. Install `cri-dockerd`, following the directions in the install section of the documentation.

For `cri-dockerd`, the CRI socket is `/run/cri-dockerd.sock` by default.

### Mirantis Container Runtime {#mcr}

Mirantis Container Runtime (MCR) is a commercially
available container runtime that was formerly known as Docker Enterprise Edition.

You can use Mirantis Container Runtime with Kubernetes using the open source
`cri-dockerd` component, included with MCR.

To learn more about how to install Mirantis Container Runtime,
visit MCR Deployment Guide.

Check the systemd unit named `cri-docker.socket` to find out the path to the CRI
socket.

#### Overriding the sandbox (pause) image {#override-pause-image-cri-dockerd-mcr}

The `cri-dockerd` adapter accepts a command line argument for
specifying which container image to use as the Pod infrastructure container (“pause image”).
The command line argument to use is `--pod-infra-container-image`.
