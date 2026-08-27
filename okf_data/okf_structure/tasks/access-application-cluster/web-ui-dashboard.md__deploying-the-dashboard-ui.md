---
id: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#deploying-the-dashboard-ui
kind: section
title: Deploying the Dashboard UI
source: tasks/access-application-cluster/web-ui-dashboard.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
heading: Deploying the Dashboard UI
parent: okf-structure/tasks/access-application-cluster/web-ui-dashboard
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#introduction
next_sibling: okf-structure/tasks/access-application-cluster/web-ui-dashboard.md#accessing-the-dashboard-ui
word_count: 69
---

Kubernetes Dashboard supports only Helm-based installation currently as it is faster
and gives us better control over all dependencies required by Dashboard to run.

The Dashboard UI is not deployed by default. To deploy it, run the following command:

```shell
# Add kubernetes-dashboard repository
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
# Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```
