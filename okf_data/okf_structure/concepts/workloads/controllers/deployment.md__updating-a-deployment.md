---
id: okf-structure/concepts/workloads/controllers/deployment.md#updating-a-deployment
kind: section
title: Updating a Deployment
source: concepts/workloads/controllers/deployment.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
heading: Updating a Deployment
parent: okf-structure/concepts/workloads/controllers/deployment
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/deployment.md#creating-a-deployment
next_sibling: okf-structure/concepts/workloads/controllers/deployment.md#rolling-back-a-deployment
word_count: 1386
---

A Deployment's rollout is triggered if and only if the Deployment's Pod template (that is, `.spec.template`)
is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

Follow the steps given below to update your Deployment:

1. Let's update the nginx Pods to use the `nginx:1.16.1` image instead of the `nginx:1.14.2` image.

   ```shell
   kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.16.1
   ```

   or use the following command:

   ```shell
   kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
   ```
   where `deployment/nginx-deployment` indicates the Deployment,
   `nginx` indicates the Container the update will take place and
   `nginx:1.16.1` indicates the new image and its tag.

   The output is similar to:

   ```
   deployment.apps/nginx-deployment image updated
   ```

   Alternatively, you can `edit` the Deployment and change `.spec.template.spec.containers[0].image` from `nginx:1.14.2` to `nginx:1.16.1`:

   ```shell
   kubectl edit deployment/nginx-deployment
   ```

   The output is similar to:

   ```
   deployment.apps/nginx-deployment edited
   ```

2. To see the rollout status, run:

   ```shell
   kubectl rollout status deployment/nginx-deployment
   ```

   The output is similar to this:

   ```
   Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
   ```

   or

   ```
   deployment "nginx-deployment" successfully rolled out
   ```

Get more details on your updated Deployment:

* After the rollout succeeds, you can view the Deployment by running `kubectl get deployments`.
  The output is similar to this:

  ```
  NAME               READY   UP-TO-DATE   AVAILABLE   AGE
  nginx-deployment   3/3     3            3           36s
  ```

* Run `kubectl get rs` to see that the Deployment updated the Pods by creating a new ReplicaSet and scaling it
up to 3 replicas, as well as scaling down the old ReplicaSet to 0 replicas.

  ```shell
  kubectl get rs
  ```

  The output is similar to this:
  ```
  NAME                          DESIRED   CURRENT   READY   AGE
  nginx-deployment-1564180365   3         3         3       6s
  nginx-deployment-2035384211   0         0         0       36s
  ```

* Running `get pods` should now show only the new Pods:

  ```shell
  kubectl get pods
  ```

  The output is similar to this:
  ```
  NAME                                READY     STATUS    RESTARTS   AGE
  nginx-deployment-1564180365-khku8   1/1       Running   0          14s
  nginx-deployment-1564180365-nacti   1/1       Running   0          14s
  nginx-deployment-1564180365-z9gth   1/1       Running   0          14s
  ```

  Next time you want to update these Pods, you only need to update the Deployment's Pod template again.

  Deployment ensures that only a certain number of Pods are down while they are being updated. By default,
  it ensures that at least 75% of the desired number of Pods are up (25% max unavailable).

  Deployment also ensures that only a certain number of Pods are created above the desired number of Pods.
  By default, it ensures that at most 125% of the desired number of Pods are up (25% max surge).

  For example, if you look at the above Deployment closely, you will see that it first creates a new Pod,
  then deletes an old Pod, and creates another new one. It does not kill old Pods until a sufficient number of
  new Pods have come up, and does not create new Pods until a sufficient number of old Pods have been killed.
  It makes sure that at least 3 Pods are available and that at max 4 Pods in total are available. In case of
  a Deployment with 4 replicas, the number of Pods would be between 3 and 5.

