---
id: okf-structure/tutorials/cluster-management/admission-policies.md#what-are-declarative-admission-policies
kind: section
title: What are declarative admission policies?
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: What are declarative admission policies?
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#prerequisites
next_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#enforcement-through-validation
word_count: 492
---

Declarative admission policies offer a declarative, 
in-process alternative to admission webhooks.

By using the Common Expression Language (CEL) to declare policy rules,
these policies are evaluated directly within the API server.

These policies are highly configurable, enabling policy authors to define logic that can be parameterized
and scoped to resources as needed by cluster administrators.

### API types for admission policies

The two types of policy have different purposes.

ValidatingAdmissionPolicy is for _enforcing constraints_.

MutatingAdmissionPolicy is for _modifying resources during admission_.

### Policy elements

Each applied policy always has a _policy_ object (ValidatingAdmissionPolicy or MutatingAdmissionPolicy)
and a separate _binding_ object (ValidatingAdmissionPolicyBinding or MutatingAdmissionPolicyBinding).

You can also use _parameters_, which are **optional**. To learn more, see
parameter resources (ValidatingAdmissionPolicy) or
parameter resources (MutatingAdmissionPolicy).

Policy objects describes the abstract logic of a policy using Common Expression Language (CEL). 
For example, a ValidatingAdmissionPolicy might enforce replica limits or ensure specific labels are present, 
while a MutatingAdmissionPolicy can modify resources such as adding a default label to a namespace.

Binding objects link the policy to your cluster and provides scoping. 
A ValidatingAdmissionPolicyBinding or MutatingAdmissionPolicyBinding connects the policy to specific resources. 
If you only want to enforce a policy for a specific subset of resources, the binding is where you narrow the
scope of the policy (using `matchResources`).

Parameters allow separating configuration for the policy behavior from its definition.
Parameter resources refer to Kubernetes resources available in the API. 
They can be built-in API types (such as ConfigMap), or they can be
custom resources.
A policy binding then uses `spec.paramRef` to reference an actual parameter resource. 

If a policy does not require parameters, you leave `spec.paramKind` unspecified.

### CEL expressions

Both kinds of policy rely on an expression language known as Common Expression Language (CEL).
Read CEL in Kubernetes to learn more.

If you are new to CEL, practice writing a very simple expression, such as `false || true`.
You can test CEL expressions in CEL Playground.

### Policy actions

Each admission policy binding must specify one or more actions to declare how the policy
is enforced.

#### ValidatingAdmissionPolicyBinding {#policy-actions-validating}

For ValidatingAdmissionPolicyBinding, the supported `validationActions` are:

Audit
: Validation failure is included in the audit event for the API request.

Warn
: Validation failure is reported to the request client as a
  warning.

Deny
: Validation failure results in a denied request.

A policy check that fails or an error that occurs is enforced according to these actions.
Failures defined by the `failurePolicy` are enforced according to these actions only if the `failurePolicy`
is set to `Fail` (or not specified).

See Audit Annotations: validation failures
for more details about audit logging for policies.

You are not allowed to use Deny and Warn together, since this combination would duplicate
the validation failure in both the API response body and the HTTP `Warning:` header.

#### MutatingAdmissionPolicyBinding {#policy-actions-mutating}

For MutatingAdmissionPolicyBinding, the the action is always to mutate the object.

You can use a JSON Patch or a Kubernetes _apply configuration_.
