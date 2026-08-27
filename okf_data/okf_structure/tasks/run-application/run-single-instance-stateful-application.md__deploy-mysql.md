---
id: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#deploy-mysql
kind: section
title: Deploy MySQL
source: tasks/run-application/run-single-instance-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
heading: Deploy MySQL
parent: okf-structure/tasks/run-application/run-single-instance-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#prerequisites
next_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#accessing-the-mysql-instance
word_count: 336
---

You can run a stateful application by creating a Kubernetes Deployment
and connecting it to an existing PersistentVolume using a
PersistentVolumeClaim. For example, this YAML file describes a
Deployment that runs MySQL and references the PersistentVolumeClaim. The file
defines a volume mount for /var/lib/mysql, and then creates a
PersistentVolumeClaim that looks for a 20G volume. This claim is
satisfied by any existing volume that meets the requirements,
or by a dynamic provisioner.

Note: The password is defined in the config yaml, and this is insecure. See
Kubernetes Secrets
for a secure solution.

1. Deploy the PV and PVC of the YAML file:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mysql/mysql-pv.yaml
   ```

1. Deploy the contents of the YAML file:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mysql/mysql-deployment.yaml
   ```

1. Display information about the Deployment:

   ```shell
   kubectl describe deployment mysql
   ```

   The output is similar to this:

   ```
   Name:                 mysql
   Namespace:            default
   CreationTimestamp:    Tue, 01 Nov 2016 11:18:45 -0700
   Labels:               app=mysql
   Annotations:          deployment.kubernetes.io/revision=1
   Selector:             app=mysql
   Replicas:             1 desired | 1 updated | 1 total | 0 available | 1 unavailable
   StrategyType:         Recreate
   MinReadySeconds:      0
   Pod Template:
     Labels:       app=mysql
     Containers:
       mysql:
       Image:      mysql:9
       Port:       3306/TCP
       Environment:
         MYSQL_ROOT_PASSWORD:      password
       Mounts:
         /var/lib/mysql from mysql-persistent-storage (rw)
     Volumes:
       mysql-persistent-storage:
       Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
       ClaimName:  mysql-pv-claim
       ReadOnly:   false
   Conditions:
     Type          Status  Reason
     ----          ------  ------
     Available     False   MinimumReplicasUnavailable
     Progressing   True    ReplicaSetUpdated
   OldReplicaSets:       <none>
   NewReplicaSet:        mysql-63082529 (1/1 replicas created)
   Events:
     FirstSeen    LastSeen    Count    From                SubobjectPath    Type        Reason            Message
     ---------    --------    -----    ----                -------------    --------    ------            -------
     33s          33s         1        {deployment-controller }             Normal      ScalingReplicaSet Scaled up replica set mysql-63082529 to 1
   ```

1. List the pods created by the Deployment:

   ```shell
   kubectl get pods -l app=mysql
   ```

   The output is similar to this:

   ```
   NAME                   READY     STATUS    RESTARTS   AGE
   mysql-63082529-2z3ki   1/1       Running   0          3m
   ```

1. Inspect the PersistentVolumeClaim:

   ```shell
   kubectl describe pvc mysql-pv-claim
   ```

   The output is similar to this:

   ```
   Name:         mysql-pv-claim
   Namespace:    default
   StorageClass:
   Status:       Bound
   Volume:       mysql-pv-volume
   Labels:       <none>
   Annotations:    pv.kubernetes.io/bind-completed=yes
                   pv.kubernetes.io/bound-by-controller=yes
   Capacity:     20Gi
   Access Modes: RWO
   Events:       <none>
   ```
