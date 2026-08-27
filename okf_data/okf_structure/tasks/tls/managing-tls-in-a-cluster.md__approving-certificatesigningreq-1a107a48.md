---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#approving-certificatesigningrequests-approving-certificate-signing-requests
kind: section
title: Approving CertificateSigningRequests {#approving-certificate-signing-requests}
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Approving CertificateSigningRequests {#approving-certificate-signing-requests}
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#download-the-certificate-and-use-it
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#configuring-your-cluster-to-provide-signing
word_count: 257
---

A Kubernetes administrator (with appropriate permissions) can manually approve
(or deny) CertificateSigningRequests by using the `kubectl certificate
approve` and `kubectl certificate deny` commands. However if you intend
to make heavy usage of this API, you might consider writing an automated
certificates controller.

The ability to approve CSRs decides who trusts whom within your environment. The
ability to approve CSRs should not be granted broadly or lightly.

You should make sure that you confidently understand both the verification requirements
that fall on the approver **and** the repercussions of issuing a specific certificate
before you grant the `approve` permission.

Whether the approver is a machine or a human using kubectl as above, the role of the _approver_ is
to verify that the CSR satisfies two requirements:

1. The subject of the CSR controls the private key used to sign the CSR. This
   addresses the threat of a third party masquerading as an authorized subject.
   In the above example, this step would be to verify that the pod controls the
   private key used to generate the CSR.
2. The subject of the CSR is authorized to act in the requested context. This
   addresses the threat of an undesired subject joining the cluster. In the
   above example, this step would be to verify that the pod is allowed to
   participate in the requested service.

If and only if these two requirements are met, the approver should approve
the CSR and otherwise should deny the CSR.

For more information on certificate approval and access control, read
the Certificate Signing Requests
reference page.
