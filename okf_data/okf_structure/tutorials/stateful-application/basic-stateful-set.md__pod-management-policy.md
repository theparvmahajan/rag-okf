---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#pod-management-policy
kind: section
title: Pod management policy
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Pod management policy
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#deleting-statefulsets
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#cleanup
word_count: 543
---

For some distributed systems, the StatefulSet ordering guarantees are
unnecessary and/or undesirable. These systems require only uniqueness and
identity.

You can specify a Pod management policy
to avoid this strict ordering; either `OrderedReady` (the default), or `Parallel`.

### OrderedReady Pod management

`OrderedReady` pod management is the default for StatefulSets. It tells the
StatefulSet controller to respect the ordering guarantees demonstrated
above.

Use this when your application requires or expects that changes, such as rolling out a new
version of your application, happen in the strict order of the ordinal (pod number) that the StatefulSet provides.
In other words, if you have Pods `app-0`, `app-1` and `app-2`, Kubernetes will update `app-0` first and check it.
Once the checks are good, Kubernetes updates `app-1` and finally `app-2`.

If you added two more Pods, Kubernetes would set up `app-3` and wait for that to become healthy before deploying
`app-4`.

Because this is the default setting, you've already practised using it.

### Parallel Pod management

The alternative, `Parallel` pod management, tells the StatefulSet controller to launch or
terminate all Pods in parallel, and not to wait for Pods to become `Running`
and `Ready` or completely terminated prior to launching or terminating another
Pod.

The `Parallel` pod management option only affects the behavior for scaling operations. Updates are not affected;
Kubernetes still rolls out changes in order. For this tutorial, the application is very simple: a webserver that
tells you its hostname (because this is a StatefulSet, the hostname for each Pod is different and predictable).

This manifest is identical to the one you downloaded above except that the `.spec.podManagementPolicy`
of the `web` StatefulSet is set to `Parallel`.

In one terminal, watch the Pods in the StatefulSet.

```shell
# Leave this watch running until the end of the section
kubectl get pod -l app=nginx --watch
```

In another terminal, reconfigure the StatefulSet for `Parallel` Pod management:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web-parallel.yaml
```
```
service/nginx updated
statefulset.apps/web updated
```

Keep the terminal open where you're running the watch. In another terminal window, scale the
StatefulSet:

```shell
kubectl scale statefulset/web --replicas=5
```
```
statefulset.apps/web scaled
```

Examine the output of the terminal where the `kubectl get` command is running. It may look something like

```
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         7s
web-3     0/1       ContainerCreating   0         7s
web-2     0/1       Pending   0         0s
web-4     0/1       Pending   0         0s
web-2     1/1       Running   0         8s
web-4     0/1       ContainerCreating   0         4s
web-3     1/1       Running   0         26s
web-4     1/1       Running   0         2s
```

The StatefulSet launched three new Pods, and it did not wait for
the first to become Running and Ready prior to launching the second and third Pods.

This approach is useful if your workload has a stateful element, or needs Pods to be able to identify each other
with predictable naming, and especially if you sometimes need to provide a lot more capacity quickly. If this
simple web service for the tutorial suddenly got an extra 1,000,000 requests per minute then you would want to run
some more Pods - but you also would not want to wait for each new Pod to launch. Starting the extra Pods in parallel
cuts the time between requesting the extra capacity and having it available for use.
