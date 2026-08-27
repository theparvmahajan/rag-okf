---
id: okf-structure/concepts/overview/working-with-objects/labels.md#using-labels-effectively
kind: section
title: Using labels effectively
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: Using labels effectively
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#api
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#updating-labels
word_count: 279
---

You can apply a single label to any resources, but this is not always the
best practice. There are many scenarios where multiple labels should be used to
distinguish resource sets from one another.

For instance, different applications would use different values for the `app` label, but a
multi-tier application, such as the guestbook example,
would additionally need to distinguish each tier. 

In the following examples, the `app` label is included for convenience in manual queries
and simple CLI usage. The `app.kubernetes.io/name` label follows the recommended Kubernetes
labeling conventions and is better suited for tooling and automation.

The frontend could carry the following labels:

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: frontend
```

while the Redis master and replica would have different `tier` labels, and perhaps even an
additional `role` label:

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: master
```

and

```yaml
labels:
  app: guestbook
  app.kubernetes.io/name: guestbook
  tier: backend
  role: replica
```

The labels allow for slicing and dicing the resources along any dimension specified by a label:

```shell
kubectl apply -f examples/guestbook/all-in-one/guestbook-all-in-one.yaml
kubectl get pods -Lapp -Ltier -Lrole
```

```none
NAME                           READY  STATUS    RESTARTS   AGE   APP         TIER       ROLE
guestbook-fe-4nlpb             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-ght6d             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-fe-jpy62             1/1    Running   0          1m    guestbook   frontend   <none>
guestbook-redis-master-5pg3b   1/1    Running   0          1m    guestbook   backend    master
guestbook-redis-replica-2q2yf  1/1    Running   0          1m    guestbook   backend    replica
guestbook-redis-replica-qgazl  1/1    Running   0          1m    guestbook   backend    replica
my-nginx-divi2                 1/1    Running   0          29m   nginx       <none>     <none>
my-nginx-o0ef1                 1/1    Running   0          29m   nginx       <none>     <none>
```

```shell
kubectl get pods -lapp=guestbook,role=replica
```

```none
NAME                           READY  STATUS   RESTARTS  AGE
guestbook-redis-replica-2q2yf  1/1    Running  0         3m
guestbook-redis-replica-qgazl  1/1    Running  0         3m
```
