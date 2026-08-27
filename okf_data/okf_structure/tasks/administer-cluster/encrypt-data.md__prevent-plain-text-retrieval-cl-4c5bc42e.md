---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#prevent-plain-text-retrieval-cleanup-all-secrets-encrypted
kind: section
title: Prevent plain text retrieval {#cleanup-all-secrets-encrypted}
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Prevent plain text retrieval {#cleanup-all-secrets-encrypted}
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#encrypt-your-data-encrypting-your-data
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#rotate-a-decryption-key-rotating-a-decryption-key
word_count: 178
---

If you want to make sure that the only access to a particular API kind is done using
encryption, you can remove the API server's ability to read that API's backing data
as plaintext.

Making this change prevents the API server from retrieving resources that are marked
as encrypted at rest, but are actually stored in the clear.

When you have configured encryption at rest for an API (for example: the API kind
`Secret`, representing `secrets` resources in the core API group), you **must** ensure
that all those resources in this cluster really are encrypted at rest. Check this before
you carry on with the next steps.

Once all Secrets in your cluster are encrypted, you can remove the `identity`
part of the encryption configuration. For example:

---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: <BASE 64 ENCODED SECRET>
      - identity: {} # REMOVE THIS LINE

…and then restart each API server in turn. This change prevents the API server
from accessing a plain-text Secret, even by accident.
