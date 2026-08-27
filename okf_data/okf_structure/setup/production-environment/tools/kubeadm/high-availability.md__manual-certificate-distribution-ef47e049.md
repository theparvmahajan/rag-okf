---
id: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#manual-certificate-distribution-manual-certs
kind: section
title: Manual certificate distribution {#manual-certs}
source: setup/production-environment/tools/kubeadm/high-availability.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/
heading: Manual certificate distribution {#manual-certs}
parent: okf-structure/setup/production-environment/tools/kubeadm/high-availability
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/high-availability.md#common-tasks-after-bootstrapping-control-plane
next_sibling: null
word_count: 418
---

If you choose to not use `kubeadm init` with the `--upload-certs` flag this means that
you are going to have to manually copy the certificates from the primary control plane node to the
joining control plane nodes.

There are many ways to do this. The following example uses `ssh` and `scp`:

SSH is required if you want to control all nodes from a single machine.

1. Enable ssh-agent on your main device that has access to all other nodes in
   the system:

   ```shell
   eval $(ssh-agent)
   ```

1. Add your SSH identity to the session:

   ```shell
   ssh-add ~/.ssh/path_to_private_key
   ```

1. SSH between nodes to check that the connection is working correctly.

   - When you SSH to any node, add the `-A` flag. This flag allows the node that you
     have logged into via SSH to access the SSH agent on your PC. Consider alternative
     methods if you do not fully trust the security of your user session on the node.

     ```shell
     ssh -A 10.0.0.7
     ```

   - When using sudo on any node, make sure to preserve the environment so SSH
     forwarding works:

     ```shell
     sudo -E -s
     ```

1. After configuring SSH on all the nodes you should run the following script on the first
   control plane node after running `kubeadm init`. This script will copy the certificates from
   the first control plane node to the other control plane nodes:

   In the following example, replace `CONTROL_PLANE_IPS` with the IP addresses of the
   other control plane nodes.

   ```sh
   USER=ubuntu # customizable
   CONTROL_PLANE_IPS="10.0.0.7 10.0.0.8"
   for host in ${CONTROL_PLANE_IPS}; do
       scp /etc/kubernetes/pki/ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.key "${USER}"@$host:
       scp /etc/kubernetes/pki/sa.pub "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.crt "${USER}"@$host:
       scp /etc/kubernetes/pki/front-proxy-ca.key "${USER}"@$host:
       scp /etc/kubernetes/pki/etcd/ca.crt "${USER}"@$host:etcd-ca.crt
       # Skip the next line if you are using external etcd
       scp /etc/kubernetes/pki/etcd/ca.key "${USER}"@$host:etcd-ca.key
   done
   ```

   
   Copy only the certificates in the above list. kubeadm will take care of generating the rest of the certificates
   with the required SANs for the joining control-plane instances. If you copy all the certificates by mistake,
   the creation of additional nodes could fail due to a lack of required SANs.
   

1. Then on each joining control plane node you have to run the following script before running `kubeadm join`.
   This script will move the previously copied certificates from the home directory to `/etc/kubernetes/pki`:

   ```sh
   USER=ubuntu # customizable
   mkdir -p /etc/kubernetes/pki/etcd
   mv /home/${USER}/ca.crt /etc/kubernetes/pki/
   mv /home/${USER}/ca.key /etc/kubernetes/pki/
   mv /home/${USER}/sa.pub /etc/kubernetes/pki/
   mv /home/${USER}/sa.key /etc/kubernetes/pki/
   mv /home/${USER}/front-proxy-ca.crt /etc/kubernetes/pki/
   mv /home/${USER}/front-proxy-ca.key /etc/kubernetes/pki/
   mv /home/${USER}/etcd-ca.crt /etc/kubernetes/pki/etcd/ca.crt
   # Skip the next line if you are using external etcd
   mv /home/${USER}/etcd-ca.key /etc/kubernetes/pki/etcd/ca.key
   ```
