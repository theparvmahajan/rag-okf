---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#understanding-stateful-pod-initialization
kind: section
title: Understanding stateful Pod initialization
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Understanding stateful Pod initialization
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#deploy-mysql
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#sending-client-traffic
word_count: 637
---

The StatefulSet controller starts Pods one at a time, in order by their
ordinal index.
It waits until each Pod reports being Ready before starting the next one.

In addition, the controller assigns each Pod a unique, stable name of the form
`<statefulset-name>-<ordinal-index>`, which results in Pods named `mysql-0`,
`mysql-1`, and `mysql-2`.

The Pod template in the above StatefulSet manifest takes advantage of these
properties to perform orderly startup of MySQL replication.

### Generating configuration

Before starting any of the containers in the Pod spec, the Pod first runs any
init containers
in the order defined.

The first init container, named `init-mysql`, generates special MySQL config
files based on the ordinal index.

The script determines its own ordinal index by extracting it from the end of
the Pod name, which is returned by the `hostname` command.
Then it saves the ordinal (with a numeric offset to avoid reserved values)
into a file called `server-id.cnf` in the MySQL `conf.d` directory.
This translates the unique, stable identity provided by the StatefulSet
into the domain of MySQL server IDs, which require the same properties.

The script in the `init-mysql` container also applies either `primary.cnf` or
`replica.cnf` from the ConfigMap by copying the contents into `conf.d`.
Because the example topology consists of a single primary MySQL server and any number of
replicas, the script assigns ordinal `0` to be the primary server, and everyone
else to be replicas.
Combined with the StatefulSet controller's
deployment order guarantee,
this ensures the primary MySQL server is Ready before creating replicas, so they can begin
replicating.

### Cloning existing data

In general, when a new Pod joins the set as a replica, it must assume the primary MySQL
server might already have data on it. It also must assume that the replication
logs might not go all the way back to the beginning of time.
These conservative assumptions are the key to allow a running StatefulSet
to scale up and down over time, rather than being fixed at its initial size.

The second init container, named `clone-mysql`, performs a clone operation on
a replica Pod the first time it starts up on an empty PersistentVolume.
That means it copies all existing data from another running Pod,
so its local state is consistent enough to begin replicating from the primary server.

MySQL itself does not provide a mechanism to do this, so the example uses a
popular open-source tool called Percona XtraBackup.
During the clone, the source MySQL server might suffer reduced performance.
To minimize impact on the primary MySQL server, the script instructs each Pod to clone
from the Pod whose ordinal index is one lower.
This works because the StatefulSet controller always ensures Pod `N` is
Ready before starting Pod `N+1`.

### Starting replication

After the init containers complete successfully, the regular containers run.
The MySQL Pods consist of a `mysql` container that runs the actual `mysqld`
server, and an `xtrabackup` container that acts as a
sidecar.

The `xtrabackup` sidecar looks at the cloned data files and determines if
it's necessary to initialize MySQL replication on the replica.
If so, it waits for `mysqld` to be ready and then executes the
`CHANGE MASTER TO` and `START SLAVE` commands with replication parameters
extracted from the XtraBackup clone files.

Once a replica begins replication, it remembers its primary MySQL server and
reconnects automatically if the server restarts or the connection dies.
Also, because replicas look for the primary server at its stable DNS name
(`mysql-0.mysql`), they automatically find the primary server even if it gets a new
Pod IP due to being rescheduled.

Lastly, after starting replication, the `xtrabackup` container listens for
connections from other Pods requesting a data clone.
This server remains up indefinitely in case the StatefulSet scales up, or in
case the next Pod loses its PersistentVolumeClaim and needs to redo the clone.
