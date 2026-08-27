---
id: okf-structure/concepts/workloads/pods/advanced-pod-config.md#pod-and-container-level-security-context-configuration-security-context
kind: section
title: Pod and container level security context configuration {#security-context}
source: concepts/workloads/pods/advanced-pod-config.md
url: https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/
heading: Pod and container level security context configuration {#security-context}
parent: okf-structure/concepts/workloads/pods/advanced-pod-config
children: []
prev_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#runtimeclasses
next_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#influencing-pod-scheduling-decisions-scheduling
word_count: 282
---

The `Security context` field in the Pod specification provides granular control over security settings for Pods and containers.

### Pod-wide `securityContext` {#pod-level-security-context}

Some aspects of security apply to the whole Pod; for other aspects,
you might want to set a default, without any container-level overrides.

Here's an example of using `securityContext` at the Pod level:

#### Example Pod {#pod-level-security-context-example}

apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:  # This applies to the entire Pod
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  containers:
  - name: sec-ctx-demo
    image: registry.k8s.io/e2e-test-images/agnhost:2.45
    command: ["sh", "-c", "sleep 1h"]

### Container-level security context {#container-level-security-context}

You can specify the security context just for a specific container.
Here's an example:

#### Example Pod {#container-level-security-context-example}

apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo-2
spec:
  containers:
  - name: sec-ctx-demo-2
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      allowPrivilegeEscalation: false
      runAsNonRoot: true
      runAsUser: 1000
      capabilities:
        drop:
        - ALL
      seccompProfile:
        type: RuntimeDefault

### Security context options

- **User and Group IDs**: Control which user/group the container runs as
- **Capabilities**: Add or drop Linux capabilities
- **Seccomp Profiles**: Set security computing profiles
- **SELinux Options**: Configure SELinux context
- **AppArmor**: Configure AppArmor profiles for additional access control
- **Windows Options**: Configure Windows-specific security settings

You can also use the Pod `securityContext` to allow
_privileged mode_
in Linux containers. Privileged mode overrides many of the other security settings in the `securityContext`.
Avoid using this setting unless you can't grant the equivalent permissions by using other fields in the `securityContext`.
You can run Windows containers in a similarly
privileged mode by setting the `windowsOptions.hostProcess` flag on the
Pod-level security context. For details and instructions, see
Create a Windows HostProcess Pod.

For more information, see Configure a Security Context for a Pod or Container.
