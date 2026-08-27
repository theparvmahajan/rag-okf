---
id: okf-structure/tasks/debug/debug-application/debug-pods.md#whatsnext
kind: section
title: Whatsnext
source: tasks/debug/debug-application/debug-pods.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/
heading: Whatsnext
parent: okf-structure/tasks/debug/debug-application/debug-pods
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-pods.md#diagnosing-the-problem
next_sibling: null
word_count: 55
---

If none of the above solves your problem, follow the instructions in
Debugging Service document
to make sure that your `Service` is running, has `Endpoints`, and your `Pods` are
actually serving; you have DNS working, iptables rules installed, and kube-proxy
does not seem to be misbehaving.

You may also visit troubleshooting document for more information.
