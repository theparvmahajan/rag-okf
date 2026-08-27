---
id: okf-structure/concepts/workloads/pods/_index.md#pod-security-settings-pod-security
kind: section
title: Pod security settings {#pod-security}
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Pod security settings {#pod-security}
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#resource-sharing-and-communication
next_sibling: okf-structure/concepts/workloads/pods/_index.md#resource-requests-and-limits
word_count: 147
---

To set security constraints on Pods and containers, you use the
`securityContext` field in the Pod specification. This field gives you
granular control over what a Pod or individual containers can do. See Advanced Pod Configuration for more details.

For basic security configuration, you should meet the Baseline Pod security standard and run containers as non-root. You can set simple security contexts:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  containers:
  - name: sec-ctx-demo
    image: busybox
    command: ["sh", "-c", "sleep 1h"]
```

For advanced security context configuration including capabilities, seccomp profiles, and detailed security options, see the security concepts section.

* To learn about kernel-level security constraints that you can use,
  see Linux kernel security constraints for Pods and containers.
* To learn more about the Pod security context, see
  Configure a Security Context for a Pod or Container.
