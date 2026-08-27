---
id: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures
kind: section
title: Verifying image signatures
source: tasks/administer-cluster/verify-signed-artifacts.md
url: https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/
heading: Verifying image signatures
parent: okf-structure/tasks/administer-cluster/verify-signed-artifacts
children: []
prev_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-binary-signatures
next_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures-with-admission-controller
word_count: 160
---

For a complete list of images that are signed please refer
to Releases.

Pick one image from this list and verify its signature using
the `cosign verify` command:

```shell
cosign verify registry.k8s.io/kube-apiserver-amd64:v \
  --certificate-identity krel-trust@k8s-releng-prod.iam.gserviceaccount.com \
  --certificate-oidc-issuer https://accounts.google.com \
  | jq .
```

### Verifying images for all control plane components

To verify all signed control plane images for the latest stable version
(v), please run the following commands:

```shell
curl -Ls "https://sbom.k8s.io/$(curl -Ls https://dl.k8s.io/release/stable.txt)/release" \
  | grep "SPDXID: SPDXRef-Package-registry.k8s.io" \
  | grep -v sha256 | cut -d- -f3- | sed 's/-/\//' | sed 's/-v1/:v1/' \
  | sort > images.txt
input=images.txt
while IFS= read -r image
do
  cosign verify "$image" \
    --certificate-identity krel-trust@k8s-releng-prod.iam.gserviceaccount.com \
    --certificate-oidc-issuer https://accounts.google.com \
    | jq .
done < "$input"
```

Once you have verified an image, you can specify the image by its digest in your Pod
manifests as per this example:

```console
registry-url/image-name@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2
```

For more information, please refer
to the Image Pull Policy
section.
