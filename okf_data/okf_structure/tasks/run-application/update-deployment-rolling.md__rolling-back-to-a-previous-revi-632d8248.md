---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#rolling-back-to-a-previous-revision-rollback
kind: section
title: Rolling back to a previous revision {#rollback}
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Rolling back to a previous revision {#rollback}
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#configuring-rolling-update-strategy
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#cleanup
word_count: 166
---

If a new version introduces issues, you can roll back to a previous revision.

### Viewing rollout history

```shell
kubectl rollout history deployment/nginx-deployment
```

The output is similar to:

```
deployment.apps/nginx-deployment
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

The `CHANGE-CAUSE` column shows the value of the `kubernetes.io/change-cause`
annotation at the time of each revision. This annotation is **not** set automatically,
but if you are using an automated solution to manage Deployments, the tool you use
may write some text into that annotation.

### Rolling back to the previous revision

```shell
kubectl rollout undo deployment/nginx-deployment
```

The output is similar to:

```
deployment.apps/nginx-deployment rolled back
```

### Rolling back to a specific revision

```shell
kubectl rollout undo deployment/nginx-deployment --to-revision=1
```

Verify the rollback completes:

```shell
kubectl rollout status deployment/nginx-deployment
```

A Deployment's revision history is stored in the ReplicaSets it controls.
By default, Kubernetes retains 10 old ReplicaSets. You can change this limit
by setting `.spec.revisionHistoryLimit` in the Deployment manifest. Setting it to `0` disables rollback entirely.
