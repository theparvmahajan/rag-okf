---
id: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-binary-signatures
kind: section
title: Verifying binary signatures
source: tasks/administer-cluster/verify-signed-artifacts.md
url: https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/
heading: Verifying binary signatures
parent: okf-structure/tasks/administer-cluster/verify-signed-artifacts
children: []
prev_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures
word_count: 117
---

The Kubernetes release process signs all binary artifacts (tarballs, SPDX files,
standalone binaries) by using cosign's keyless signing. To verify a particular
binary, retrieve it together with its signature and certificate:

```bash
URL=https://dl.k8s.io/release/v/bin/linux/amd64
BINARY=kubectl

FILES=(
    "$BINARY"
    "$BINARY.sig"
    "$BINARY.cert"
)

for FILE in "${FILES[@]}"; do
    curl -sSfL --retry 3 --retry-delay 3 "$URL/$FILE" -o "$FILE"
done
```

Then verify the blob by using `cosign verify-blob`:

```shell
cosign verify-blob "$BINARY" \
  --signature "$BINARY".sig \
  --certificate "$BINARY".cert \
  --certificate-identity krel-staging@k8s-releng-prod.iam.gserviceaccount.com \
  --certificate-oidc-issuer https://accounts.google.com
```

Cosign 2.0 requires the `--certificate-identity` and `--certificate-oidc-issuer` options.

To learn more about keyless signing, please refer to Keyless Signatures.

Previous versions of Cosign required that you set `COSIGN_EXPERIMENTAL=1`.

For additional information, please refer to the sigstore Blog
