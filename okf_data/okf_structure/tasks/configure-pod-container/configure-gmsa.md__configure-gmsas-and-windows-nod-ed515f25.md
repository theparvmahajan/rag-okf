---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsas-and-windows-nodes-in-active-directory
kind: section
title: Configure GMSAs and Windows nodes in Active Directory
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Configure GMSAs and Windows nodes in Active Directory
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#create-gmsa-credential-spec-resources
word_count: 61
---

Before Pods in Kubernetes can be configured to use GMSAs, the desired GMSAs need
to be provisioned in Active Directory as described in the
Windows GMSA documentation.
Windows worker nodes (that are part of the Kubernetes cluster) need to be configured
in Active Directory to access the secret credentials associated with the desired GMSA as described in the
Windows GMSA documentation.
