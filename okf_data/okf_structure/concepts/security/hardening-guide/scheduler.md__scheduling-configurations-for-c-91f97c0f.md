---
id: okf-structure/concepts/security/hardening-guide/scheduler.md#scheduling-configurations-for-custom-schedulers
kind: section
title: Scheduling configurations for custom schedulers
source: concepts/security/hardening-guide/scheduler.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/
heading: Scheduling configurations for custom schedulers
parent: okf-structure/concepts/security/hardening-guide/scheduler
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#kube-scheduler-configuration
next_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#disallow-labeling-nodes
word_count: 347
---

When using custom schedulers based on the Kubernetes scheduling code, cluster administrators need to be careful with
plugins that use the `queueSort`, `prefilter`, `filter`, or `permit` extension points.
These extension points control various stages of a scheduling process,
and the wrong configuration can impact the kube-scheduler's behavior in your cluster.

### Key considerations

- Exactly one plugin that uses the `queueSort` extension point can be enabled at a time.
  Any plugins that use `queueSort` should be scrutinized.
- Plugins that implement the `prefilter` or `filter` extension point can potentially mark all nodes as unschedulable.
  This can bring scheduling of new pods to a halt.
- Plugins that implement the `permit` extension point can prevent or delay the binding of a Pod.
  Such plugins should be thoroughly reviewed by the cluster administrator.

When using a plugin that is not one of the default plugins,
consider disabling the `queueSort`, `filter` and `permit` extension points as follows:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
  - schedulerName: my-scheduler
    plugins:
      # Disable specific plugins for different extension points
      # You can disable all plugins for an extension point using "*"
      queueSort:
        disabled:
        - name: "*"             # Disable all queueSort plugins
      # - name: "PrioritySort"  # Disable specific queueSort plugin
      filter:
        disabled:
        - name: "*"                 # Disable all filter plugins
      # - name: "NodeResourcesFit"  # Disable specific filter plugin
      permit:
        disabled:
        - name: "*"               # Disables all permit plugins
      # - name: "TaintToleration" # Disable specific permit plugin
```
This creates a scheduler profile ` my-scheduler`.
Whenever the `.spec` of a Pod does not have a value for `.spec.schedulerName`, the kube-scheduler runs for that Pod, 
using its main configuration, and default plugins.
If you define a Pod with `.spec.schedulerName` set to `my-scheduler`, the kube-scheduler runs
but with a custom configuration; in that custom configuration,
the  `queueSort`, `filter` and `permit` extension points are disabled.
If you use this KubeSchedulerConfiguration, and don't run any custom scheduler, 
and you then define a Pod with  `.spec.schedulerName` set to `nonexistent-scheduler` 
(or any other scheduler name that doesn't exist in your cluster), no events would be generated for a pod.
