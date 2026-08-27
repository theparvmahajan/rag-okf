---
id: okf-structure/tasks/configure-pod-container/enforce-standards-admission-controller.md#configure-the-admission-controller
kind: section
title: Configure the Admission Controller
source: tasks/configure-pod-container/enforce-standards-admission-controller.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/
heading: Configure the Admission Controller
parent: okf-structure/tasks/configure-pod-container/enforce-standards-admission-controller
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/enforce-standards-admission-controller.md#prerequisites
next_sibling: null
word_count: 134
---

`pod-security.admission.config.k8s.io/v1` configuration requires v1.25+.
For v1.23 and v1.24, use v1beta1.
For v1.22, use v1alpha1.

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: PodSecurity
  configuration:
    apiVersion: pod-security.admission.config.k8s.io/v1 # see compatibility note
    kind: PodSecurityConfiguration
    # Defaults applied when a mode label is not set.
    #
    # Level label values must be one of:
    # - "privileged" (default)
    # - "baseline"
    # - "restricted"
    #
    # Version label values must be one of:
    # - "latest" (default) 
    # - specific version like "v"
    defaults:
      enforce: "privileged"
      enforce-version: "latest"
      audit: "privileged"
      audit-version: "latest"
      warn: "privileged"
      warn-version: "latest"
    exemptions:
      # Array of authenticated usernames to exempt.
      usernames: []
      # Array of runtime class names to exempt.
      runtimeClasses: []
      # Array of namespaces to exempt.
      namespaces: []
```

The above manifest needs to be specified via the `--admission-control-config-file` to kube-apiserver.
