---
id: okf-structure/tasks/administer-cluster/namespaces.md#understanding-the-motivation-for-using-namespaces
kind: section
title: Understanding the motivation for using namespaces
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Understanding the motivation for using namespaces
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#subdividing-your-cluster-using-kubernetes-namespaces
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#understanding-namespaces-and-dns
word_count: 257
---

A single cluster should be able to satisfy the needs of multiple users or groups of users
(henceforth in this document a _user community_).

Kubernetes _namespaces_ help different projects, teams, or customers to share a Kubernetes cluster.

It does this by providing the following:

1. A scope for names.
1. A mechanism to attach authorization and policy to a subsection of the cluster.

Use of multiple namespaces is optional.

Each user community wants to be able to work in isolation from other communities.
Each user community has its own:

1. resources (pods, services, replication controllers, etc.)
1. policies (who can or cannot perform actions in their community)
1. constraints (this community is allowed this much quota, etc.)

A cluster operator may create a Namespace for each unique user community.

The Namespace provides a unique scope for:

1. named resources (to avoid basic naming collisions)
1. delegated management authority to trusted users
1. ability to limit community resource consumption

Use cases include:

1. As a cluster operator, I want to support multiple user communities on a single cluster.
1. As a cluster operator, I want to delegate authority to partitions of the cluster to trusted
   users in those communities.
1. As a cluster operator, I want to limit the amount of resources each community can consume in
   order to limit the impact to other communities using the cluster.
1. As a cluster user, I want to interact with resources that are pertinent to my user community in
   isolation of what other user communities are doing on the cluster.
