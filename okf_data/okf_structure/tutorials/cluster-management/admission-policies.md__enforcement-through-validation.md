---
id: okf-structure/tutorials/cluster-management/admission-policies.md#enforcement-through-validation
kind: section
title: Enforcement through validation
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: Enforcement through validation
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#what-are-declarative-admission-policies
next_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#modifying-resources-when-they-are-created-or-changed-mutation
word_count: 426
---

Now, try defining a ValidatingAdmissionPolicy.

The following is an example of a ValidatingAdmissionPolicy that requires that any Deployment has multiple replicas.

`spec.validations` contains CEL expressions which use the Common Expression Language (CEL)
to validate the request. 
If an expression evaluates to false, the validation check is enforced according to the `spec.failurePolicy` field.

Write a policy like this and apply it.

Or, if you want to apply a ready-made manifest:

```shell
kubectl apply --server-side -f https://k8s.io/examples/access/manifest-admission-control/vap-min-replicas.yaml
```

On its own, this doesn't do anything.

You can try creating a Deployment with 0 or 1 replicas; it will work (unless some other policy prevents it).

---

To make it work, you define a ValidatingAdmissionPolicyBinding.

Pick a namespace where you'll enforce the new policy.

The following is an example ValidatingAdmissionPolicyBinding for the policy you made:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: enforce-multiple-replicas-deployments-binding
spec:
  policyName: "enforce-multiple-replicas-deployments"
  validationActions: [Deny]
  matchResources:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: default # change this to match the namespace you're using
```

Anyone with full / admin access to a namespace can write to its labels. This includes deleting a label from
the namespace.

The `kubernetes.io/metadata.name` label is protected, but if you use a different label, take care to make sure
that only trusted users have a way to remove or edit that label you choose.

Write a manifest based on that example YAML (if you're using the `default` namespace, you can use
it without any changes). Apply that manifest using `kubectl apply`.

### Test the policy {#test-admission-policy-validation}

Now, test the policy. Try creating a Deployment
and then scale it to 0 replicas using `kubectl scale`. What happens?

You could change the ValidatingAdmissionPolicyBinding to have a different validation action,
instead of Deny. If you choose the Warning validation action and try to scale a Deployment to 0 replicas,
what happens?

If you did change the ValidatingAdmissionPolicyBinding to just warn people, there's a problem…

The name is wrong! If you change a ValidatingAdmissionPolicyBinding or the associated ValidatingAdmissionPolicy so
that it only warns people, you should check if you also need to change the name of the policy. You would change the
name to make sure that the naming doesn't mislead people.

### Existing resources aren't affected {#limitation-admission-policy-validation}

If you have a Deployment with 0 or 1 replicas, and you change the ValidatingAdmissionPolicyBinding back
to Deny mode, it doesn't affect any existing resources.

(If you wanted to try to scale out Deployments to have at least 2 replicas, you could achieve that another
way - for example, using a controller).

That's all for the ValidatingAdmissionPolicy. Now you'll learn about MutatingAdmissionPolicies.
