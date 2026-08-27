---
id: okf-structure/tutorials/hello-minikube.md#create-a-deployment
kind: section
title: Create a Deployment
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Create a Deployment
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#open-the-dashboard
next_sibling: okf-structure/tutorials/hello-minikube.md#create-a-service
word_count: 282
---

A Kubernetes *Pod* is a group of one or more Containers,
tied together for the purposes of administration and networking. The Pod in this
tutorial has only one Container. A Kubernetes
*Deployment* checks on the health of your
Pod and restarts the Pod's Container if it terminates. Deployments are the
recommended way to manage the creation and scaling of Pods.

1. Use the `kubectl create` command to create a Deployment that manages a Pod. The
   Pod runs a Container based on the provided Docker image.

    ```shell
    # Run a test container image that includes a webserver
    kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.53 -- /agnhost netexec --http-port=8080
    ```

1. View the Deployment:

    ```shell
    kubectl get deployments
    ```

    The output is similar to:

    ```
    NAME         READY   UP-TO-DATE   AVAILABLE   AGE
    hello-node   1/1     1            1           1m
    ```

    (It may take some time for the pod to become available. If you see "0/1", try again in a few seconds.)

1. View the Pod:

    ```shell
    kubectl get pods
    ```

    The output is similar to:

    ```
    NAME                          READY     STATUS    RESTARTS   AGE
    hello-node-5f76cf6ccf-br9b5   1/1       Running   0          1m
    ```

1. View cluster events:

    ```shell
    kubectl get events
    ```

1. View the `kubectl` configuration:

    ```shell
    kubectl config view
    ```

1. View application logs for a container in a pod (replace pod name with the one you got from `kubectl get pods`).

   
   Replace `hello-node-5f76cf6ccf-br9b5` in the `kubectl logs` command with the name of the pod from the `kubectl get pods` command output.
   

   ```shell
   kubectl logs hello-node-5f76cf6ccf-br9b5
   ```

   The output is similar to:

   ```
   I0911 09:19:26.677397       1 log.go:195] Started HTTP server on port 8080
   I0911 09:19:26.677586       1 log.go:195] Started UDP server on port  8081
   ```

For more information about `kubectl` commands, see the kubectl overview.
