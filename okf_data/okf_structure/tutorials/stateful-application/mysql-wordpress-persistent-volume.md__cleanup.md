---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#cleanup
kind: section
title: Cleanup
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Cleanup
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#apply-and-verify
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#whatsnext
word_count: 19
---

1. Run the following command to delete your Secret, Deployments, Services and PersistentVolumeClaims:

   ```shell
   kubectl delete -k ./
   ```
