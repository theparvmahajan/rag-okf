---
id: okf-structure/concepts/overview/working-with-objects/labels.md#updating-labels
kind: section
title: Updating labels
source: concepts/overview/working-with-objects/labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
heading: Updating labels
parent: okf-structure/concepts/overview/working-with-objects/labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#using-labels-effectively
next_sibling: okf-structure/concepts/overview/working-with-objects/labels.md#whatsnext
word_count: 136
---

Sometimes you may want to relabel existing pods and other resources before creating
new resources. This can be done with `kubectl label`.
For example, if you want to label all your NGINX Pods as frontend tier, run:

```shell
kubectl label pods -l app=nginx tier=fe
```

```none
pod/my-nginx-2035384211-j5fhi labeled
pod/my-nginx-2035384211-u2c7e labeled
pod/my-nginx-2035384211-u3t6x labeled
```

This first filters all pods with the label "app=nginx", and then labels them with the "tier=fe".
To see the pods you labeled, run:

```shell
kubectl get pods -l app=nginx -L tier
```

```none
NAME                        READY     STATUS    RESTARTS   AGE       TIER
my-nginx-2035384211-j5fhi   1/1       Running   0          23m       fe
my-nginx-2035384211-u2c7e   1/1       Running   0          23m       fe
my-nginx-2035384211-u3t6x   1/1       Running   0          23m       fe
```

This outputs all "app=nginx" pods, with an additional label column of pods' tier
(specified with `-L` or `--label-columns`).

For more information, please see kubectl label.
