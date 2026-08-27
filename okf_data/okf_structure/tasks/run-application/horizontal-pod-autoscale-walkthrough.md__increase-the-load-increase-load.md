---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#increase-the-load-increase-load
kind: section
title: Increase the load {#increase-load}
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: Increase the load {#increase-load}
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#create-the-horizontalpodautoscaler-create-horizontal-pod-autoscaler
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#stop-generating-load-stop-load
word_count: 248
---

Next, see how the autoscaler reacts to increased load.
To do this, you'll start a different Pod to act as a client. The container within the client Pod
runs in an infinite loop, sending queries to the php-apache service.

```shell
# Run this in a separate terminal
# so that the load generation continues and you can carry on with the rest of the steps
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```

Now run:
```shell
# type Ctrl+C to end the watch when you're ready
kubectl get hpa php-apache --watch
```

Within a minute or so, you should see the higher CPU load; for example:

```
NAME         REFERENCE                     TARGET      MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   305% / 50%  1         10        1          3m
```

and then, more replicas. For example:
```
NAME         REFERENCE                     TARGET      MINPODS   MAXPODS   REPLICAS   AGE
php-apache   Deployment/php-apache/scale   305% / 50%  1         10        7          3m
```

Here, CPU consumption has increased to 305% of the request.
As a result, the Deployment was resized to 7 replicas:

```shell
kubectl get deployment php-apache
```

You should see the replica count matching the figure from the HorizontalPodAutoscaler
```
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
php-apache   7/7      7           7           19m
```

It may take a few minutes to stabilize the number of replicas. Since the amount
of load is not controlled in any way it may happen that the final number of replicas
will differ from this example.
