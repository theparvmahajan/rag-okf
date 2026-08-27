---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-kubectl-helpers
kind: section
title: Verify kubectl helpers
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: Verify kubectl helpers
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#tls-problems
next_sibling: null
word_count: 59
---

Some kubectl authentication helpers provide easy access to Kubernetes clusters. If you
have used such helpers and are facing connectivity issues, ensure that the necessary
configurations are still present.

Check kubectl configuration for authentication details:

```shell
kubectl config view
```

If you previously used a helper tool (for example, `kubectl-oidc-login`), ensure that it is still
installed and configured correctly.
