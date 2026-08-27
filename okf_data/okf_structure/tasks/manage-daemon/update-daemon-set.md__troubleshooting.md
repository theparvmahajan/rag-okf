---
id: okf-structure/tasks/manage-daemon/update-daemon-set.md#troubleshooting
kind: section
title: Troubleshooting
source: tasks/manage-daemon/update-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/
heading: Troubleshooting
parent: okf-structure/tasks/manage-daemon/update-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#performing-a-rolling-update
next_sibling: okf-structure/tasks/manage-daemon/update-daemon-set.md#clean-up
word_count: 210
---

### DaemonSet rolling update is stuck

Sometimes, a DaemonSet rolling update may be stuck. Here are some possible
causes:

#### Some nodes run out of resources

The rollout is stuck because new DaemonSet pods can't be scheduled on at least one
node. This is possible when the node is
running out of resources.

When this happens, find the nodes that don't have the DaemonSet pods scheduled on
by comparing the output of `kubectl get nodes` and the output of:

```shell
kubectl get pods -l name=fluentd-elasticsearch -o wide -n kube-system
```

Once you've found those nodes, delete some non-DaemonSet pods from the node to
make room for new DaemonSet pods.

This will cause service disruption when deleted pods are not controlled by any controllers or pods are not
replicated. This does not respect PodDisruptionBudget
either.

#### Broken rollout

If the recent DaemonSet template update is broken, for example, the container is
crash looping, or the container image doesn't exist (often due to a typo),
DaemonSet rollout won't progress.

To fix this, update the DaemonSet template again. New rollout won't be
blocked by previous unhealthy rollouts.

#### Clock skew

If `.spec.minReadySeconds` is specified in the DaemonSet, clock skew between
master and nodes will make DaemonSet unable to detect the right rollout
progress.
