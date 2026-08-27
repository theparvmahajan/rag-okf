---
id: okf-structure/tutorials/cluster-management/admission-policies.md#clean-up
kind: section
title: Clean up
source: tutorials/cluster-management/admission-policies.md
url: https://kubernetes.io/docs/tutorials/cluster-management/admission-policies/
heading: Clean up
parent: okf-structure/tutorials/cluster-management/admission-policies
children: []
prev_sibling: okf-structure/tutorials/cluster-management/admission-policies.md#modifying-resources-when-they-are-created-or-changed-mutation
next_sibling: null
word_count: 49
---

To remove the resources created, run the following commands:

```bash
kubectl delete validatingadmissionpolices/enforce-multiple-replicas-deployments \
               validatingadmissionpolicybindings/enforce-multiple-replicas-deployments

kubectl delete mutatingadmissionpolicies/default-pod-security-baseline \
               mutatingadmissionpolicybindings/default-pod-security-baseline

kubectl delete mutatingadmissionpolicies/default-pod-security-configurable \
               mutatingadmissionpolicybindings/default-pod-security-configurable

kubectl --namespace kube-system delete configmaps/default-pod-security-standard

kubectl delete namespaces/example namespaces/another-example namespaces/yet-another-example
```

If you created any test Pods or test Namespaces, clear those up too.
