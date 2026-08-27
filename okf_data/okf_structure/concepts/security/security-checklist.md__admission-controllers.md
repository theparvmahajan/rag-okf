---
id: okf-structure/concepts/security/security-checklist.md#admission-controllers
kind: section
title: Admission controllers
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Admission controllers
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#images
next_sibling: okf-structure/concepts/security/security-checklist.md#what-s-next
word_count: 398
---

- [ ] An appropriate selection of admission controllers is enabled.
- [ ] A pod security policy is enforced by the Pod Security Admission or/and a
  webhook admission controller.
- [ ] The admission chain plugins and webhooks are securely configured.

Admission controllers can help improve the security of the cluster. However,
they can present risks themselves as they extend the API server and
should be properly secured.

The following lists present a number of admission controllers that could be
considered to enhance the security posture of your cluster and application. It
includes controllers that may be referenced in other parts of this document.

This first group of admission controllers includes plugins
enabled by default,
consider to leave them enabled unless you know what you are doing:

`CertificateApproval`
: Performs additional authorization checks to ensure the approving user has
permission to approve certificate request.

`CertificateSigning`
: Performs additional authorization checks to ensure the signing user has
permission to sign certificate requests.

`CertificateSubjectRestriction`
: Rejects any certificate request that specifies a 'group' (or 'organization
attribute') of `system:masters`.

`LimitRanger`
: Enforces the LimitRange API constraints.

`MutatingAdmissionWebhook`
: Allows the use of custom controllers through webhooks, these controllers may
mutate requests that they review.

`PodSecurity`
: Replacement for Pod Security Policy, restricts security contexts of deployed
Pods.

`ResourceQuota`
: Enforces resource quotas to prevent over-usage of resources.

`ValidatingAdmissionWebhook`
: Allows the use of custom controllers through webhooks, these controllers do
not mutate requests that it reviews.

The second group includes plugins that are not enabled by default but are in general
availability state and are recommended to improve your security posture:

`DenyServiceExternalIPs`
: Rejects all net-new usage of the `Service.spec.externalIPs` field. This is a mitigation for
CVE-2020-8554: Man in the middle using LoadBalancer or ExternalIPs.

`NodeRestriction`
: Restricts kubelet's permissions to only modify the pods API resources they own
or the node API resource that represent themselves. It also prevents kubelet
from using the `node-restriction.kubernetes.io/` annotation, which can be used
by an attacker with access to the kubelet's credentials to influence pod
placement to the controlled node.

The third group includes plugins that are not enabled by default but could be
considered for certain use cases:

`AlwaysPullImages`
: Enforces the usage of the latest version of a tagged image and ensures that the deployer
has permissions to use the image.

`ImagePolicyWebhook`
: Allows enforcing additional controls for images through webhooks.
