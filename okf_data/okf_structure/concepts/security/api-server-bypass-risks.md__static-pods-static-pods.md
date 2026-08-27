---
id: okf-structure/concepts/security/api-server-bypass-risks.md#static-pods-static-pods
kind: section
title: Static Pods {#static-pods}
source: concepts/security/api-server-bypass-risks.md
url: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/
heading: Static Pods {#static-pods}
parent: okf-structure/concepts/security/api-server-bypass-risks
children: []
prev_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#introduction
next_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#the-kubelet-api-kubelet-api
word_count: 282
---

The kubelet on each node loads and
directly manages any manifests that are stored in a named directory or fetched from
a specific URL as *static Pods* in
your cluster. The API server doesn't manage these static Pods. An attacker with write
access to this location could modify the configuration of static pods loaded from that
source, or could introduce new static Pods.

Static Pods are restricted from accessing other objects in the Kubernetes API. For example,
you can't configure a static Pod to mount a Secret from the cluster. However, these Pods can
take other security sensitive actions, such as using `hostPath` mounts from the underlying
node.

By default, the kubelet creates a mirror pod
so that the static Pods are visible in the Kubernetes API. However, if the attacker uses an invalid
namespace name when creating the Pod, it will not be visible in the Kubernetes API and can only
be discovered by tooling that has access to the affected host(s).

If a static Pod fails admission control, the kubelet won't register the Pod with the
API server. However, the Pod still runs on the node. For more information, refer to
kubeadm issue #1541.

### Mitigations {#static-pods-mitigations}

- Only enable the kubelet static Pod manifest functionality
  if required by the node.
- If a node uses the static Pod functionality, restrict filesystem access to the static Pod manifest directory
  or URL to users who need the access.
- Restrict access to kubelet configuration parameters and files to prevent an attacker setting
  a static Pod path or URL.
- Regularly audit and centrally report all access to directories or web storage locations that host
  static Pod manifests and kubelet configuration files.
