---
id: okf-structure/concepts/cluster-administration/node-autoscaling.md#autoscalers-autoscalers
kind: section
title: Autoscalers {#autoscalers}
source: concepts/cluster-administration/node-autoscaling.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
heading: Autoscalers {#autoscalers}
parent: okf-structure/concepts/cluster-administration/node-autoscaling
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#node-consolidation-consolidation
next_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#combine-workload-and-node-autoscaling
word_count: 534
---

The functionalities described in previous sections are provided by Node _autoscalers_. In addition
to the Kubernetes API, autoscalers also need to interact with cloud provider APIs to provision and
consolidate Nodes. This means that they need to be explicitly integrated with each supported cloud
provider. The performance and feature set of a given autoscaler can differ between cloud provider
integrations.

graph TD
    na[Node autoscaler]
    k8s[Kubernetes]
    cp[Cloud Provider]

    k8s --> |get Pods/Nodes|na
    na --> |drain Nodes|k8s
    na --> |create/remove resources backing Nodes|cp
    cp --> |get resources backing Nodes|na

    classDef white_on_blue fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef blue_on_white fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class na blue_on_white;
    class k8s,cp white_on_blue;

### Autoscaler implementations

Cluster Autoscaler
and Karpenter are the two Node autoscalers currently
sponsored by SIG Autoscaling.

From the perspective of a cluster user, both autoscalers should provide a similar Node autoscaling
experience. Both will provision new Nodes for unschedulable Pods, and both will consolidate the
Nodes that are no longer optimally utilized.

Different autoscalers may also provide features outside the Node autoscaling scope described on this
page, and those additional features may differ between them.

Consult the sections below, and the linked documentation for the individual autoscalers to decide
which autoscaler fits your use case better.

#### Cluster Autoscaler

Cluster Autoscaler adds or removes Nodes to pre-configured _Node groups_. Node groups generally map
to some sort of cloud provider resource group (most commonly a Virtual Machine group). A single
instance of Cluster Autoscaler can simultaneously manage multiple Node groups. When provisioning,
Cluster Autoscaler will add Nodes to the group that best fits the requests of pending Pods. When
consolidating, Cluster Autoscaler always selects specific Nodes to remove, as opposed to just
resizing the underlying cloud provider resource group.

Additional context:

* Documentation overview
* Cloud provider integrations
* Cluster Autoscaler FAQ
* Contact

#### Karpenter

Karpenter auto-provisions Nodes based on NodePool
configurations provided by the cluster operator. Karpenter handles all aspects of node lifecycle,
not just autoscaling. This includes automatically refreshing Nodes once they reach a certain
lifetime, and auto-upgrading Nodes when new worker Node images are released. It works directly with
individual cloud provider resources (most commonly individual Virtual Machines), and doesn't rely on
cloud provider resource groups.

Additional context:

* Documentation
* Cloud provider integrations
* Karpenter FAQ
* Contact

#### Implementation comparison

Main differences between Cluster Autoscaler and Karpenter:

* Cluster Autoscaler provides features related to just Node autoscaling. Karpenter has a wider
  scope, and also provides features intended for managing Node lifecycle altogether (for example,
  utilizing disruption to auto-recreate Nodes once they reach a certain lifetime, or auto-upgrade
  them to new versions).
* Cluster Autoscaler doesn't support auto-provisioning, the Node groups it can provision from have
  to be pre-configured. Karpenter supports auto-provisioning, so the user only has to configure a
  set of constraints for the provisioned Nodes, instead of fully configuring homogeneous groups.
* Cluster Autoscaler provides cloud provider integrations directly, which means that they're a part
  of the Kubernetes project. For Karpenter, the Kubernetes project publishes Karpenter as a library
  that cloud providers can integrate with to build a Node autoscaler.
* Cluster Autoscaler provides integrations with numerous cloud providers, including smaller and less
  popular providers. There are fewer cloud providers that integrate with Karpenter, including
  AWS, and
  Azure.
