---
id: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#performing-a-rollback-on-a-daemonset
kind: section
title: Performing a rollback on a DaemonSet
source: tasks/manage-daemon/rollback-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/rollback-daemon-set/
heading: Performing a rollback on a DaemonSet
parent: okf-structure/tasks/manage-daemon/rollback-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#prerequisites
next_sibling: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#understanding-daemonset-revisions
word_count: 253
---

### Step 1: Find the DaemonSet revision you want to roll back to

You can skip this step if you only want to roll back to the last revision.

List all revisions of a DaemonSet:

```shell
kubectl rollout history daemonset <daemonset-name>
```

This returns a list of DaemonSet revisions:

```
daemonsets "<daemonset-name>"
REVISION        CHANGE-CAUSE
1               ...
2               ...
...
```

* Change cause is copied from DaemonSet annotation `kubernetes.io/change-cause`
  to its revisions upon creation. You may specify `--record=true` in `kubectl`
  to record the command executed in the change cause annotation.

To see the details of a specific revision:

```shell
kubectl rollout history daemonset <daemonset-name> --revision=1
```

This returns the details of that revision:

```
daemonsets "<daemonset-name>" with revision #1
Pod Template:
Labels:       foo=bar
Containers:
app:
 Image:        ...
 Port:         ...
 Environment:  ...
 Mounts:       ...
Volumes:      ...
```

### Step 2: Roll back to a specific revision

```shell
# Specify the revision number you get from Step 1 in --to-revision
kubectl rollout undo daemonset <daemonset-name> --to-revision=<revision>
```

If it succeeds, the command returns:

```
daemonset "<daemonset-name>" rolled back
```

If `--to-revision` flag is not specified, kubectl picks the most recent revision.

### Step 3: Watch the progress of the DaemonSet rollback

`kubectl rollout undo daemonset` tells the server to start rolling back the
DaemonSet. The real rollback is done asynchronously inside the cluster
control plane.

To watch the progress of the rollback:

```shell
kubectl rollout status ds/<daemonset-name>
```

When the rollback is complete, the output is similar to:

```
daemonset "<daemonset-name>" successfully rolled out
```
