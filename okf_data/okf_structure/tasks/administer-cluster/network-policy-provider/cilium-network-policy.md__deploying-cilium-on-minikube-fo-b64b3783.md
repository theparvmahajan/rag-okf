---
id: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#deploying-cilium-on-minikube-for-basic-testing
kind: section
title: Deploying Cilium on Minikube for Basic Testing
source: tasks/administer-cluster/network-policy-provider/cilium-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/
heading: Deploying Cilium on Minikube for Basic Testing
parent: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#deploying-cilium-for-production-use
word_count: 234
---

To get familiar with Cilium easily you can follow the
Cilium Kubernetes Getting Started Guide
to perform a basic DaemonSet installation of Cilium in minikube.

To start minikube, which requires version v1.5.2 or higher, run it with the
following arguments:

```shell
minikube version
```

```
minikube version: v1.5.2
```

```shell
minikube start --network-plugin=cni
```

For minikube you can install Cilium using its CLI tool. To do so, first download the latest
version of the CLI with the following command:

```shell
curl -LO https://github.com/cilium/cilium-cli/releases/latest/download/cilium-linux-amd64.tar.gz
```

Then extract the downloaded file to your `/usr/local/bin` directory with the following command:

```shell
sudo tar xzvfC cilium-linux-amd64.tar.gz /usr/local/bin
rm cilium-linux-amd64.tar.gz
```

After running the above commands, you can now install Cilium with the following command: 

```shell
cilium install
```

Cilium will then automatically detect the cluster configuration and create and
install the appropriate components for a successful installation.
The components are:

- Certificate Authority (CA) in Secret `cilium-ca` and certificates for Hubble (Cilium's observability layer).
- Service accounts.
- Cluster roles.
- ConfigMap.
- Agent DaemonSet and an Operator Deployment.

After the installation, you can view the overall status of the Cilium deployment with the `cilium status` command.
See the expected output of the `status` command
here. 

The remainder of the Getting Started Guide explains how to enforce both L3/L4
(i.e., IP address + port) security policies, as well as L7 (e.g., HTTP) security
policies using an example application.
