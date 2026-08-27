---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#create-the-horizontalpodautoscaler-create-horizontal-pod-autoscaler
kind: section
title: Create the HorizontalPodAutoscaler {#create-horizontal-pod-autoscaler}
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Create the HorizontalPodAutoscaler {#create-horizontal-pod-autoscaler}
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#run-and-expose-php-apache-server
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#increase-the-load-increase-load
word_count: 265
---

Now that the server is running, create the autoscaler using `kubectl`. The
`kubectl autoscale` subcommand,
part of `kubectl`, helps you do this.

You will shortly run a command that creates a HorizontalPodAutoscaler that maintains
between 1 and 10 replicas of the Pods controlled by the php-apache Deployment that
you created in the first step of these instructions.

Roughly speaking, the HPA controller will increase and decrease
the number of replicas (by updating the Deployment) to maintain an average CPU utilization across all Pods of 50%.
The Deployment then updates the ReplicaSet - this is part of how all Deployments work in Kubernetes -
and then the ReplicaSet either adds or removes Pods based on the change to its `.spec`.

Since each pod requests 200 milli-cores by `kubectl run`, this means an average CPU usage of 100 milli-cores.
See Algorithm details for more details
on the algorithm.

Create the HorizontalPodAutoscaler:

```shell
kubectl autoscale deployment php-apache --cpu=50% --min=1 --max=10
```

```
horizontalpodautoscaler.autoscaling/php-apache autoscaled
```

You can check the current status of the newly-made HorizontalPodAutoscaler, by running:

```shell
# You can use "hpa" or "horizontalpodautoscaler"; either name works OK.
kubectl get hpa
```

The output is similar to:
```
NAME         REFERENCE                     TARGET    MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%  1         10        1          18s
```

(if you see other HorizontalPodAutoscalers with different names, that means they already existed,
and isn't usually a problem).

Please note that the current CPU consumption is 0% as there are no clients sending requests to the server
(the ``TARGET`` column shows the average across all the Pods controlled by the corresponding deployment).
