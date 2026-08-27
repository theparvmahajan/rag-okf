---
id: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#introduction
kind: section
title: Tools for Monitoring Resources
source: tasks/debug/debug-cluster/resource-usage-monitoring.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/
heading: null
parent: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-cluster/resource-usage-monitoring.md#resource-metrics-pipeline
word_count: 104
---

To scale an application and provide a reliable service, you need to
understand how the application behaves when it is deployed. You can examine
application performance in a Kubernetes cluster by examining the containers,
pods,
services, and
the characteristics of the overall cluster. Kubernetes provides detailed
information about an application's resource usage at each of these levels.
This information allows you to evaluate your application's performance and
where bottlenecks can be removed to improve overall performance. 

In Kubernetes, application monitoring does not depend on a single monitoring solution.
On new clusters, you can use resource metrics or
full metrics pipelines to collect monitoring statistics.
