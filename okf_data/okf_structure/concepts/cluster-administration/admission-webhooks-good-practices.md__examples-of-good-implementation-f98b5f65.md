---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#examples-of-good-implementations-example-good-implementations
kind: section
title: Examples of good implementations {#example-good-implementations}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Examples of good implementations {#example-good-implementations}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-deployment-mutating-webhook-deployment
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#whatsnext
word_count: 54
---

The following projects are examples of "good" custom webhook server
implementations. You can use them as a starting point when designing your own
webhooks. Don't use these examples as-is; use them as a starting point and
design your webhooks to run well in your specific environment.

* `cert-manager`
* Gatekeeper Open Policy Agent (OPA)
