---
id: okf-structure/tutorials/stateful-application/cassandra.md#cleanup
kind: section
title: Cleanup
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Cleanup
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#modifying-the-cassandra-statefulset
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#cassandra-container-environment-variables
word_count: 139
---

Deleting or scaling a StatefulSet down does not delete the volumes associated with the StatefulSet.
This setting is for your safety because your data is more valuable than automatically purging all related StatefulSet resources.

Depending on the storage class and reclaim policy, deleting the *PersistentVolumeClaims* may cause the associated volumes
to also be deleted. Never assume you'll be able to access data if its volume claims are deleted.

1. Run the following commands (chained together into a single command) to delete everything in the Cassandra StatefulSet:

    ```shell
    grace=$(kubectl get pod cassandra-0 -o=jsonpath='{.spec.terminationGracePeriodSeconds}') \
      && kubectl delete statefulset -l app=cassandra \
      && echo "Sleeping ${grace} seconds" 1>&2 \
      && sleep $grace \
      && kubectl delete persistentvolumeclaim -l app=cassandra
    ```

1. Run the following command to delete the Service you set up for Cassandra:

    ```shell
    kubectl delete service -l app=cassandra
    ```
