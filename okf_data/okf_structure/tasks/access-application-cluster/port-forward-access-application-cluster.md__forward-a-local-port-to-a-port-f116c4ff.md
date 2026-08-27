---
id: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#forward-a-local-port-to-a-port-on-the-pod
kind: section
title: Forward a local port to a port on the Pod
source: tasks/access-application-cluster/port-forward-access-application-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/
heading: Forward a local port to a port on the Pod
parent: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#creating-mongodb-deployment-and-service
next_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#discussion
word_count: 242
---

1. `kubectl port-forward` allows using resource name, such as a pod name, to select a matching pod to port forward to.

   ```shell
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl port-forward mongo-75f59d57f4-4nd6q 28015:27017
   ```

   which is the same as

   ```shell
   kubectl port-forward pods/mongo-75f59d57f4-4nd6q 28015:27017
   ```

   or

   ```shell
   kubectl port-forward deployment/mongo 28015:27017
   ```

   or

   ```shell
   kubectl port-forward replicaset/mongo-75f59d57f4 28015:27017
   ```

   or

   ```shell
   kubectl port-forward service/mongo 28015:27017
   ```

   Any of the above commands works. The output is similar to this:

   ```
   Forwarding from 127.0.0.1:28015 -> 27017
   Forwarding from [::1]:28015 -> 27017
   ```

   
   `kubectl port-forward` does not return. To continue with the exercises, you will need to open another terminal.
   

2. Start the MongoDB command line interface:

   ```shell
   mongosh --port 28015
   ```

3. At the MongoDB command line prompt, enter the `ping` command:

   ```
   db.runCommand( { ping: 1 } )
   ```

   A successful ping request returns:

   ```
   { ok: 1 }
   ```

### Optionally let _kubectl_ choose the local port {#let-kubectl-choose-local-port}

If you don't need a specific local port, you can let `kubectl` choose and allocate 
the local port and thus relieve you from having to manage local port conflicts, with 
the slightly simpler syntax:

```shell
kubectl port-forward deployment/mongo :27017
```

The `kubectl` tool finds a local port number that is not in use (avoiding low ports numbers,
because these might be used by other applications). The output is similar to:

```
Forwarding from 127.0.0.1:63753 -> 27017
Forwarding from [::1]:63753 -> 27017
```
