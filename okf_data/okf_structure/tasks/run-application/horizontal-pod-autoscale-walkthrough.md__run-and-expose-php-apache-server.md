---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#run-and-expose-php-apache-server
kind: section
title: Run and expose php-apache server
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Run and expose php-apache server
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#prerequisites
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#create-the-horizontalpodautoscaler-create-horizontal-pod-autoscaler
word_count: 47
---

To demonstrate a HorizontalPodAutoscaler, you will first start a Deployment that runs a container using the
`hpa-example` image, and expose it as a service
using the following manifest:

To do so, run the following command:

```shell
kubectl apply -f https://k8s.io/examples/application/php-apache.yaml
```

```
deployment.apps/php-apache created
service/php-apache created
```
