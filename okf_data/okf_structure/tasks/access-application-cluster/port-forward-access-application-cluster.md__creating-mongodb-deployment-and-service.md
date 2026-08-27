---
id: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#creating-mongodb-deployment-and-service
kind: section
title: Creating MongoDB deployment and service
source: tasks/access-application-cluster/port-forward-access-application-cluster.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/
heading: Creating MongoDB deployment and service
parent: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#prerequisites
next_sibling: okf-structure/tasks/access-application-cluster/port-forward-access-application-cluster.md#forward-a-local-port-to-a-port-on-the-pod
word_count: 246
---

1. Create a Deployment that runs MongoDB:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-deployment.yaml
   ```

   The output of a successful command verifies that the deployment was created:

   ```
   deployment.apps/mongo created
   ```

   View the pod status to check that it is ready:

   ```shell
   kubectl get pods
   ```

   The output displays the pod created:

   ```
   NAME                     READY   STATUS    RESTARTS   AGE
   mongo-75f59d57f4-4nd6q   1/1     Running   0          2m4s
   ```

   View the Deployment's status:

   ```shell
   kubectl get deployment
   ```

   The output displays that the Deployment was created:

   ```
   NAME    READY   UP-TO-DATE   AVAILABLE   AGE
   mongo   1/1     1            1           2m21s
   ```

   The Deployment automatically manages a ReplicaSet.
   View the ReplicaSet status using:

   ```shell
   kubectl get replicaset
   ```

   The output displays that the ReplicaSet was created:

   ```
   NAME               DESIRED   CURRENT   READY   AGE
   mongo-75f59d57f4   1         1         1       3m12s
   ```

2. Create a Service to expose MongoDB on the network:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/mongodb/mongo-service.yaml
   ```

   The output of a successful command verifies that the Service was created:

   ```
   service/mongo created
   ```

   Check the Service created:

   ```shell
   kubectl get service mongo
   ```

   The output displays the service created:

   ```
   NAME    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)     AGE
   mongo   ClusterIP   10.96.41.183   <none>        27017/TCP   11s
   ```

3. Verify that the MongoDB server is running in the Pod, and listening on port 27017:

   ```shell
   # Change mongo-75f59d57f4-4nd6q to the name of the Pod
   kubectl get pod mongo-75f59d57f4-4nd6q --template='{{(index (index .spec.containers 0).ports 0).containerPort}}{{"\n"}}'
   ```

   The output displays the port for MongoDB in that Pod:

   ```
   27017
   ```

   27017 is the official TCP port for MongoDB.
