---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#introduction
kind: section
title: Configure a Pod to Use a ConfigMap
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: null
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#prerequisites
word_count: 108
---

Many applications rely on configuration which is used during either application initialization or runtime.
Most times, there is a requirement to adjust values assigned to configuration parameters.
ConfigMaps are a Kubernetes mechanism that let you inject configuration data into application
pods.

The ConfigMap concept allow you to decouple configuration artifacts from image content to
keep containerized applications portable. For example, you can download and run the same
container image to spin up containers for 
the purposes of local development, system test, or running a live end-user workload.

This page provides a series of usage examples demonstrating how to create ConfigMaps and
configure Pods using data stored in ConfigMaps.
