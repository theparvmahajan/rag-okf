---
id: okf-structure/concepts/workloads/controllers/statefulset.md#revision-history
kind: section
title: Revision history
source: concepts/workloads/controllers/statefulset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
heading: Revision history
parent: okf-structure/concepts/workloads/controllers/statefulset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#rolling-updates
next_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#persistentvolumeclaim-retention
word_count: 290
---

ControllerRevision is a Kubernetes API resource used by controllers, such as the StatefulSet controller, to track historical configuration changes.

StatefulSets use ControllerRevisions to maintain a revision history, enabling rollbacks and version tracking.

### How StatefulSets track changes using ControllerRevisions

When you update a StatefulSet's Pod template (`spec.template`), the StatefulSet controller:

1. Prepares a new ControllerRevision object  
2. Stores a snapshot of the Pod template and metadata  
3. Assigns an incremental revision number  

#### Key Properties

See ControllerRevision to learn more about key properties and other details. 

---

### Managing Revision History

Control retained revisions with `.spec.revisionHistoryLimit`:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: webapp
spec:
  revisionHistoryLimit: 5  # Keep last 5 revisions
  # ... other spec fields ...
```

* **Default**: 10 revisions retained if unspecified  
* **Cleanup**: Oldest revisions are garbage-collected when exceeding the limit

#### Performing Rollbacks

You can revert to a previous configuration using:

```bash
# View revision history
kubectl rollout history statefulset/webapp

# Rollback to a specific revision
kubectl rollout undo statefulset/webapp --to-revision=3
```

This will:

* Apply the Pod template from revision 3  
* Create a new ControllerRevision with an updated revision number  

#### Inspecting ControllerRevisions

To view associated ControllerRevisions:

```bash
# List all revisions for the StatefulSet
kubectl get controllerrevisions -l app.kubernetes.io/name=webapp

# View detailed configuration of a specific revision
kubectl get controllerrevision/webapp-3 -o yaml
```

#### Best Practices

##### Retention Policy

- Set `revisionHistoryLimit` between **5–10** for most workloads.  
- Increase only if **deep rollback history** is required.

##### Monitoring

* Regularly check revisions with:

  ```bash
  kubectl get controllerrevisions
  ```

- Alert on **rapid revision count growth**.

##### Avoid

* Manual edits to ControllerRevision objects.  
* Using revisions as a backup mechanism (use actual backup tools).
* Setting `revisionHistoryLimit: 0` (disables rollback capability).
