---
id: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-coredns
kind: section
title: Customizing CoreDNS
source: setup/production-environment/tools/kubeadm/control-plane-flags.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/control-plane-flags/
heading: Customizing CoreDNS
parent: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/control-plane-flags.md#customizing-kube-proxy
next_sibling: null
word_count: 98
---

kubeadm allows you to customize the CoreDNS Deployment with patches against the
`corednsdeployment` patch target.

Patches for other CoreDNS related API objects like the `kube-system/coredns`
ConfigMap are currently not supported.
You must manually patch any of these objects using kubectl and recreate the CoreDNS
Pods after that.

Alternatively, you can disable the kubeadm CoreDNS deployment by including the following
option in your `ClusterConfiguration`:

```yaml
dns:
  disabled: true
```

Also, by executing the following command:

```shell
kubeadm init phase addon coredns --print-manifest --config my-config.yaml`
```

you can obtain the manifest file kubeadm would create for CoreDNS on your setup.
