---
id: okf-structure/tutorials/hello-minikube.md#check-the-status-of-the-minikube-cluster
kind: section
title: Check the status of the minikube cluster
source: tutorials/hello-minikube.md
url: https://kubernetes.io/docs/tutorials/hello-minikube/
heading: Check the status of the minikube cluster
parent: okf-structure/tutorials/hello-minikube
children: []
prev_sibling: okf-structure/tutorials/hello-minikube.md#create-a-minikube-cluster
next_sibling: okf-structure/tutorials/hello-minikube.md#open-the-dashboard
word_count: 55
---

Verify the status of the minikube cluster to ensure all the components are in a running state.

```shell
minikube status
```
The output from the above command should show all components Running or Configured, as shown in the example output below:

```
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
