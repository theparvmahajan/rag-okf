---
id: okf-structure/concepts/architecture/self-healing.md#considerations-considerations
kind: section
title: Considerations {#considerations}
source: concepts/architecture/self-healing.md
url: https://kubernetes.io/docs/concepts/architecture/self-healing/
heading: Considerations {#considerations}
parent: okf-structure/concepts/architecture/self-healing
children: []
prev_sibling: okf-structure/concepts/architecture/self-healing.md#self-healing-capabilities-self-healing-capabilities
next_sibling: okf-structure/concepts/architecture/self-healing.md#whatsnext
word_count: 29
---

- **Storage Failures:** If a persistent volume becomes unavailable, recovery steps may be required.

- **Application Errors:** Kubernetes can restart containers, but underlying application issues must be addressed separately.
