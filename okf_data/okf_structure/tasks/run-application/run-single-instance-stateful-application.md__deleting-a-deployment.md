---
id: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#deleting-a-deployment
kind: section
title: Deleting a deployment
source: tasks/run-application/run-single-instance-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
heading: Deleting a deployment
parent: okf-structure/tasks/run-application/run-single-instance-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#updating
next_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#whatsnext
word_count: 78
---

Delete the deployed objects by name:

```shell
kubectl delete deployment,svc mysql
kubectl delete pvc mysql-pv-claim
kubectl delete pv mysql-pv-volume
```

If you manually provisioned a PersistentVolume, you also need to manually
delete it, as well as release the underlying resource.
If you used a dynamic provisioner, it automatically deletes the
PersistentVolume when it sees that you deleted the PersistentVolumeClaim.
Some dynamic provisioners (such as those for EBS and PD) also release the
underlying resource upon deleting the PersistentVolume.
