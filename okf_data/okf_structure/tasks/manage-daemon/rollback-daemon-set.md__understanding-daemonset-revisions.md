---
id: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#understanding-daemonset-revisions
kind: section
title: Understanding DaemonSet revisions
source: tasks/manage-daemon/rollback-daemon-set.md
url: https://kubernetes.io/docs/tasks/manage-daemon/rollback-daemon-set/
heading: Understanding DaemonSet revisions
parent: okf-structure/tasks/manage-daemon/rollback-daemon-set
children: []
prev_sibling: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#performing-a-rollback-on-a-daemonset
next_sibling: okf-structure/tasks/manage-daemon/rollback-daemon-set.md#troubleshooting
word_count: 173
---

In the previous `kubectl rollout history` step, you got a list of DaemonSet
revisions. Each revision is stored in a resource named ControllerRevision.

To see what is stored in each revision, find the DaemonSet revision raw
resources:

```shell
kubectl get controllerrevision -l <daemonset-selector-key>=<daemonset-selector-value>
```

This returns a list of ControllerRevisions:

```
NAME                               CONTROLLER                     REVISION   AGE
<daemonset-name>-<revision-hash>   DaemonSet/<daemonset-name>     1          1h
<daemonset-name>-<revision-hash>   DaemonSet/<daemonset-name>     2          1h
```

Each ControllerRevision stores the annotations and template of a DaemonSet
revision.

`kubectl rollout undo` takes a specific ControllerRevision and replaces
DaemonSet template with the template stored in the ControllerRevision.
`kubectl rollout undo` is equivalent to updating DaemonSet template to a
previous revision through other commands, such as `kubectl edit` or `kubectl
apply`.

DaemonSet revisions only roll forward. That is to say, after a
rollback completes, the revision number (`.revision` field) of the
ControllerRevision being rolled back to will advance. For example, if you
have revision 1 and 2 in the system, and roll back from revision 2 to revision
1, the ControllerRevision with `.revision: 1` will become `.revision: 3`.
