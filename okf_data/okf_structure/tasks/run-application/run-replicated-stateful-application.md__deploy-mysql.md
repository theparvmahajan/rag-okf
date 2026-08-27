---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#deploy-mysql
kind: section
title: Deploy MySQL
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Deploy MySQL
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#objectives
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#understanding-stateful-pod-initialization
word_count: 391
---

The example MySQL deployment consists of a ConfigMap, two Services,
and a StatefulSet.

### Create a ConfigMap {#configmap}

Create the ConfigMap from the following YAML configuration file:

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-configmap.yaml
```

This ConfigMap provides `my.cnf` overrides that let you independently control
configuration on the primary MySQL server and its replicas.
In this case, you want the primary server to be able to serve replication logs to replicas
and you want replicas to reject any writes that don't come via replication.

There's nothing special about the ConfigMap itself that causes different
portions to apply to different Pods.
Each Pod decides which portion to look at as it's initializing,
based on information provided by the StatefulSet controller.

### Create Services {#services}

Create the Services from the following YAML configuration file:

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-services.yaml
```

The headless Service provides a home for the DNS entries that the StatefulSet
controllers creates for each
Pod that's part of the set.
Because the headless Service is named `mysql`, the Pods are accessible by
resolving `<pod-name>.mysql` from within any other Pod in the same Kubernetes
cluster and namespace.

The client Service, called `mysql-read`, is a normal Service with its own
cluster IP that distributes connections across all MySQL Pods that report
being Ready. The set of potential endpoints includes the primary MySQL server and all
replicas.

Note that only read queries can use the load-balanced client Service.
Because there is only one primary MySQL server, clients should connect directly to the
primary MySQL Pod (through its DNS entry within the headless Service) to execute
writes.

### Create the StatefulSet {#statefulset}

Finally, create the StatefulSet from the following YAML configuration file:

```shell
kubectl apply -f https://k8s.io/examples/application/mysql/mysql-statefulset.yaml
```

You can watch the startup progress by running:

```shell
kubectl get pods -l app=mysql --watch
```

After a while, you should see all 3 Pods become `Running`:

```
NAME      READY     STATUS    RESTARTS   AGE
mysql-0   2/2       Running   0          2m
mysql-1   2/2       Running   0          1m
mysql-2   2/2       Running   0          1m
```

Press **Ctrl+C** to cancel the watch.

If you don't see any progress, make sure you have a dynamic PersistentVolume
provisioner enabled, as mentioned in the prerequisites.

This manifest uses a variety of techniques for managing stateful Pods as part of
a StatefulSet. The next section highlights some of these techniques to explain
what happens as the StatefulSet creates Pods.
