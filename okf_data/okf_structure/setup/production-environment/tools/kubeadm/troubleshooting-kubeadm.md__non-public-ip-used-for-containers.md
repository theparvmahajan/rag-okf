---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#non-public-ip-used-for-containers
kind: section
title: Non-public IP used for containers
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: Non-public IP used for containers
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#default-nic-when-using-flannel-as-the-pod-network-in-vagrant
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#coredns-pods-have-crashloopbackoff-or-error-state
word_count: 210
---

In some situations `kubectl logs` and `kubectl run` commands may return with the
following errors in an otherwise functional cluster:

```console
Error from server: Get https://10.19.0.41:10250/containerLogs/default/mysql-ddc65b868-glc5m/mysql: dial tcp 10.19.0.41:10250: getsockopt: no route to host
```

- This may be due to Kubernetes using an IP that can not communicate with other IPs on
  the seemingly same subnet, possibly by policy of the machine provider.
- DigitalOcean assigns a public IP to `eth0` as well as a private one to be used internally
  as anchor for their floating IP feature, yet `kubelet` will pick the latter as the node's
  `InternalIP` instead of the public one.

  Use `ip addr show` to check for this scenario instead of `ifconfig` because `ifconfig` will
  not display the offending alias IP address. Alternatively an API endpoint specific to
  DigitalOcean allows to query for the anchor IP from the droplet:

  ```sh
  curl http://169.254.169.254/metadata/v1/interfaces/public/0/anchor_ipv4/address
  ```

  The workaround is to tell `kubelet` which IP to use using `--node-ip`.
  When using DigitalOcean, it can be the public one (assigned to `eth0`) or
  the private one (assigned to `eth1`) should you want to use the optional
  private network. The `kubeletExtraArgs` section of the kubeadm
  `NodeRegistrationOptions` structure
  can be used for this.

  Then restart `kubelet`:

  ```sh
  systemctl daemon-reload
  systemctl restart kubelet
  ```
