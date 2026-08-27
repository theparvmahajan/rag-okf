---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-deployment-mutating-webhook-deployment
kind: section
title: Mutating webhook deployment {#mutating-webhook-deployment}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Mutating webhook deployment {#mutating-webhook-deployment}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-testing-and-validation-mutation-testing-validation
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#examples-of-good-implementations-example-good-implementations
word_count: 248
---

This section provides recommendations for deploying your mutating admission
webhooks. In summary, these are as follows:

* Gradually roll out the webhook configuration and monitor for issues by
  namespace.
* Limit access to edit the webhook configuration resources. 
* Limit access to the namespace that runs the webhook server, if the server is
  in-cluster.

### Install and enable a mutating webhook {#install-enable-mutating-webhook}

When you're ready to deploy your mutating webhook to a cluster, use the
following order of operations: 

1.  Install the webhook server and start it.
1.  Set the `failurePolicy` field in the MutatingWebhookConfiguration manifest
    to Ignore. This lets you avoid disruptions caused by misconfigured webhooks.
1.  Set the `namespaceSelector` field in the MutatingWebhookConfiguration
    manifest to a test namespace.
1.  Deploy the MutatingWebhookConfiguration to your cluster.

Monitor the webhook in the test namespace to check for any issues, then roll the
webhook out to other namespaces. If the webhook intercepts an API request that
it wasn't meant to intercept, pause the rollout and adjust the scope of the
webhook configuration.

### Limit edit access to mutating webhooks {#limit-edit-access}

Mutating webhooks are powerful Kubernetes controllers. Use RBAC or another
authorization mechanism to limit access to your webhook configurations and
servers. For RBAC, ensure that the following access is only available to trusted
entities:

* Verbs: **create**, **update**, **patch**, **delete**, **deletecollection**
* API group: `admissionregistration.k8s.io/v1`
* API kind: MutatingWebhookConfigurations

If your mutating webhook server runs in the cluster, limit access to create or
modify any resources in that namespace.
