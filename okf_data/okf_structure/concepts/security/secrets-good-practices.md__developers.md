---
id: okf-structure/concepts/security/secrets-good-practices.md#developers
kind: section
title: Developers
source: concepts/security/secrets-good-practices.md
url: https://kubernetes.io/docs/concepts/security/secrets-good-practices/
heading: Developers
parent: okf-structure/concepts/security/secrets-good-practices
children: []
prev_sibling: okf-structure/concepts/security/secrets-good-practices.md#good-practices-for-using-swap-memory
next_sibling: null
word_count: 172
---

This section provides good practices for developers to use to improve the
security of confidential data when building and deploying Kubernetes resources.

### Restrict Secret access to specific containers

If you are defining multiple containers in a Pod, and only one of those
containers needs access to a Secret, define the volume mount or environment
variable configuration so that the other containers do not have access to that
Secret.

### Protect Secret data after reading

Applications still need to protect the value of confidential information after
reading it from an environment variable or volume. For example, your
application must avoid logging the secret data in the clear or transmitting it
to an untrusted party.

### Avoid sharing Secret manifests

If you configure a Secret through a
manifest, with the secret
data encoded as base64, sharing this file or checking it in to a source
repository means the secret is available to everyone who can read the manifest.

Base64 encoding is _not_ an encryption method, it provides no additional
confidentiality over plain text.
