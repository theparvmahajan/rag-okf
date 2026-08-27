---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-testing-and-validation-mutation-testing-validation
kind: section
title: Mutation testing and validation {#mutation-testing-validation}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Mutation testing and validation {#mutation-testing-validation}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-ordering-and-idempotence-ordering-idempotence
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-deployment-mutating-webhook-deployment
word_count: 373
---

This section provides recommendations for testing your mutating webhooks and
validating mutated objects. In summary, these are as follows:

* Test webhooks in staging environments.
* Avoid mutations that violate validations.
* Test minor version upgrades for regressions and conflicts.
* Validate mutated objects before admission.

### Test webhooks in staging environments {#test-in-staging-environments}

Robust testing should be a core part of your release cycle for new or updated
webhooks. If possible, test any changes to your cluster webhooks in a staging
environment that closely resembles your production clusters. At the very least,
consider using a tool like minikube or
kind to create a small test cluster for webhook
changes.

### Ensure that mutations don't violate validations {#ensure-mutations-dont-violate-validations}

Your mutating webhooks shouldn't break any of the validations that apply to an
object before admission. For example, consider a mutating webhook that sets the 
default CPU request of a Pod to a specific value. If the CPU limit of that Pod
is set to a lower value than the mutated request, the Pod fails admission. 

Test every mutating webhook against the validations that run in your cluster.

### Test minor version upgrades to ensure consistent behavior {#test-minor-version-upgrades}

Before upgrading your production clusters to a new minor version, test your
webhooks and workloads in a staging environment. Compare the results to ensure
that your webhooks continue to function as expected after the upgrade. 

Additionally, use the following resources to stay informed about API changes:

* Kubernetes release notes
* Kubernetes blog

### Validate mutations before admission {#validate-mutations}

Mutating webhooks run to completion before any validating webhooks run. There is
no stable order in which mutations are applied to objects. As a result, your
mutations could get overwritten by a mutating webhook that runs at a later time.

Add a validating admission controller like a ValidatingAdmissionWebhook or a
ValidatingAdmissionPolicy to your cluster to ensure that your mutations
are still present. For example, consider a mutating webhook that inserts the
`restartPolicy: Always` field to specific init containers to make them run as
sidecar containers. You could run a validating webhook to ensure that those
init containers retained the `restartPolicy: Always` configuration after all
mutations were completed. 

For details, see the following resources:

* Validating Admission Policy
* ValidatingAdmissionWebhooks
