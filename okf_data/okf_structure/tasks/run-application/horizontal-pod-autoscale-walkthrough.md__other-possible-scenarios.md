---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#other-possible-scenarios
kind: section
title: Other possible scenarios
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Other possible scenarios
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#quantities
next_sibling: null
word_count: 45
---

### Creating the autoscaler declaratively

Instead of using `kubectl autoscale` command to create a HorizontalPodAutoscaler imperatively we
can use the following manifest to create it declaratively:

Then, create the autoscaler by executing the following command:

```shell
kubectl create -f https://k8s.io/examples/application/hpa/php-apache.yaml
```

```
horizontalpodautoscaler.autoscaling/php-apache created
```
