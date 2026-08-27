---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#sign-the-certificatesigningrequest-sign-the-certificate-signing-request
kind: section
title: Sign the CertificateSigningRequest {#sign-the-certificate-signing-request}
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Sign the CertificateSigningRequest {#sign-the-certificate-signing-request}
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#get-the-certificatesigningrequest-approved-get-the-certificate-signing-request-approved
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#download-the-certificate-and-use-it
word_count: 363
---

Next, you'll play the part of a certificate signer, issue the certificate, and upload it to the API.

A signer would typically watch the CertificateSigningRequest API for objects with its `signerName`,
check that they have been approved, sign certificates for those requests,
and update the API object status with the issued certificate.

### Create a Certificate Authority

You need an authority to provide the digital signature on the new certificate.

First, create a signing certificate by running the following:

```shell
cat <<EOF | cfssl gencert -initca - | cfssljson -bare ca
{
  "CN": "My Example Signer",
  "key": {
    "algo": "rsa",
    "size": 2048
  }
}
EOF
```

You should see output similar to:

```none
2022/02/01 11:50:39 [INFO] generating a new CA key and certificate from CSR
2022/02/01 11:50:39 [INFO] generate received request
2022/02/01 11:50:39 [INFO] received CSR
2022/02/01 11:50:39 [INFO] generating key: rsa-2048
2022/02/01 11:50:39 [INFO] encoded CSR
2022/02/01 11:50:39 [INFO] signed certificate with serial number 263983151013686720899716354349605500797834580472
```

This produces a certificate authority key file (`ca-key.pem`) and certificate (`ca.pem`).

### Issue a certificate

Use a `server-signing-config.json` signing configuration and the certificate authority key file 
and certificate to sign the certificate request:

```shell
kubectl get csr my-svc.my-namespace -o jsonpath='{.spec.request}' | \
  base64 --decode | \
  cfssl sign -ca ca.pem -ca-key ca-key.pem -config server-signing-config.json - | \
  cfssljson -bare ca-signed-server
```

You should see the output similar to:

```
2022/02/01 11:52:26 [INFO] signed certificate with serial number 576048928624926584381415936700914530534472870337
```

This produces a signed serving certificate file, `ca-signed-server.pem`.

### Upload the signed certificate

Finally, populate the signed certificate in the API object's status:

```shell
kubectl get csr my-svc.my-namespace -o json | \
  jq '.status.certificate = "'$(base64 ca-signed-server.pem | tr -d '\n')'"' | \
  kubectl replace --raw /apis/certificates.k8s.io/v1/certificatesigningrequests/my-svc.my-namespace/status -f -
```

This uses the command line tool `jq` to populate the base64-encoded
content in the `.status.certificate` field.
If you do not have `jq`, you can also save the JSON output to a file, populate this field manually, and
upload the resulting file.

Once the CSR is approved and the signed certificate is uploaded, run:

```shell
kubectl get csr
```

The output is similar to:
```none
NAME                  AGE   SIGNERNAME            REQUESTOR              REQUESTEDDURATION   CONDITION
my-svc.my-namespace   20m   example.com/serving   yourname@example.com   <none>              Approved,Issued
```
