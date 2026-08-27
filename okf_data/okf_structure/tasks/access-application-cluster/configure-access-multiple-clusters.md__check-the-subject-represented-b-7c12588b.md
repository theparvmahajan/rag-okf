---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#check-the-subject-represented-by-the-kubeconfig
kind: section
title: Check the subject represented by the kubeconfig
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Check the subject represented by the kubeconfig
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#clean-up
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#whatsnext
word_count: 72
---

It is not always obvious what attributes (username, groups) you will get after authenticating to the cluster. 
It can be even more challenging if you are managing more than one cluster at the same time.

There is a `kubectl` subcommand to check subject attributes, such as username, for your selected Kubernetes 
client context: `kubectl auth whoami`.

Read API access to authentication information for a client
to learn about this in more detail.
