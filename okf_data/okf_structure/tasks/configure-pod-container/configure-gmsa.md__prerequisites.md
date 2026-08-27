---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#configure-gmsas-and-windows-nodes-in-active-directory
word_count: 290
---

You need to have a Kubernetes cluster and the `kubectl` command-line tool must be
configured to communicate with your cluster. The cluster is expected to have Windows worker nodes.
This section covers a set of initial steps required once for each cluster:

### Install the GMSACredentialSpec CRD

A CustomResourceDefinition(CRD)
for GMSA credential spec resources needs to be configured on the cluster to define
the custom resource type `GMSACredentialSpec`. Download the GMSA CRD
YAML
and save it as gmsa-crd.yaml. Next, install the CRD with `kubectl apply -f gmsa-crd.yaml`

### Install webhooks to validate GMSA users

Two webhooks need to be configured on the Kubernetes cluster to populate and
validate GMSA credential spec references at the Pod or container level:

1. A mutating webhook that expands references to GMSAs (by name from a Pod specification)
   into the full credential spec in JSON form within the Pod spec.

1. A validating webhook ensures all references to GMSAs are authorized to be used by the Pod service account.

Installing the above webhooks and associated objects require the steps below:

1. Create a certificate key pair (that will be used to allow the webhook container to communicate to the cluster)

1. Install a secret with the certificate from above.

1. Create a deployment for the core webhook logic.

1. Create the validating and mutating webhook configurations referring to the deployment.

A script
can be used to deploy and configure the GMSA webhooks and associated objects
mentioned above. The script can be run with a `--dry-run=server` option to
allow you to review the changes that would be made to your cluster.

The YAML template
used by the script may also be used to deploy the webhooks and associated objects
manually (with appropriate substitutions for the parameters)
