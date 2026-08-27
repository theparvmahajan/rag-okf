---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#identify-whether-you-use-admission-webhooks-identify-admission-webhooks
kind: section
title: Identify whether you use admission webhooks {#identify-admission-webhooks}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Identify whether you use admission webhooks {#identify-admission-webhooks}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#importance-of-good-webhook-design-why-good-webhook-design-matters
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#choose-an-admission-control-mechanism-choose-admission-mechanism
word_count: 83
---

Even if you don't run your own admission webhooks, some third-party applications
that you run in your clusters might use mutating or validating admission
webhooks.

To check whether your cluster has any mutating admission webhooks, run the
following command:

```shell
kubectl get mutatingwebhookconfigurations
```
The output lists any mutating admission controllers in the cluster. 

To check whether your cluster has any validating admission webhooks, run the
following command:

```shell
kubectl get validatingwebhookconfigurations
```
The output lists any validating admission controllers in the cluster.
