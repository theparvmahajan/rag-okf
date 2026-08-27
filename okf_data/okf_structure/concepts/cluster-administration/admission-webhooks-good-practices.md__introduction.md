---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#introduction
kind: section
title: Admission Webhook Good Practices
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: null
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#importance-of-good-webhook-design-why-good-webhook-design-matters
word_count: 53
---

This page provides good practices and considerations when designing
_admission webhooks_ in Kubernetes. This information is intended for
cluster operators who run admission webhook servers or third-party applications
that modify or validate your API requests.

Before reading this page, ensure that you're familiar with the following
concepts:

* Admission controllers
* Admission webhooks
