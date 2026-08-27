---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#coredns-pods-have-crashloopbackoff-or-error-state
kind: section
title: '`coredns` pods have `CrashLoopBackOff` or `Error` state'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`coredns` pods have `CrashLoopBackOff` or `Error` state'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#non-public-ip-used-for-containers
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#etcd-pods-restart-continually
word_count: 135
---

If you have nodes that are running SELinux with an older version of Docker, you might experience a scenario
where the `coredns` pods are not starting. To solve that, you can try one of the following options:

- Upgrade to a newer version of Docker.

- Disable SELinux.

- Modify the `coredns` deployment to set `allowPrivilegeEscalation` to `true`:

```bash
kubectl -n kube-system get deployment coredns -o yaml | \
  sed 's/allowPrivilegeEscalation: false/allowPrivilegeEscalation: true/g' | \
  kubectl apply -f -
```

Another cause for CoreDNS to have `CrashLoopBackOff` is when a CoreDNS Pod deployed in Kubernetes detects a loop.
A number of workarounds
are available to avoid Kubernetes trying to restart the CoreDNS Pod every time CoreDNS detects the loop and exits.

Disabling SELinux or setting `allowPrivilegeEscalation` to `true` can compromise
the security of your cluster.
