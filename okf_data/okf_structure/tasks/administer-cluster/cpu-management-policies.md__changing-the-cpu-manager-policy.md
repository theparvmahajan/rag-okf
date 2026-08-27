---
id: okf-structure/tasks/administer-cluster/cpu-management-policies.md#changing-the-cpu-manager-policy
kind: section
title: Changing the CPU Manager Policy
source: tasks/administer-cluster/cpu-management-policies.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/
heading: Changing the CPU Manager Policy
parent: okf-structure/tasks/administer-cluster/cpu-management-policies
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#configuration
next_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#whatsnext
word_count: 702
---

Since the CPU manager policy can only be applied when kubelet spawns new pods, simply changing from
"none" to "static" won't apply to existing pods. So in order to properly change the CPU manager
policy on a node, perform the following steps:

1. Drain the node.
2. Stop kubelet.
3. Remove the old CPU manager state file. The path to this file is
`/var/lib/kubelet/cpu_manager_state` by default. This clears the state maintained by the
CPUManager so that the cpu-sets set up by the new policy won’t conflict with it.
4. Edit the kubelet configuration to change the CPU manager policy to the desired value.
5. Start kubelet.

Repeat this process for every node that needs its CPU manager policy changed. Skipping this
process will result in kubelet crashlooping with the following error:

```
could not restore state from checkpoint: configured policy "static" differs from state checkpoint policy "none", please drain this node and delete the CPU manager checkpoint file "/var/lib/kubelet/cpu_manager_state" before restarting Kubelet
```

if the set of online CPUs changes on the node, the node must be drained and CPU manager manually reset by deleting the
state file `cpu_manager_state` in the kubelet root directory.

### `none` policy configuration

This policy has no extra configuration items.

### `static` policy configuration

This policy manages a shared pool of CPUs that initially contains all CPUs in the
node. The amount of exclusively allocatable CPUs is equal to the total
number of CPUs in the node minus any CPU reservations by the kubelet `--kube-reserved` or
`--system-reserved` options. From 1.17, the CPU reservation list can be specified
explicitly by kubelet `--reserved-cpus` option. The explicit CPU list specified by
`--reserved-cpus` takes precedence over the CPU reservation specified by
`--kube-reserved` and `--system-reserved`. CPUs reserved by these options are taken, in
integer quantity, from the initial shared pool in ascending order by physical
core ID.  This shared pool is the set of CPUs on which any containers in
`BestEffort` and `Burstable` pods run. Containers in `Guaranteed` pods with fractional
CPU `requests` also run on CPUs in the shared pool. Only containers that are
both part of a `Guaranteed` pod and have integer CPU `requests` are assigned
exclusive CPUs.

The kubelet requires a CPU reservation greater than zero be made
using either `--kube-reserved` and/or `--system-reserved` or `--reserved-cpus` when
the static policy is enabled. This is because zero CPU reservation would allow the shared
pool to become empty.

### Static policy options {#cpu-policy-static--options}

You can toggle groups of options on and off based upon their maturity level
using the following feature gates:
* `CPUManagerPolicyBetaOptions` default enabled. Disable to hide beta-level options.
* `CPUManagerPolicyAlphaOptions` default disabled. Enable to show alpha-level options.
You will still have to enable each option using the `CPUManagerPolicyOptions` kubelet option.

The following policy options exist for the static `CPUManager` policy:
* `full-pcpus-only` (GA, visible by default) (1.33 or higher)
* `distribute-cpus-across-numa` (beta, visible by default) (1.33 or higher)
* `align-by-socket` (alpha, hidden by default) (1.25 or higher)
* `distribute-cpus-across-cores` (alpha, hidden by default) (1.31 or higher)
* `strict-cpu-reservation` (GA, visible by default) (1.35 or higher)
* `prefer-align-cpus-by-uncorecache` (GA, visible by default) (1.36 or higher)

The `full-pcpus-only` option can be enabled by adding `full-pcpus-only=true` to
the CPUManager policy options.
Likewise, the `distribute-cpus-across-numa` option can be enabled by adding
`distribute-cpus-across-numa=true` to the CPUManager policy options.
When both are set, they are "additive" in the sense that CPUs will be
distributed across NUMA nodes in chunks of full-pcpus rather than individual
cores.
The `align-by-socket` policy option can be enabled by adding `align-by-socket=true`
to the `CPUManager` policy options. It is also additive to the `full-pcpus-only`
and `distribute-cpus-across-numa` policy options.

The `distribute-cpus-across-cores` option can be enabled by adding
`distribute-cpus-across-cores=true` to the `CPUManager` policy options.
It cannot be used with `full-pcpus-only` or `distribute-cpus-across-numa` policy
options together at this moment.

The `strict-cpu-reservation` option can be enabled by adding `strict-cpu-reservation=true` to
the CPUManager policy options followed by removing the `/var/lib/kubelet/cpu_manager_state` file and restart kubelet.

The `prefer-align-cpus-by-uncorecache` option can be enabled by adding the
`prefer-align-cpus-by-uncorecache` to the `CPUManager` policy options. If 
incompatible options are used, the kubelet will fail to start with the error 
explained in the logs.

For mode detail about the behavior of the individual options you can configure, please refer to the
Node ResourceManagers documentation.
