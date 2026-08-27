---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#stop-generating-load-stop-load
kind: section
title: Stop generating load {#stop-load}
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Stop generating load {#stop-load}
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#increase-the-load-increase-load
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#autoscaling-on-multiple-metrics-and-custom-metrics
word_count: 134
---

To finish the example, stop sending the load.

In the terminal where you created the Pod that runs a `busybox` image, terminate
the load generation by typing `<Ctrl> + C`.

Then verify the result state (after a minute or so):

```shell
# type Ctrl+C to end the watch when you're ready
kubectl get hpa php-apache --watch
```

The output is similar to:

```
NAME         REFERENCE                     TARGET       MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   0% / 50%     1         10        1          11m
```

and the Deployment also shows that it has scaled down:

```shell
kubectl get deployment php-apache
```

```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
php-apache   1/1     1            1           27m
```

Once CPU utilization dropped to 0, the HPA automatically scaled the number of replicas back down to 1.

Autoscaling the replicas may take a few minutes.