* Get details of your Deployment:
  ```shell
  kubectl describe deployments
  ```
  The output is similar to this:
  ```
  Name:                   nginx-deployment
  Namespace:              default
  CreationTimestamp:      Thu, 30 Nov 2017 10:56:25 +0000
  Labels:                 app=nginx
  Annotations:            deployment.kubernetes.io/revision=2
  Selector:               app=nginx
  Replicas:               3 desired | 3 updated | 3 total | 3 available | 0 unavailable
  StrategyType:           RollingUpdate
  MinReadySeconds:        0
  RollingUpdateStrategy:  25% max unavailable, 25% max surge
  Pod Template:
    Labels:  app=nginx
     Containers:
      nginx:
        Image:        nginx:1.16.1
        Port:         80/TCP
        Environment:  <none>
        Mounts:       <none>
      Volumes:        <none>
    Conditions:
      Type           Status  Reason
      ----           ------  ------
      Available      True    MinimumReplicasAvailable
      Progressing    True    NewReplicaSetAvailable
    OldReplicaSets:  <none>
    NewReplicaSet:   nginx-deployment-1564180365 (3/3 replicas created)
    Events:
      Type    Reason             Age   From                   Message
      ----    ------             ----  ----                   -------
      Normal  ScalingReplicaSet  2m    deployment-controller  Scaled up replica set nginx-deployment-2035384211 to 3
      Normal  ScalingReplicaSet  24s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 1
      Normal  ScalingReplicaSet  22s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 2
      Normal  ScalingReplicaSet  22s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 2
      Normal  ScalingReplicaSet  19s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 1
      Normal  ScalingReplicaSet  19s   deployment-controller  Scaled up replica set nginx-deployment-1564180365 to 3
      Normal  ScalingReplicaSet  14s   deployment-controller  Scaled down replica set nginx-deployment-2035384211 to 0
  ```
  Here you see that when you first created the Deployment, it created a ReplicaSet (nginx-deployment-2035384211)
  and scaled it up to 3 replicas directly. When you updated the Deployment, it created a new ReplicaSet
  (nginx-deployment-1564180365) and scaled it up to 1 and waited for it to come up. Then it scaled down the old ReplicaSet
  to 2 and scaled up the new ReplicaSet to 2 so that at least 3 Pods were available and at most 4 Pods were created at all times.
  It then continued scaling up and down the new and the old ReplicaSet, with the same rolling update strategy.
  Finally, you'll have 3 available replicas in the new ReplicaSet, and the old ReplicaSet is scaled down to 0.

Kubernetes doesn't count terminating Pods when calculating the number of `availableReplicas`, which must be between
`replicas - maxUnavailable` and `replicas + maxSurge`. As a result, you might notice that there are more Pods than
expected during a rollout, and that the total resources consumed by the Deployment is more than `replicas + maxSurge`
until the `terminationGracePeriodSeconds` of the terminating Pods expires.

### Rollover (aka multiple updates in-flight)

Each time a new Deployment is observed by the Deployment controller, a ReplicaSet is created to bring up
the desired Pods. If the Deployment is updated, the existing ReplicaSet that controls Pods whose labels
match `.spec.selector` but whose template does not match `.spec.template` is scaled down. Eventually, the new
ReplicaSet is scaled to `.spec.replicas` and all old ReplicaSets is scaled to 0.

If you update a Deployment while an existing rollout is in progress, the Deployment creates a new ReplicaSet
as per the update and start scaling that up, and rolls over the ReplicaSet that it was scaling up previously
-- it will add it to its list of old ReplicaSets and start scaling it down.

For example, suppose you create a Deployment to create 5 replicas of `nginx:1.14.2`,
but then update the Deployment to create 5 replicas of `nginx:1.16.1`, when only 3
replicas of `nginx:1.14.2` had been created. In that case, the Deployment immediately starts
killing the 3 `nginx:1.14.2` Pods that it had created, and starts creating
`nginx:1.16.1` Pods. It does not wait for the 5 replicas of `nginx:1.14.2` to be created
before changing course.

### Label selector updates

It is generally discouraged to make label selector updates and it is suggested to plan your selectors up front.
A Deployment's label selector is **immutable** after creation;
it cannot be updated via `kubectl patch`, `kubectl edit`, `kubectl apply`, or tools like `helm upgrade`.

If you must change the selector, you have to delete the Deployment and recreate it.
By default, deleting the Deployment also deletes its running Pods, causing downtime; use
`--cascade=orphan` if you need those Pods to keep running while you recreate the Deployment
(see the implications below).
Exercise great caution and ensure you grasp the following implications:

* **Additions:** When you create a new Deployment with a narrower selector, the new Deployment **must** also have a suitable Pod template.
  If you have an existing manifest and you edit the manifest to narrow the selector, you need to edit the metadata of the Pod template inside that Deployment, adding the
  new labels
  to match, as otherwise the API server returns a validation error. This is a _non-overlapping_ change:
  the new Deployment will not "see" the old Pods (which lack the new label), causing the old
  ReplicaSet to be **orphaned** and a brand-new ReplicaSet to be created.
* **Value Updates:** Changing the existing value in a selector key (e.g., from `v1` to `v2`)
  results in the same behavior as additions (orphaning and recreation).
* **Removals:** Removing an existing key from the Deployment selector does not require any changes
  in the Pod template labels. This is an _overlapping_ change: the new, broader selector would
  match the old Pods. Existing ReplicaSets are not orphaned, and a new ReplicaSet is not created,
  but note that the removed label still exists in any existing Pods and ReplicaSets.
  You can clean that up by triggering a rollout for the Deployment.
