---
id: okf-structure/concepts/security/cloud-native-security.md#deploy-lifecycle-phase-lifecycle-phase-deploy
kind: section
title: _Deploy_ lifecycle phase {#lifecycle-phase-deploy}
source: concepts/security/cloud-native-security.md
url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
heading: _Deploy_ lifecycle phase {#lifecycle-phase-deploy}
parent: okf-structure/concepts/security/cloud-native-security
children: []
prev_sibling: okf-structure/concepts/security/cloud-native-security.md#distribute-lifecycle-phase-lifecycle-phase-distribute
next_sibling: okf-structure/concepts/security/cloud-native-security.md#runtime-lifecycle-phase-lifecycle-phase-runtime
word_count: 91
---

Ensure appropriate restrictions on what can be deployed, who can deploy it,
and where it can be deployed.
You can enforce measures from the _distribute_ phase, such as verifying the
cryptographic identity of container image artifacts.

You can deploy different applications and cluster components into different
namespaces. Containers
and namespaces both provide isolation mechanisms that are relevant to
information security.

When you deploy Kubernetes, you also set the foundation for your
applications' runtime environment: a Kubernetes cluster (or
multiple clusters).
That infrastructure must provide the security guarantees that higher
layers expect.
