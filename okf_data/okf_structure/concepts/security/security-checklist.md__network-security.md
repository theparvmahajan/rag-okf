---
id: okf-structure/concepts/security/security-checklist.md#network-security
kind: section
title: Network security
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Network security
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#authentication-authorization
next_sibling: okf-structure/concepts/security/security-checklist.md#pod-security
word_count: 370
---

- [ ] CNI plugins in use support network policies.
- [ ] Ingress and egress network policies are applied to all workloads in the
  cluster.
- [ ] Default network policies within each namespace, selecting all pods, denying
  everything, are in place.
- [ ] If appropriate, a service mesh is used to encrypt all communications inside of the cluster.
- [ ] The Kubernetes API, kubelet API and etcd are not exposed publicly on Internet.
- [ ] Access from the workloads to the cloud metadata API is filtered.
- [ ] Use of LoadBalancer and ExternalIPs is restricted.

A number of Container Network Interface (CNI) plugins
plugins provide the functionality to
restrict network resources that pods may communicate with. This is most commonly done
through Network Policies
which provide a namespaced resource to define rules. Default network policies
that block all egress and ingress, in each namespace, selecting all pods, can be
useful to adopt an allow list approach to ensure that no workloads are missed.

Not all CNI plugins provide encryption in transit. If the chosen plugin lacks this
feature, an alternative solution could be to use a service mesh to provide that
functionality.

The etcd datastore of the control plane should have controls to limit access and
not be publicly exposed on the Internet. Furthermore, mutual TLS (mTLS) should
be used to communicate securely with it. The certificate authority for this
should be unique to etcd.

External Internet access to the Kubernetes API server should be restricted to
not expose the API publicly. Be careful, as many managed Kubernetes distributions
are publicly exposing the API server by default. You can then use a bastion host
to access the server.

The kubelet API access
should be restricted and not exposed publicly, the default authentication and
authorization settings, when no configuration file specified with the `--config`
flag, are overly permissive.

If a cloud provider is used for hosting Kubernetes, the access from pods to the cloud
metadata API `169.254.169.254` should also be restricted or blocked if not needed
because it may leak information.

For restricted LoadBalancer and ExternalIPs use, see
CVE-2020-8554: Man in the middle using LoadBalancer or ExternalIPs
and the DenyServiceExternalIPs admission controller
for further information.
