---
id: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-policy-options
kind: section
title: Topology manager policy options
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: Topology manager policy options
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-policies
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#pod-interactions-with-topology-manager-policies
word_count: 459
---

Support for the Topology Manager policy options requires `TopologyManagerPolicyOptions`
feature gate to be enabled
(it is enabled by default).

You can toggle groups of options on and off based upon their maturity level using the following feature gates:

* `TopologyManagerPolicyBetaOptions` default enabled. Enable to show beta-level options.
* `TopologyManagerPolicyAlphaOptions` default disabled. Enable to show alpha-level options.

You will still have to enable each option using the `TopologyManagerPolicyOptions` kubelet option.

### `prefer-closest-numa-nodes` {#policy-option-prefer-closest-numa-nodes}

The `prefer-closest-numa-nodes` option is GA since Kubernetes 1.32. In Kubernetes 
this policy option is visible by default provided that the `TopologyManagerPolicyOptions`
feature gate is enabled.

The Topology Manager is not aware by default of NUMA distances, and does not take them into account when making
Pod admission decisions. This limitation surfaces in multi-socket, as well as single-socket multi NUMA systems,
and can cause significant performance degradation in latency-critical execution and high-throughput applications
if the Topology Manager decides to align resources on non-adjacent NUMA nodes.

If you specify the `prefer-closest-numa-nodes` policy option, the `best-effort` and `restricted`
policies favor sets of NUMA nodes with shorter distance between them when making admission decisions.

You can enable this option by adding `prefer-closest-numa-nodes=true` to the Topology Manager policy options.

By default (without this option), the Topology Manager aligns resources on either a single NUMA node or,
in the case where more than one NUMA node is required, using the minimum number of NUMA nodes.

### `max-allowable-numa-nodes` {#policy-option-max-allowable-numa-nodes}

The `max-allowable-numa-nodes` option is GA since Kubernetes 1.35. In Kubernetes ,
this policy option is visible by default provided that the `TopologyManagerPolicyOptions`
feature gate is enabled.

The time to admit a pod is tied to the number of NUMA nodes on the physical machine.
By default, Kubernetes does not run a kubelet with the Topology Manager enabled, on any (Kubernetes) node where
more than 8 NUMA nodes are detected.

If you select the `max-allowable-numa-nodes` policy option, nodes with more than 8 NUMA nodes can
be allowed to run with the Topology Manager enabled. The Kubernetes project only has limited data on the impact
of using the Topology Manager on (Kubernetes) nodes with more than 8 NUMA nodes. Because of that
lack of data, using this policy option with Kubernetes  is **not** recommended and is
at your own risk.

You can enable this option by adding `max-allowable-numa-nodes=<integer>` to the Topology Manager policy options, where the integer value must be greater than 8. The default is 8, which preserves the existing limit.

Setting a value of `max-allowable-numa-nodes` does not (in and of itself) affect the
latency of pod admission, but binding a Pod to a (Kubernetes) node with many NUMA does have an impact.
Future, potential improvements to Kubernetes may improve Pod admission performance and the high
latency that happens as the number of NUMA nodes increases.
