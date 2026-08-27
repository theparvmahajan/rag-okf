---
id: okf-structure/concepts/cluster-administration/kube-state-metrics.md#introduction
kind: section
title: Metrics for Kubernetes Object States
source: concepts/cluster-administration/kube-state-metrics.md
url: https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/
heading: null
parent: okf-structure/concepts/cluster-administration/kube-state-metrics
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/kube-state-metrics.md#example-using-metrics-from-kube-state-metrics-to-query-the-cluster-state-example-kube-state-metrics-query-1
word_count: 164
---

The state of Kubernetes objects in the Kubernetes API can be exposed as metrics.
An add-on agent called kube-state-metrics can connect to the Kubernetes API server and expose a HTTP endpoint with metrics generated from the state of individual objects in the cluster.
It exposes various information about the state of objects like labels and annotations, startup and termination times, status or the phase the object currently is in.
For example, containers running in pods create a `kube_pod_container_info` metric.
This includes the name of the container, the name of the pod it is part of, the namespace the pod is running in, the name of the container image, the ID of the image, the image name from the spec of the container, the ID of the running container and the ID of the pod as labels.

An external component that is able and capable to scrape the endpoint of kube-state-metrics (for example via Prometheus) can now be used to enable the following use cases.
