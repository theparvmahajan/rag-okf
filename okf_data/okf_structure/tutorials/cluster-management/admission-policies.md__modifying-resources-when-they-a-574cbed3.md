---
id: okf-structure/tutorials/cluster-management/admission-policies.md#modifying-resources-when-they-are-created-or-changed-mutation
kind: section
title: Modifying resources when they are created or changed {#mutation}
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: Modifying resources when they are created or changed {#mutation}
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#enforcement-through-validation
next_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#clean-up
word_count: 610
---

For this example, imagine that you want to use Pod security admission
to ensure that namespaces, other than system namespaces, enforce a Pod security standard.

Similar to validation, you can create a MutatingAdmissionPolicy that can modify 
resources during admission. The API type that you need to modify is Namespace.

Here's a MutatingAdmissionPolicy that does some of this:

This policy sets a **default**. Someone with the ability to update a Namespace would be able to remove the
`pod-security.kubernetes.io/enforce` label from a namespace.

If you are not sure what this means, read through the Security documentation or
get external information security advice.

To apply that policy:

```shell
kubectl apply --server-side -f https://k8s.io/examples/access/manifest-admission-control/default-pod-security-baseline.yaml 
```

A MutatingAdmissionPolicyBinding is required to activate this policy; for example:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: default-pod-security-baseline
spec:
  # the name of the MutatingAdmissionPolicy to apply
  policyName: default-pod-security-baseline
```

### Test the policy {#test-admission-policy-mutation}

Try creating a new namespace named `example`:

```shell
kubectl create ns example
```

Examine its labels:
```shell
kubectl describe ns example
```

Even though you didn't specify a Pod security admission enforcement level, the label has been set.

Next, check whether you can find a way round the security settings.
Create a YAML manifest for a different Namespace:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: another-example
  labels:
    pod-security.kubernetes.io/enforce: privileged
```

You can create that namespace from the local manifest using `kubectl apply --server-side`. Does it work?

Yes, and the new namespace allows running privileged Pods.

This admission policy was **not** set up to validate or restrict. It provides a default value, but you can set
your own.
However, you can combine mutating admission with a validating admission policy as a way to enforce something,
but also make it easy to comply. (The tutorial doesn't explain this, but you can do it).

Providing a useful default means that when people don't set anything, they get a better outcome than just seeing
an error message. Imagine if you did have a validation rule to make sure that all namespaces had to enforce at
least the baseline standard. Anyone who didn't know about that rule might try to deploy something and immediately
see an error message when they try making a namespace.

### Use a parameter resource

Parameter resources allow a policy configuration to be separate from its definition.
A policy can define `paramKind`, which outlines the group, version, and kind (also known as GVK)
of the parameter resource. Then, a  policy binding ties that policy to the scope where it is bound,
as configured by a particular parameter resource.

Here is a sample MutatingAdmissionPolicyBinding:

```yaml
---
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingAdmissionPolicyBinding
metadata:
  name: default-pod-security-configurable
spec:
  # the name of the MutatingAdmissionPolicy to apply
  policyName: default-pod-security-configurable

  # parameters to use
  paramRef:
    # if the ConfigMap is missing or empty, don't set a default
    # (but do allow namespace creation)
    parameterNotFoundAction: Allow

    # where to find the parameter
    namespace: kube-system
    name: default-pod-security-standard
```

and here's a sample ConfigMap to put into the kube-system namespace:

```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: kube-system
  name: default-pod-security-standard
data:
  default: baseline # could also be "restricted"
```

Define both of those. You should **create the ConfigMap first**; the binding expects that the parameter
resource already exists (even if you plan to change it later).

Now, delete the previous MutatingAdmissionPolicyBinding:
```shell
kubectl delete mutatingadmissionpolicybindings/default-pod-security-baseline
```

and create a new namespace:
```shell
kubectl create ns yet-another-example
```

```shell
kubectl describe ns yet-another-example
```

Did the labels get defaulted?

### Change the parameter

```shell
# This starts an editor that lets you change .data.default for the parameter
kubectl --namespace kube-system edit configmap default-pod-security-standard
```

After you change it, try creating one more namespace. What happens?
