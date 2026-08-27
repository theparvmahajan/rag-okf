---
id: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#summary
kind: section
title: Summary
source: tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/
heading: Summary
parent: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#use-strategic-merge-patch-to-update-a-deployment-using-the-retainkeys-strategy
next_sibling: okf-structure/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch.md#whatsnext
word_count: 59
---

In this exercise, you used `kubectl patch` to change the live configuration
of a Deployment object. You did not change the configuration file that you originally used to
create the Deployment object. Other commands for updating API objects include
kubectl annotate,
kubectl edit,
kubectl replace,
kubectl scale,
and
kubectl apply.

Strategic merge patch is not supported for custom resources.
