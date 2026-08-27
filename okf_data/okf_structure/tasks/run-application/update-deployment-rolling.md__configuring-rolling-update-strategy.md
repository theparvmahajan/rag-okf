---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#configuring-rolling-update-strategy
kind: section
title: Configuring rolling update strategy
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Configuring rolling update strategy
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#pausing-and-resuming-a-rollout
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#rolling-back-to-a-previous-revision-rollback
word_count: 243
---

Deployments support two
update strategy types:

- **RollingUpdate** (default): gradually replaces old Pods with new ones.
- **Recreate**: terminates all existing Pods before creating new ones. This
  causes downtime.

For the RollingUpdate strategy, these parameters control how Kubernetes performs the update:

| Parameter | Controls | Default | Example |
|-----------|----------|---------|---------|
| `maxUnavailable` | Maximum number of Pods that can be unavailable during the update | 25% | `1` or `25%` |
| `maxSurge` | Maximum number of extra Pods that can be created during the update | 25% | `1` or `25%` |

`maxUnavailable` and `maxSurge` accept an absolute number or a percentage.
Kubernetes calculates percentages from the desired replica count, rounding down
for `maxUnavailable` and rounding up for `maxSurge`.

To configure these parameters, use `kubectl patch`:

```shell
kubectl patch deployment nginx-deployment -p \
  '{"spec":{"strategy":{"rollingUpdate":{"maxUnavailable":"25%","maxSurge":"25%"}}}}'
```

You can also set these fields in a Deployment manifest under
`.spec.strategy.rollingUpdate`. For detailed examples, see
max unavailable
and max surge
in the Deployment concepts documentation.

### Detecting a stalled rollout

If a rollout does not make progress within the time specified by
`.spec.progressDeadlineSeconds` (default: 600 seconds), Kubernetes marks the Deployment condition `Progressing` as `False`. You can check for this condition by describing the Deployment:

```shell
kubectl describe deployment nginx-deployment
```

Look for the `Progressing` condition in the `Conditions` section of the output. A stalled rollout usually indicates that new Pods are failing to start. The `Events` section of the output can help diagnose the issue.
