---
id: okf-structure/concepts/services-networking/ingress.md#prerequisites
kind: section
title: Prerequisites
source: concepts/services-networking/ingress.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress/
heading: Prerequisites
parent: okf-structure/concepts/services-networking/ingress
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress.md#what-is-ingress
next_sibling: okf-structure/concepts/services-networking/ingress.md#the-ingress-resource
word_count: 60
---

You must have an Ingress controller
to satisfy an Ingress. Only creating an Ingress resource has no effect.

You can choose from a number of Ingress controllers.

Ideally, all Ingress controllers should fit the reference specification. In reality, the various Ingress
controllers operate slightly differently.

Make sure you review your Ingress controller's documentation to understand the caveats of choosing it.
