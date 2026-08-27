---
id: okf-structure/concepts/security/cloud-native-security.md#distribute-lifecycle-phase-lifecycle-phase-distribute
kind: section
title: _Distribute_ lifecycle phase {#lifecycle-phase-distribute}
source: concepts/security/cloud-native-security.md
url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
heading: _Distribute_ lifecycle phase {#lifecycle-phase-distribute}
parent: okf-structure/concepts/security/cloud-native-security
children: []
prev_sibling: okf-structure/concepts/security/cloud-native-security.md#develop-lifecycle-phase-lifecycle-phase-develop
next_sibling: okf-structure/concepts/security/cloud-native-security.md#deploy-lifecycle-phase-lifecycle-phase-deploy
word_count: 143
---

- Ensure the security of the supply chain for container images you execute.
- Ensure the security of the supply chain for the cluster and other components
  that execute your application. For example, this might include an external
  database that your cloud native application uses for persistence.

To achieve this, you can:

1. Scan container images and other artifacts for known vulnerabilities.
1. Ensure that software distribution uses encryption in transit, with
   a chain of trust for the software source.
1. Adopt and follow processes to update dependencies when updates are
   available, especially in response to security announcements.
1. Use validation mechanisms such as digital certificates for supply
   chain assurance.
1. Subscribe to feeds and other mechanisms to alert you to security
   risks.
1. Restrict access to artifacts. Place container images in a
   private registry
   that only allows authorized clients to pull images.
