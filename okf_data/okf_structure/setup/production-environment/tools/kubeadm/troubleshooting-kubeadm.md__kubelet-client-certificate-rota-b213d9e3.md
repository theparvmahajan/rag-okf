---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubelet-client-certificate-rotation-fails-kubelet-client-cert
kind: section
title: Kubelet client certificate rotation fails {#kubelet-client-cert}
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: Kubelet client certificate rotation fails {#kubelet-client-cert}
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#tls-certificate-errors
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#default-nic-when-using-flannel-as-the-pod-network-in-vagrant
word_count: 209
---

By default, kubeadm configures a kubelet with automatic rotation of client certificates by using the
`/var/lib/kubelet/pki/kubelet-client-current.pem` symlink specified in `/etc/kubernetes/kubelet.conf`.
If this rotation process fails you might see errors such as `x509: certificate has expired or is not yet valid`
in kube-apiserver logs. To fix the issue you must follow these steps:

1. Backup and delete `/etc/kubernetes/kubelet.conf` and `/var/lib/kubelet/pki/kubelet-client*` from the failed node.
1. From a working control plane node in the cluster that has `/etc/kubernetes/pki/ca.key` execute
   `kubeadm kubeconfig user --org system:nodes --client-name system:node:$NODE > kubelet.conf`.
   `$NODE` must be set to the name of the existing failed node in the cluster.
   Modify the resulted `kubelet.conf` manually to adjust the cluster name and server endpoint,
   or pass `kubeconfig user --config` (see Generating kubeconfig files for additional users). If your cluster does not have
   the `ca.key` you must sign the embedded certificates in the `kubelet.conf` externally.
1. Copy this resulted `kubelet.conf` to `/etc/kubernetes/kubelet.conf` on the failed node.
1. Restart the kubelet (`systemctl restart kubelet`) on the failed node and wait for
   `/var/lib/kubelet/pki/kubelet-client-current.pem` to be recreated.
1. Manually edit the `kubelet.conf` to point to the rotated kubelet client certificates, by replacing
   `client-certificate-data` and `client-key-data` with:

   ```yaml
   client-certificate: /var/lib/kubelet/pki/kubelet-client-current.pem
   client-key: /var/lib/kubelet/pki/kubelet-client-current.pem
   ```

1. Restart the kubelet.
1. Make sure the node becomes `Ready`.
