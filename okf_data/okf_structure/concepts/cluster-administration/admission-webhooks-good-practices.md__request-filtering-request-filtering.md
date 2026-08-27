---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#request-filtering-request-filtering
kind: section
title: Request filtering {#request-filtering}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Request filtering {#request-filtering}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#performance-and-latency-performance-latency
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-scope-and-field-considerations-mutation-scope-considerations
word_count: 352
---

This section provides recommendations for filtering which requests trigger
specific webhooks. In summary, these are as follows:

* Limit the webhook scope to avoid system components and read-only requests.
* Limit webhooks to specific namespaces.
* Use match conditions to perform fine-grained request filtering.
* Match all versions of an object.

### Limit the scope of each webhook {#webhook-limit-scope}

Admission webhooks are only called when an API request matches the corresponding
webhook configuration. Limit the scope of each webhook to reduce unnecessary
calls to the webhook server. Consider the following scope limitations:

* Avoid matching objects in the `kube-system` namespace. If you run your own
  Pods in the `kube-system` namespace, use an
  `objectSelector`
  to avoid mutating a critical workload.
* Don't mutate node leases, which exist as Lease objects in the
  `kube-node-lease` system namespace. Mutating node leases might result in
  failed node upgrades. Only apply validation controls to Lease objects in this
  namespace if you're confident that the controls won't put your cluster at
  risk.
* Don't mutate TokenReview or SubjectAccessReview objects. These are always
  read-only requests. Modifying these objects might break your cluster.
* Limit each webhook to a specific namespace by using a
  `namespaceSelector`.

### Filter for specific requests by using match conditions {#filter-match-conditions}

Admission controllers support multiple fields that you can use to match requests
that meet specific criteria. For example, you can use a `namespaceSelector` to
filter for requests that target a specific namespace.

For more fine-grained request filtering, use the `matchConditions` field in your
webhook configuration. This field lets you write multiple CEL expressions that
must evaluate to `true` for a request to trigger your admission webhook. Using
`matchConditions` might significantly reduce the number of calls to your webhook
server.

For details, see
Matching requests: `matchConditions`.

### Match all versions of an API {#match-all-versions}

By default, admission webhooks run on any API versions that affect a specified
resource. The `matchPolicy` field in the webhook configuration controls this
behavior. Specify a value of `Equivalent` in the `matchPolicy` field or omit
the field to allow the webhook to run on any API version. 

For details, see
Matching requests: `matchPolicy`.
