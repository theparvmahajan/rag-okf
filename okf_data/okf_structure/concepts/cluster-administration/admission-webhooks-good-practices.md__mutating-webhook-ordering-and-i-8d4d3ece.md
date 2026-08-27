---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-ordering-and-idempotence-ordering-idempotence
kind: section
title: Mutating webhook ordering and idempotence {#ordering-idempotence}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Mutating webhook ordering and idempotence {#ordering-idempotence}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-scope-and-field-considerations-mutation-scope-considerations
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-testing-and-validation-mutation-testing-validation
word_count: 520
---

This section provides recommendations for webhook order and designing idempotent
webhooks. In summary, these are as follows:

* Don't rely on a specific order of execution.
* Validate mutations before admission.
* Check for mutations being overwritten by other controllers.
* Ensure that the set of mutating webhooks is idempotent, not just the
  individual webhooks.

### Don't rely on mutating webhook invocation order {#dont-rely-webhook-order}

Mutating admission webhooks don't run in a consistent order. Various factors
might change when a specific webhook is called. Don't rely on your webhook
running at a specific point in the admission process. Other webhooks could still
mutate your modified object.

The following recommendations might help to minimize the risk of unintended
changes:

* Validate mutations before admission
* Use a reinvocation policy to observe changes to an object by other plugins
  and re-run the webhook as needed. For details, see
  Reinvocation policy.

### Ensure that the mutating webhooks in your cluster are idempotent {#ensure-mutating-webhook-idempotent}

Every mutating admission webhook should be _idempotent_. The webhook should be
able to run on an object that it already modified without making additional
changes beyond the original change.

Additionally, all of the mutating webhooks in your cluster should, as a
collection, be idempotent. After the mutation phase of admission control ends,
every individual mutating webhook should be able to run on an object without 
making additional changes to the object.

Depending on your environment, ensuring idempotence at scale might be
challenging. The following recommendations might help:

* Use validating admission controllers to verify the final state of
  critical workloads.
* Test your deployments in a staging cluster to see if any objects get modified
  multiple times by the same webhook. 
* Ensure that the scope of each mutating webhook is specific and limited.

The following examples show idempotent mutation logic:

1. For a **create** Pod request, set the field
  `.spec.securityContext.runAsNonRoot` of the Pod to true.

1. For a **create** Pod request, if the field
   `.spec.containers[].resources.limits` of a container is not set, set default
   resource limits.

1. For a **create** Pod request, inject a sidecar container with name
   `foo-sidecar` if no container with the name `foo-sidecar` already exists.

In these cases, the webhook can be safely reinvoked, or admit an object that
already has the fields set.

The following examples show non-idempotent mutation logic:

1. For a **create** Pod request, inject a sidecar container with name
   `foo-sidecar` suffixed with the current timestamp (such as
   `foo-sidecar-19700101-000000`).

   Reinvoking the webhook can result in the same sidecar being injected multiple
   times to a Pod, each time with a different container name. Similarly, the
   webhook can inject duplicated containers if the sidecar already exists in
   a user-provided pod.

1. For a **create**/**update** Pod request, reject if the Pod has label `env`
   set, otherwise add an `env: prod` label to the Pod.

   Reinvoking the webhook will result in the webhook failing on its own output.

1. For a **create** Pod request, append a sidecar container named `foo-sidecar`
   without checking whether a `foo-sidecar` container exists.

   Reinvoking the webhook will result in duplicated containers in the Pod, which
   makes the request invalid and rejected by the API server.
