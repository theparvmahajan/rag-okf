---
id: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verify-the-software-bill-of-materials
kind: section
title: Verify the Software Bill Of Materials
source: tasks/administer-cluster/verify-signed-artifacts.md
url: https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/
heading: Verify the Software Bill Of Materials
parent: okf-structure/tasks/administer-cluster/verify-signed-artifacts
children: []
prev_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures-with-admission-controller
next_sibling: null
word_count: 103
---

You can verify the Kubernetes Software Bill of Materials (SBOM) by using the
sigstore certificate and signature, or the corresponding SHA files:

```shell
# Retrieve the latest available Kubernetes release version
VERSION=$(curl -Ls https://dl.k8s.io/release/stable.txt)

# Verify the SHA512 sum
curl -Ls "https://sbom.k8s.io/$VERSION/release" -o "$VERSION.spdx"
echo "$(curl -Ls "https://sbom.k8s.io/$VERSION/release.sha512") $VERSION.spdx" | sha512sum --check

# Verify the SHA256 sum
echo "$(curl -Ls "https://sbom.k8s.io/$VERSION/release.sha256") $VERSION.spdx" | sha256sum --check

# Retrieve sigstore signature and certificate
curl -Ls "https://sbom.k8s.io/$VERSION/release.sig" -o "$VERSION.spdx.sig"
curl -Ls "https://sbom.k8s.io/$VERSION/release.cert" -o "$VERSION.spdx.cert"

# Verify the sigstore signature
cosign verify-blob \
    --certificate "$VERSION.spdx.cert" \
    --signature "$VERSION.spdx.sig" \
    --certificate-identity krel-staging@k8s-releng-prod.iam.gserviceaccount.com \
    --certificate-oidc-issuer https://accounts.google.com \
    "$VERSION.spdx"
```
