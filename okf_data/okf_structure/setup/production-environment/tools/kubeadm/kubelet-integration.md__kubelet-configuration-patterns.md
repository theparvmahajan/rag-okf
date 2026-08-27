---
id: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#kubelet-configuration-patterns
kind: section
title: Kubelet configuration patterns
source: setup/production-environment/tools/kubeadm/kubelet-integration.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/
heading: Kubelet configuration patterns
parent: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#introduction
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/kubelet-integration.md#configure-kubelets-using-kubeadm
word_count: 408
---

The following sections describe patterns to kubelet configuration that are simplified by
using kubeadm, rather than managing the kubelet configuration for each Node manually.

### Propagating cluster-level configuration to each kubelet

You can provide the kubelet with default values to be used by `kubeadm init` and `kubeadm join`
commands. Interesting examples include using a different container runtime or setting the default subnet
used by services.

If you want your services to use the subnet `10.96.0.0/12` as the default for services, you can pass
the `--service-cidr` parameter to kubeadm:

```bash
kubeadm init --service-cidr 10.96.0.0/12
```

Virtual IPs for services are now allocated from this subnet. You also need to set the DNS address used
by the kubelet, using the `--cluster-dns` flag. This setting needs to be the same for every kubelet
on every manager and Node in the cluster. The kubelet provides a versioned, structured API object
that can configure most parameters in the kubelet and push out this configuration to each running
kubelet in the cluster. This object is called
`KubeletConfiguration`.
The `KubeletConfiguration` allows the user to specify flags such as the cluster DNS IP addresses expressed as
a list of values to a camelCased key, illustrated by the following example:

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
clusterDNS:
- 10.96.0.10
```

For more details on the `KubeletConfiguration` have a look at this section.

### Providing instance-specific configuration details

Some hosts require specific kubelet configurations due to differences in hardware, operating system,
networking, or other host-specific parameters. The following list provides a few examples.

- The path to the DNS resolution file, as specified by the `--resolv-conf` kubelet
  configuration flag, may differ among operating systems, or depending on whether you are using
  `systemd-resolved`. If this path is wrong, DNS resolution will fail on the Node whose kubelet
  is configured incorrectly.

- The Node API object `.metadata.name` is set to the machine's hostname by default,
  unless you are using a cloud provider. You can use the `--hostname-override` flag to override the
  default behavior if you need to specify a Node name different from the machine's hostname.

- Currently, the kubelet cannot automatically detect the cgroup driver used by the container runtime,
  but the value of `--cgroup-driver` must match the cgroup driver used by the container runtime to ensure
  the health of the kubelet.

- To specify the container runtime you must set its endpoint with the
`--container-runtime-endpoint=<path>` flag.

The recommended way of applying such instance-specific configuration is by using
`KubeletConfiguration` patches.
