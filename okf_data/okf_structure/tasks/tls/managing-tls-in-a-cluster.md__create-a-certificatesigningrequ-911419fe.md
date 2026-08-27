---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#create-a-certificatesigningrequest-object-to-send-to-the-kubernetes-api
kind: section
title: Create a CertificateSigningRequest object to send to the Kubernetes API
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Create a CertificateSigningRequest object to send to the Kubernetes API
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#create-a-certificate-signing-request
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#get-the-certificatesigningrequest-approved-get-the-certificate-signing-request-approved
word_count: 183
---

Generate a CSR manifest (in YAML) and send it to the API server. You can do that by
running the following command:

```shell
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: my-svc.my-namespace
spec:
  request: $(cat server.csr | base64 | tr -d '\n')
  signerName: example.com/serving
  usages:
  - digital signature
  - key encipherment
  - server auth
EOF
```

Notice that the `server.csr` file created in step 1 is base64 encoded
and stashed in the `.spec.request` field. You are also requesting a
certificate with the "digital signature", "key encipherment", and "server
auth" key usages, signed by an example `example.com/serving` signer.
A specific `signerName` must be requested.
View documentation for supported signer names
for more information.

The CSR should now be visible in the API in a Pending state. You can see
it by running:

```shell
kubectl describe csr my-svc.my-namespace
```

```none
Name:                   my-svc.my-namespace
Labels:                 <none>
Annotations:            <none>
CreationTimestamp:      Tue, 01 Feb 2022 11:49:15 -0500
Requesting User:        yourname@example.com
Signer:                 example.com/serving
Status:                 Pending
Subject:
        Common Name:    my-pod.my-namespace.pod.cluster.local
        Serial Number:
Subject Alternative Names:
        DNS Names:      my-pod.my-namespace.pod.cluster.local
                        my-svc.my-namespace.svc.cluster.local
        IP Addresses:   192.0.2.24
                        10.0.34.2
Events: <none>
```
