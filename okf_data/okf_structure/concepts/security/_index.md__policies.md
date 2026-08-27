---
id: okf-structure/concepts/security/_index.md#policies
kind: section
title: Policies
source: concepts/security/_index.md
url: https://kubernetes.io/docs/concepts/security/
heading: Policies
parent: okf-structure/concepts/security/_index
children: []
prev_sibling: okf-structure/concepts/security/_index.md#cloud-provider-security
next_sibling: okf-structure/concepts/security/_index.md#whatsnext
word_count: 82
---

You can define security policies using Kubernetes-native mechanisms,
such as NetworkPolicy
(declarative control over network packet filtering) or
ValidatingAdmissionPolicy (declarative restrictions on what changes
someone can make using the Kubernetes API).

However, you can also rely on policy implementations from the wider
ecosystem around Kubernetes. Kubernetes provides extension mechanisms
to let those ecosystem projects implement their own policy controls
on source code review, container image approval, API access controls,
networking, and more.

For more information about policy mechanisms and Kubernetes,
read Policies.
