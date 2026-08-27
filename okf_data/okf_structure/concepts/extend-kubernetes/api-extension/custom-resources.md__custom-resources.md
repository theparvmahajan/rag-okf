---
id: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#custom-resources
kind: section
title: Custom resources
source: concepts/extend-kubernetes/api-extension/custom-resources.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
heading: Custom resources
parent: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/api-extension/custom-resources.md#custom-controllers
word_count: 125
---

A *resource* is an endpoint in the Kubernetes API that
stores a collection of API objects
of a certain kind; for example, the built-in *pods* resource contains a collection of Pod objects.

A *custom resource* is an extension of the Kubernetes API that is not necessarily available in a default
Kubernetes installation. It represents a customization of a particular Kubernetes installation. However,
many core Kubernetes functions are now built using custom resources, making Kubernetes more modular.

Custom resources can appear and disappear in a running cluster through dynamic registration,
and cluster admins can update custom resources independently of the cluster itself.
Once a custom resource is installed, users can create and access its objects using
kubectl, just as they do for built-in resources
like *Pods*.
