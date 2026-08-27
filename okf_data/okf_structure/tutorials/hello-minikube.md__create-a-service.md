---
id: okf-structure/tutorials/hello-minikube.md#create-a-service
kind: section
title: Create a Service
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Create a Service
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#create-a-deployment
next_sibling: okf-structure/tutorials/hello-minikube.md#enable-addons
word_count: 230
---

By default, the Pod is only accessible by its internal IP address within the
Kubernetes cluster. To make the `hello-node` Container accessible from outside the
Kubernetes virtual network, you have to expose the Pod as a
Kubernetes *Service*.

The agnhost container has a `/shell` endpoint, which is useful for
debugging, but dangerous to expose to the public internet. Do not run this on an
internet-facing cluster, or a production cluster.

1. Expose the Pod to the public internet using the `kubectl expose` command:

    ```shell
    kubectl expose deployment hello-node --type=LoadBalancer --port=8080
    ```

    The `--type=LoadBalancer` flag indicates that you want to expose your Service
    outside of the cluster.

    The application code inside the test image only listens on TCP port 8080. If you used
    `kubectl expose` to expose a different port, clients could not connect to that other port.

2. View the Service you created:

    ```shell
    kubectl get services
    ```

    The output is similar to:

    ```
    NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    hello-node   LoadBalancer   10.108.144.78   <pending>     8080:30369/TCP   21s
    kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          23m
    ```

    On cloud providers that support load balancers,
    an external IP address would be provisioned to access the Service. On minikube,
    the `LoadBalancer` type makes the Service accessible through the `minikube service`
    command.

3. Run the following command:

    ```shell
    minikube service hello-node
    ```

    This opens up a browser window that serves your app and shows the app's response.
