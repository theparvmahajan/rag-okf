---
id: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#clean-up-2
kind: section
title: Clean up
source: tutorials/configuration/configure-persistent-volume-storage.md
url: https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
heading: Clean up
parent: okf-structure/tutorials/configuration/configure-persistent-volume-storage
children: []
prev_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#mounting-the-same-persistentvolume-in-two-places
next_sibling: okf-structure/tutorials/configuration/configure-persistent-volume-storage.md#access-control
word_count: 91
---

Delete the Pod:

```shell
kubectl delete pod test
kubectl delete pvc task-pv-claim
kubectl delete pv task-pv-volume
```

If you don't already have a shell open to the Node in your cluster,
open a new shell the same way that you did earlier.

In the shell on your Node, remove the file and directory that you created:

```shell
# This assumes that your Node uses "sudo" to run commands
# as the superuser
sudo rm /mnt/data/html/index.html
sudo rm /mnt/data/nginx.conf
sudo rmdir /mnt/data
```

You can now close the shell to your Node.
