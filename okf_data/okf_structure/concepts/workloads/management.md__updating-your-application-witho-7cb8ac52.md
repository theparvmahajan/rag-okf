---
id: okf-structure/concepts/workloads/management.md#updating-your-application-without-an-outage
kind: section
title: Updating your application without an outage
source: concepts/workloads/management.md
url: https://kubernetes.io/docs/concepts/workloads/management/
heading: Updating your application without an outage
parent: okf-structure/concepts/workloads/management
children: []
prev_sibling: okf-structure/concepts/workloads/management.md#bulk-operations-in-kubectl
next_sibling: okf-structure/concepts/workloads/management.md#canary-deployments
word_count: 334
---

At some point, you'll eventually need to update your deployed application, typically by specifying
a new image or image tag. `kubectl` supports several update operations, each of which is applicable
to different scenarios.

You can run multiple copies of your app, and use a _rollout_ to gradually shift the traffic to
new healthy Pods. Eventually, all the running Pods would have the new software.

This section of the page guides you through how to create and update applications with Deployments.

Let's say you were running version 1.14.2 of nginx:

```shell
kubectl create deployment my-nginx --image=nginx:1.14.2
```

```none
deployment.apps/my-nginx created
```

Ensure that there is 1 replica:

```shell
kubectl scale --replicas 1 deployments/my-nginx --subresource='scale' --type='merge' -p '{"spec":{"replicas": 1}}'
```

```none
deployment.apps/my-nginx scaled
```

and allow Kubernetes to add more temporary replicas during a rollout, by setting a _surge maximum_ of
100%:

```shell
kubectl patch --type='merge' -p '{"spec":{"strategy":{"rollingUpdate":{"maxSurge": "100%" }}}}'
```

```none
deployment.apps/my-nginx patched
```

To update to version 1.16.1, change `.spec.template.spec.containers[0].image` from `nginx:1.14.2`
to `nginx:1.16.1` using `kubectl edit`:

```shell
kubectl edit deployment/my-nginx
# Change the manifest to use the newer container image, then save your changes
```

That's it! The Deployment will declaratively update the deployed nginx application progressively
behind the scene. It ensures that only a certain number of old replicas may be down while they are
being updated, and only a certain number of new replicas may be created above the desired number
of pods. To learn more details about how this happens,
visit Deployment.

You can use rollouts with DaemonSets, Deployments, or StatefulSets.

### Managing rollouts

You can use `kubectl rollout` to manage a
progressive update of an existing application.

For example:

```shell
kubectl apply -f my-deployment.yaml

# wait for rollout to finish
kubectl rollout status deployment/my-deployment --timeout 10m # 10 minute timeout
```

or

```shell
kubectl apply -f backing-stateful-component.yaml

# don't wait for rollout to finish, just check the status
kubectl rollout status statefulsets/backing-stateful-component --watch=false
```

You can also pause, resume or cancel a rollout.
Visit `kubectl rollout` to learn more.
