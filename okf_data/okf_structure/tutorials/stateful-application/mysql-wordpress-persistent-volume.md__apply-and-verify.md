---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#apply-and-verify
kind: section
title: Apply and Verify
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Apply and Verify
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#add-resource-configs-for-mysql-and-wordpress
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#cleanup
word_count: 328
---

The `kustomization.yaml` contains all the resources for deploying a WordPress site and a
MySQL database. You can apply the directory by

```shell
kubectl apply -k ./
```

Now you can verify that all objects exist.

1. Verify that the Secret exists by running the following command:

   ```shell
   kubectl get secrets
   ```

   The response should be like this:

   ```
   NAME                    TYPE                                  DATA   AGE
   mysql-pass-c57bb4t7mf   Opaque                                1      9s
   ```

2. Verify that a PersistentVolume got dynamically provisioned.

   ```shell
   kubectl get pvc
   ```

   
   It can take up to a few minutes for the PVs to be provisioned and bound.
   

   The response should be like this:

   ```
   NAME             STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS       AGE
   mysql-pv-claim   Bound     pvc-8cbd7b2e-4044-11e9-b2bb-42010a800002   20Gi       RWO            standard           77s
   wp-pv-claim      Bound     pvc-8cd0df54-4044-11e9-b2bb-42010a800002   20Gi       RWO            standard           77s
   ```

3. Verify that the Pod is running by running the following command:

   ```shell
   kubectl get pods
   ```

   
   It can take up to a few minutes for the Pod's Status to be `RUNNING`.
   

   The response should be like this:

   ```
   NAME                               READY     STATUS    RESTARTS   AGE
   wordpress-mysql-1894417608-x5dzt   1/1       Running   0          40s
   ```

4. Verify that the Service is running by running the following command:

   ```shell
   kubectl get services wordpress
   ```

   The response should be like this:

   ```
   NAME        TYPE            CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
   wordpress   LoadBalancer    10.0.0.89    <pending>     80:32406/TCP   4m
   ```

   
   Minikube can only expose Services through `NodePort`. The EXTERNAL-IP is always pending.
   

5. Run the following command to get the IP Address for the WordPress Service:

   ```shell
   minikube service wordpress --url
   ```

   The response should be like this:

   ```
   http://1.2.3.4:32406
   ```

6. Copy the IP address, and load the page in your browser to view your site.

   You should see the WordPress set up page similar to the following screenshot.

   wordpress-init

   
   Do not leave your WordPress installation on this page. If another user finds it,
   they can set up a website on your instance and use it to serve malicious content.
   Either install WordPress by creating a username and password or delete your instance.
