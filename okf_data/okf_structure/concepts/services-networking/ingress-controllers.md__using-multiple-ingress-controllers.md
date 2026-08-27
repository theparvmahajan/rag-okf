---
id: okf-structure/concepts/services-networking/ingress-controllers.md#using-multiple-ingress-controllers
kind: section
title: Using multiple Ingress controllers
source: concepts/services-networking/ingress-controllers.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/
heading: Using multiple Ingress controllers
parent: okf-structure/concepts/services-networking/ingress-controllers
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress-controllers.md#third-party-ingress-controllers
next_sibling: okf-structure/concepts/services-networking/ingress-controllers.md#whatsnext
word_count: 135
---

You may deploy any number of ingress controllers using ingress class
within a cluster. Note the `.metadata.name` of your ingress class resource. When you create an ingress you would need that name to specify the `ingressClassName` field on your Ingress object (refer to IngressSpec v1 reference). `ingressClassName` is a replacement of the older annotation method.

If you do not specify an IngressClass for an Ingress, and your cluster has exactly one IngressClass marked as default, then Kubernetes applies the cluster's default IngressClass to the Ingress.
You mark an IngressClass as default by setting the `ingressclass.kubernetes.io/is-default-class` annotation on that IngressClass, with the string value `"true"`.

Ideally, all ingress controllers should fulfill this specification, but the various ingress
controllers operate slightly differently.

Make sure you review your ingress controller's documentation to understand the caveats of choosing it.
