---
id: okf-structure/tasks/job/job-with-pod-to-pod-communication.md#introduction
kind: section
title: Job with Pod-to-Pod Communication
source: tasks/job/job-with-pod-to-pod-communication.md
url: https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/
heading: null
parent: okf-structure/tasks/job/job-with-pod-to-pod-communication
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/job-with-pod-to-pod-communication.md#prerequisites
word_count: 153
---

In this example, you will run a Job in Indexed completion mode
configured such that the pods created by the Job can communicate with each other using pod hostnames rather
than pod IP addresses.

Pods within a Job might need to communicate among themselves. The user workload running in each pod
could query the Kubernetes API server to learn the IPs of the other Pods, but it's much simpler to
rely on Kubernetes' built-in DNS resolution.

Jobs in Indexed completion mode automatically set the pods' hostname to be in the format of
`${jobName}-${completionIndex}`. You can use this format to deterministically build
pod hostnames and enable pod communication *without* needing to create a client connection to
the Kubernetes control plane to obtain pod hostnames/IPs via API requests.

This configuration is useful for use cases where pod networking is required but you don't want
to depend on a network connection with the Kubernetes API server.
