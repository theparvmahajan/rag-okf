---
id: okf-structure/tasks/run-application/configure-pdb.md#check-the-status-of-the-pdb
kind: section
title: Check the status of the PDB
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Check the status of the PDB
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#create-the-pdb-object
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#unhealthy-pod-eviction-policy
word_count: 188
---

Use kubectl to check that your PDB is created.

Assuming you don't actually have pods matching `app: zookeeper` in your namespace,
then you'll see something like this:

```shell
kubectl get poddisruptionbudgets
```
```
NAME     MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
zk-pdb   2               N/A               0                     7s
```

If there are matching pods (say, 3), then you would see something like this:

```shell
kubectl get poddisruptionbudgets
```
```
NAME     MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
zk-pdb   2               N/A               1                     7s
```

The non-zero value for `ALLOWED DISRUPTIONS` means that the disruption controller has seen the pods,
counted the matching pods, and updated the status of the PDB.

You can get more information about the status of a PDB with this command:

```shell
kubectl get poddisruptionbudgets zk-pdb -o yaml
```
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  annotations:
…
  creationTimestamp: "2020-03-04T04:22:56Z"
  generation: 1
  name: zk-pdb
…
status:
  currentHealthy: 3
  desiredHealthy: 2
  disruptionsAllowed: 1
  expectedPods: 3
  observedGeneration: 1
```

### Healthiness of a Pod

The current implementation considers healthy pods, as pods that have `.status.conditions`
item with `type="Ready"` and `status="True"`.
These pods are tracked via `.status.currentHealthy` field in the PDB status.
