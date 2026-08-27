---
id: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutation-scope-and-field-considerations-mutation-scope-considerations
kind: section
title: Mutation scope and field considerations {#mutation-scope-considerations}
source: concepts/cluster-administration/admission-webhooks-good-practices.md
url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
heading: Mutation scope and field considerations {#mutation-scope-considerations}
parent: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices
children: []
prev_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#request-filtering-request-filtering
next_sibling: okf-structure/concepts/cluster-administration/admission-webhooks-good-practices.md#mutating-webhook-ordering-and-idempotence-ordering-idempotence
word_count: 1038
---

This section provides recommendations for the scope of mutations and any special
considerations for object fields. In summary, these are as follows:

* Patch only the fields that you need to patch.
* Don't overwrite array values.
* Avoid side effects in mutations when possible.
* Avoid self-mutations.
* Fail open and validate the final state.
* Plan for future field updates in later versions.
* Prevent webhooks from self-triggering.
* Don't change immutable objects.

### Patch only required fields {#patch-required-fields}

Admission webhook servers send HTTP responses to indicate what to do with a
specific Kubernetes API request. This response is an AdmissionReview object.
A mutating webhook can add specific fields to mutate before allowing admission
by using the `patchType` field and the `patch` field in the response. Ensure
that you only modify the fields that require a change. 

For example, consider a mutating webhook that's configured to ensure that
`web-server` Deployments have at least three replicas. When a request to
create a Deployment object matches your webhook configuration, the webhook
should only update the value in the `spec.replicas` field.

### Don't overwrite array values {#dont-overwrite-arrays}

Fields in Kubernetes object specifications might include arrays. Some arrays
contain key:value pairs (like the `envVar` field in a container specification),
while other arrays are unkeyed (like the `readinessGates` field in a Pod
specification). The order of values in an array field might matter in some
situations. For example, the order of arguments in the `args` field of a
container specification might affect the container. 

Consider the following when modifying arrays:

* Whenever possible, use the `add` JSONPatch operation instead of `replace` to
  avoid accidentally replacing a required value.
* Treat arrays that don't use key:value pairs as sets.
* Ensure that the values in the field that you modify aren't required to be
  in a specific order. 
* Don't overwrite existing key:value pairs unless absolutely necessary.
* Use caution when modifying label fields. An accidental modification might
  cause label selectors to break, resulting in unintended behavior.

### Avoid side effects {#avoid-side-effects}

Ensure that your webhooks operate only on the content of the AdmissionReview
that's sent to them, and do not make out-of-band changes. These additional
changes, called _side effects_, might cause conflicts during admission if they
aren't reconciled properly. The `.webhooks[].sideEffects` field should
be set to `None` if a webhook doesn't have any side effect. 

If side effects are required during the admission evaluation, they must be
suppressed when processing an AdmissionReview object with `dryRun` set to
`true`, and the `.webhooks[].sideEffects` field should be set to `NoneOnDryRun`.

For details, see
Side effects.

### Avoid self-mutations {#avoid-self-mutation}

A webhook running inside the cluster might cause deadlocks for its own
deployment if it is configured to intercept resources required to start its own
Pods.

For example, a mutating admission webhook is configured to admit **create** Pod
requests only if a certain label is set in the Pod (such as `env: prod`).
The webhook server runs in a Deployment that doesn't set the `env` label.

When a node that runs the webhook server Pods becomes unhealthy, the webhook
Deployment tries to reschedule the Pods to another node. However, the existing
webhook server rejects the requests since the `env` label is unset. As a
result, the migration cannot happen.

Exclude the namespace where your webhook is running with a
`namespaceSelector`.

### Avoid dependency loops {#avoid-dependency-loops}

Dependency loops can occur in scenarios like the following:

* Two webhooks check each other's Pods. If both webhooks become unavailable
  at the same time, neither webhook can start.
* Your webhook intercepts cluster add-on components, such as networking plugins
  or storage plugins, that your webhook depends on. If both the webhook and the
  dependent add-on become unavailable, neither component can function.

To avoid these dependency loops, try the following:

* Use
  ValidatingAdmissionPolicies
  to avoid introducing dependencies.
* Prevent webhooks from validating or mutating other webhooks. Consider
  excluding specific namespaces
  from triggering your webhook.
* Prevent your webhooks from acting on dependent add-ons by using an
  `objectSelector`.

### Fail open and validate the final state {#fail-open-validate-final-state}

Mutating admission webhooks support the `failurePolicy` configuration field.
This field indicates whether the API server should admit or reject the request
if the webhook fails. Webhook failures might occur because of timeouts or errors
in the server logic.

By default, admission webhooks set the `failurePolicy` field to Fail. The API
server rejects a request if the webhook fails. However, rejecting requests by
default might result in compliant requests being rejected during webhook
downtime. 

Let your mutating webhooks "fail open" by setting the `failurePolicy` field to
Ignore. Use a validating controller to check the state of requests to ensure
that they comply with your policies. 

This approach has the following benefits:

* Mutating webhook downtime doesn't affect compliant resources from deploying.
* Policy enforcement occurs during validating admission control.
* Mutating webhooks don't interfere with other controllers in the cluster.

### Plan for future updates to fields {#plan-future-field-updates}

In general, design your webhooks under the assumption that Kubernetes APIs might
change in a later version. Don't write a server that takes the stability of an
API for granted. For example, the release of sidecar containers in Kubernetes
added a `restartPolicy` field to the Pod API. 

### Prevent your webhook from triggering itself {#prevent-webhook-self-trigger}

Mutating webhooks that respond to a broad range of API requests might
unintentionally trigger themselves. For example, consider a webhook that
responds to all requests in the cluster. If you configure the webhook to create
Event objects for every mutation, it'll respond to its own Event object
creation requests.

To avoid this, consider setting a unique label in any resources that your
webhook creates. Exclude this label from your webhook match conditions.

### Don't change immutable objects {#dont-change-immutable-objects}

Some Kubernetes objects in the API server can't change. For example, when you
deploy a static Pod, the
kubelet on the node creates a 
mirror Pod in the API
server to track the static Pod. However, changes to the mirror Pod don't
propagate to the static Pod. 

Don't attempt to mutate these objects during admission. All mirror Pods have the
`kubernetes.io/config.mirror` annotation. To exclude mirror Pods while reducing
the security risk of ignoring an annotation, allow static Pods to only run in
specific namespaces.
