---
id: okf-structure/concepts/storage/projected-volumes.md#podcertificate-projected-volumes-podcertificate
kind: section
title: podCertificate projected volumes {#podcertificate}
source: concepts/storage/projected-volumes.md
url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
heading: podCertificate projected volumes {#podcertificate}
parent: okf-structure/concepts/storage/projected-volumes
children: []
prev_sibling: okf-structure/concepts/storage/projected-volumes.md#clustertrustbundle-projected-volumes-clustertrustbundle
next_sibling: okf-structure/concepts/storage/projected-volumes.md#securitycontext-interactions
word_count: 486
---

In Kubernetes , you must enable support for Pod
Certificates using the `PodCertificateRequest` feature gate
and the `--runtime-config=certificates.k8s.io/v1beta1/podcertificaterequests=true`
kube-apiserver flag.

The `podCertificate` projected volumes source securely provisions a private key
and X.509 certificate chain for pod to use as client or server credentials.
Kubelet will then handle refreshing the private key and certificate chain when
they get close to expiration.  The application just has to make sure that it
reloads the file promptly when it changes, with a mechanism like `inotify` or
polling.

Each `podCertificate` projection supports the following configuration fields:
* `signerName`: The
  signer
  you want to issue the certificate.  Note that signers may have their own
  access requirements, and may refuse to issue certificates to your pod.
* `keyType`: The type of private key that should be generated.  Valid values are
  `ED25519`, `ECDSAP256`, `ECDSAP384`, `ECDSAP521`, `RSA3072`, and `RSA4096`.
* `maxExpirationSeconds`: The maximum lifetime you will accept for the
  certificate issued to the pod.  If not set, will be defaulted to `86400` (24
  hours).  Must be at least `3600` (1 hour), and at most `7862400` (91 days).
  Kubernetes built-in signers are restricted to a max lifetime of `86400` (1
  day). The signer is allowed to issue a certificate with a lifetime shorter
  than what you've specified.
* `credentialBundlePath`: Relative path within the projection where the
  credential bundle should be written.  The credential bundle is a PEM-formatted
  file, where the first block is a "PRIVATE KEY" block that contains a
  PKCS#8-serialized private key, and the remaining blocks are "CERTIFICATE"
  blocks that comprise the certificate chain (leaf certificate and any
  intermediates).
* `keyPath` and `certificateChainPath`: Separate paths where Kubelet should
  write *just* the private key or certificate chain.
* `userAnnotations`: a map that allows you to pass additional information to
  the signer implementation. It is copied verbatim into the
  `spec.unverifiedUserAnnotations` field of the
  PodCertificateRequest objects
  that Kubelet creates. Entries are subject to the same validation as object
  metadata annotations, with the addition that all keys must be domain-prefixed.
  No restrictions are placed on values, except an overall size limitation on the
  entire field. Other than these basic validations, the API server does not
  conduct any extra validations. The signer implementations should be very
  careful when consuming this data. Signers must not inherently trust this data
  without first performing the appropriate verification steps. Signers should
  document the keys and values they support. Signers should deny requests that
  contain keys they do not recognize.

Most applications should prefer using `credentialBundlePath` unless they need
the key and certificates in separate files for compatibility reasons. Kubelet
uses an atomic writing strategy based on symlinks to make sure that when you
open the files it projects, you read either the old content or the new content.
However, if you read the key and certificate chain from separate files, Kubelet
may rotate the credentials after your first read and before your second read,
resulting in your application loading a mismatched key and certificate.
