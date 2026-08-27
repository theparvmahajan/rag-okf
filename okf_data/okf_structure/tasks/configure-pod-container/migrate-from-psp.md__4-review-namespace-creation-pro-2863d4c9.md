---
id: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#4-review-namespace-creation-processes-review-namespace-creation-process
kind: section
title: 4. Review namespace creation processes {#review-namespace-creation-process}
source: tasks/configure-pod-container/migrate-from-psp.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/migrate-from-psp/
heading: 4. Review namespace creation processes {#review-namespace-creation-process}
parent: okf-structure/tasks/configure-pod-container/migrate-from-psp
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#3-update-namespaces-update-namespaces
next_sibling: okf-structure/tasks/configure-pod-container/migrate-from-psp.md#5-disable-podsecuritypolicy-disable-psp
word_count: 69
---

Now that existing namespaces have been updated to enforce Pod Security Admission, you should ensure
that your processes and/or policies for creating new namespaces are updated to ensure that an
appropriate Pod Security profile is applied to new namespaces.

You can also statically configure the Pod Security admission controller to set a default enforce,
audit, and/or warn level for unlabeled namespaces. See
Configure the Admission Controller
for more information.
