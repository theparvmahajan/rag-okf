---
id: okf-structure/concepts/overview/kubectl.md#what-you-can-do-with-kubectl
kind: section
title: What you can do with kubectl
source: concepts/overview/kubectl.md
url: https://kubernetes.io/docs/concepts/overview/kubectl/
heading: What you can do with kubectl
parent: okf-structure/concepts/overview/kubectl
children: []
prev_sibling: okf-structure/concepts/overview/kubectl.md#how-kubectl-works
next_sibling: okf-structure/concepts/overview/kubectl.md#declarative-vs-imperative
word_count: 119
---

The `kubectl` tool supports many operations, which fall into these broad categories:

* **Manage resources** – Create, update, and delete objects such as Pods, Deployments, and Services.
  Use `kubectl apply` for declarative management from configuration files.
* **Inspect cluster state** – List and describe objects, view events, and check resource usage.
* **Debug** – View logs from containers, execute commands inside a running container, or port-forward to a Pod.
* **Cluster operations** – Drain nodes for maintenance, cordon nodes to prevent new workloads, and manage cluster configuration.
* **Script and automate** – Format output as JSON, YAML, or custom columns using JSONPath for use in scripts and pipelines.

For syntax, command reference, and examples, see the kubectl reference documentation.
