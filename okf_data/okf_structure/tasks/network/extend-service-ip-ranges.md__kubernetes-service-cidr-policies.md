---
id: okf-structure/tasks/network/extend-service-ip-ranges.md#kubernetes-service-cidr-policies
kind: section
title: Kubernetes Service CIDR Policies
source: tasks/network/extend-service-ip-ranges.md
url: https://kubernetes.io/docs/tasks/network/extend-service-ip-ranges/
heading: Kubernetes Service CIDR Policies
parent: okf-structure/tasks/network/extend-service-ip-ranges
children: []
prev_sibling: okf-structure/tasks/network/extend-service-ip-ranges.md#extend-the-number-of-available-ips-for-services
next_sibling: null
word_count: 411
---

Cluster administrators can implement policies to control the creation and
modification of ServiceCIDR resources within the cluster. This allows for
centralized management of the IP address ranges used for Services and helps
prevent unintended or conflicting configurations. Kubernetes provides mechanisms
like Validating Admission Policies to enforce these rules.

### Preventing Unauthorized ServiceCIDR Creation/Update using Validating Admission Policy

There can be situations that the cluster administrators want to restrict the
ranges that can be allowed or to completely deny any changes to the cluster
Service IP ranges.

The default "kubernetes" ServiceCIDR is created by the kube-apiserver
to provide consistency in the cluster and is required for the cluster to work,
so it always must be allowed. You can ensure your `ValidatingAdmissionPolicy`
doesn't restrict the default ServiceCIDR by adding the clause:

```yaml
  matchConditions:
  - name: 'exclude-default-servicecidr'
    expression: "object.metadata.name != 'kubernetes'"
```

as in the examples below.

#### Restrict Service CIDR ranges to some specific ranges

The following is an example of a `ValidatingAdmissionPolicy` that only allows
ServiceCIDRs to be created if they are subranges of the given `allowed` ranges.
(So the example policy would allow a ServiceCIDR with `cidrs: ['10.96.1.0/24']`
or `cidrs: ['2001:db8:0:0:ffff::/80', '10.96.0.0/20']` but would not allow a
ServiceCIDR with `cidrs: ['172.20.0.0/16']`.) You can copy this policy and change
the value of `allowed` to something appropriate for you cluster.

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: "servicecidrs.default"
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
    - apiGroups:   ["networking.k8s.io"]
      apiVersions: ["v1"]
      operations:  ["CREATE", "UPDATE"]
      resources:   ["servicecidrs"]
  matchConditions:
  - name: 'exclude-default-servicecidr'
    expression: "object.metadata.name != 'kubernetes'"
  variables:
  - name: allowed
    expression: "['10.96.0.0/16','2001:db8::/64']"
  validations:
  - expression: "object.spec.cidrs.all(newCIDR, variables.allowed.exists(allowedCIDR, cidr(allowedCIDR).containsCIDR(newCIDR)))"
  # For all CIDRs (newCIDR) listed in the spec.cidrs of the submitted ServiceCIDR
  # object, check if there exists at least one CIDR (allowedCIDR) in the `allowed`
  # list of the VAP such that the allowedCIDR fully contains the newCIDR.
---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: "servicecidrs-binding"
spec:
  policyName: "servicecidrs.default"
  validationActions: [Deny,Audit]
```

Consult the CEL documentation
to learn more about CEL if you want to write your own validation `expression`.

#### Restrict any usage of the ServiceCIDR API

The following example demonstrates how to use a `ValidatingAdmissionPolicy` and
its binding to restrict the creation of any new Service CIDR ranges, excluding the default "kubernetes" ServiceCIDR:

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: "servicecidrs.deny"
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
    - apiGroups:   ["networking.k8s.io"]
      apiVersions: ["v1"]
      operations:  ["CREATE", "UPDATE"]
      resources:   ["servicecidrs"]
  validations:
  - expression: "object.metadata.name == 'kubernetes'"
---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: "servicecidrs-deny-binding"
spec:
  policyName: "servicecidrs.deny"
  validationActions: [Deny,Audit]
```
