---
id: okf-structure/concepts/security/security-checklist.md#images
kind: section
title: Images
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Images
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#secrets
next_sibling: okf-structure/concepts/security/security-checklist.md#admission-controllers
word_count: 359
---

- [ ] Minimize unnecessary content in container images.
- [ ] Container images are configured to be run as unprivileged user.
- [ ] References to container images are made by sha256 digests (rather than
tags) or the provenance of the image is validated by verifying the image's
digital signature at deploy time via admission control.
- [ ] Container images are regularly scanned during creation and in deployment, and
  known vulnerable software is patched.

Container image should contain the bare minimum to run the program they
package. Preferably, only the program and its dependencies, building the image
from the minimal possible base. In particular, image used in production should not
contain shells or debugging utilities, as an
ephemeral debug container
can be used for troubleshooting.

Build images to directly start with an unprivileged user by using the
`USER` instruction in Dockerfile.
The Security Context
allows a container image to be started with a specific user and group with
`runAsUser` and `runAsGroup`, even if not specified in the image manifest.
However, the file permissions in the image layers might make it impossible to just
start the process with a new unprivileged user without image modification.

Avoid using image tags to reference an image, especially the `latest` tag, the
image behind a tag can be easily modified in a registry. Prefer using the
complete `sha256` digest which is unique to the image manifest. This policy can be
enforced via an ImagePolicyWebhook.
Image signatures can also be automatically verified with an admission controller
at deploy time to validate their authenticity and integrity.

Scanning a container image can prevent critical vulnerabilities from being
deployed to the cluster alongside the container image. Image scanning should be
completed before deploying a container image to a cluster and is usually done
as part of the deployment process in a CI/CD pipeline. The purpose of an image
scan is to obtain information about possible vulnerabilities and their
prevention in the container image, such as a
Common Vulnerability Scoring System (CVSS)
score. If the result of the image scans is combined with the pipeline
compliance rules, only properly patched container images will end up in
Production.
