---
id: okf-structure/tutorials/stateful-application/zookeeper.md#cleanup
kind: section
title: Cleanup
source: tutorials/stateful-application/zookeeper.md
url: https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/
heading: Cleanup
parent: okf-structure/tutorials/stateful-application/zookeeper
children: []
prev_sibling: okf-structure/tutorials/stateful-application/zookeeper.md#surviving-maintenance
next_sibling: null
word_count: 47
---

- Use `kubectl uncordon` to uncordon all the nodes in your cluster.
- You must delete the persistent storage media for the PersistentVolumes used in this tutorial.
  Follow the necessary steps, based on your environment, storage configuration,
  and provisioning method, to ensure that all storage is reclaimed.
