---
id: okf-structure/concepts/extend-kubernetes/_index.md#extensions
kind: section
title: Extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: Extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#configuration
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#client-extensions
word_count: 616
---

Extensions are software components that extend and deeply integrate with Kubernetes.
They adapt it to support new types and new kinds of hardware.

Many cluster administrators use a hosted or distribution instance of Kubernetes.
These clusters come with extensions pre-installed. As a result, most Kubernetes
users will not need to install extensions and even fewer users will need to author new ones.

### Extension patterns

Kubernetes is designed to be automated by writing client programs. Any
program that reads and/or writes to the Kubernetes API can provide useful
automation. *Automation* can run on the cluster or off it. By following
the guidance in this doc you can write highly available and robust automation.
Automation generally works with any Kubernetes cluster, including hosted
clusters and managed installations.

There is a specific pattern for writing client programs that work well with
Kubernetes called the controller
pattern. Controllers typically read an object's `.spec`, possibly do things, and then
update the object's `.status`.

A controller is a client of the Kubernetes API. When Kubernetes is the client and calls
out to a remote service, Kubernetes calls this a *webhook*. The remote service is called
a *webhook backend*. As with custom controllers, webhooks do add a point of failure.

Outside of Kubernetes, the term “webhook” typically refers to a mechanism for asynchronous
notifications, where the webhook call serves as a one-way notification to another system or
component. In the Kubernetes ecosystem, even synchronous HTTP callouts are often
described as “webhooks”.

In the webhook model, Kubernetes makes a network request to a remote service.
With the alternative *binary Plugin* model, Kubernetes executes a binary (program).
Binary plugins are used by the kubelet (for example, CSI storage plugins
and CNI network plugins),
and by kubectl (see Extend kubectl with plugins).

### Extension points

This diagram shows the extension points in a Kubernetes cluster and the
clients that access it.

#### Key to the figure

1. Users often interact with the Kubernetes API using `kubectl`. Plugins
   customise the behaviour of clients. There are generic extensions that can apply to different clients,
   as well as specific ways to extend `kubectl`.

1. The API server handles all requests. Several types of extension points in the API server allow
   authenticating requests, or blocking them based on their content, editing content, and handling
   deletion. These are described in the API Access Extensions section.

1. The API server serves various kinds of *resources*. *Built-in resource kinds*, such as
   `pods`, are defined by the Kubernetes project and can't be changed.
   Read API extensions to learn about extending the Kubernetes API.

1. The Kubernetes scheduler decides
   which nodes to place pods on. There are several ways to extend scheduling, which are
   described in the Scheduling extensions section.

1. Much of the behavior of Kubernetes is implemented by programs called
   controllers, that are
   clients of the API server. Controllers are often used in conjunction with custom resources.
   Read combining new APIs with automation and
   Changing built-in resources to learn more.

1. The kubelet runs on servers (nodes), and helps pods appear like virtual servers with their own IPs on
   the cluster network. Network Plugins allow for different implementations of
   pod networking.

1. You can use Device Plugins to integrate custom hardware or other special
   node-local facilities, and make these available to Pods running in your cluster. The kubelet
   includes support for working with device plugins.

   The kubelet also mounts and unmounts
   volume for pods and their containers.
   You can use Storage Plugins to add support for new kinds
   of storage and other volume types.

#### Extension point choice flowchart {#extension-flowchart}

If you are unsure where to start, this flowchart can help. Note that some solutions may involve
several types of extensions.

---
