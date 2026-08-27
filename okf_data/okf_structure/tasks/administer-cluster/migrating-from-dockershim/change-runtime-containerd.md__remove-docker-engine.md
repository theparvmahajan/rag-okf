---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#remove-docker-engine
kind: section
title: Remove Docker Engine
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: Remove Docker Engine
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#verify-that-the-node-is-healthy
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#uncordon-the-node
word_count: 77
---

If the node appears healthy, remove Docker.

```shell
sudo yum remove docker-ce docker-ce-cli
```

```shell
sudo apt-get purge docker-ce docker-ce-cli
```

```shell
sudo dnf remove docker-ce docker-ce-cli
```

```shell
sudo apt-get purge docker-ce docker-ce-cli
```

The preceding commands don't remove images, containers, volumes, or customized configuration files on your host.
To delete them, follow Docker's instructions to Uninstall Docker Engine.

Docker's instructions for uninstalling Docker Engine create a risk of deleting containerd. Be careful when executing commands.
