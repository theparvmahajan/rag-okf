---
id: okf-structure/concepts/security/security-checklist.md#pod-placement
kind: section
title: Pod placement
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Pod placement
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#logs-and-auditing
next_sibling: okf-structure/concepts/security/security-checklist.md#secrets
word_count: 220
---

- [ ] Pod placement is done in accordance with the tiers of sensitivity of the
  application.
- [ ] Sensitive applications are running isolated on nodes or with specific
  sandboxed runtimes.

Pods that are on different tiers of sensitivity, for example, an application pod
and the Kubernetes API server, should be deployed onto separate nodes. The
purpose of node isolation is to prevent an application container breakout to
directly providing access to applications with higher level of sensitivity to easily
pivot within the cluster. This separation should be enforced to prevent pods
accidentally being deployed onto the same node. This could be enforced with the
following features:

Node Selectors
: Key-value pairs, as part of the pod specification, that specify which nodes to
deploy onto. These can be enforced at the namespace and cluster level with the
PodNodeSelector
admission controller.

PodTolerationRestriction
: An admission controller that allows administrators to restrict permitted
tolerations within a
namespace. Pods within a namespace may only utilize the tolerations specified on
the namespace object annotation keys that provide a set of default and allowed
tolerations.

RuntimeClass
: RuntimeClass is a feature for selecting the container runtime configuration.
The container runtime configuration is used to run a Pod's containers and can
provide more or less isolation from the host at the cost of performance
overhead.
