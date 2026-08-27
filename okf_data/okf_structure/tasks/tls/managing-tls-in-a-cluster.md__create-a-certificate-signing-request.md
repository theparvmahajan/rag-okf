---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#create-a-certificate-signing-request
kind: section
title: Create a certificate signing request
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Create a certificate signing request
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#requesting-a-certificate
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#create-a-certificatesigningrequest-object-to-send-to-the-kubernetes-api
word_count: 132
---

Generate a private key and certificate signing request (or CSR) by running
the following command:

```shell
cat <<EOF | cfssl genkey - | cfssljson -bare server
{
  "hosts": [
    "my-svc.my-namespace.svc.cluster.local",
    "my-pod.my-namespace.pod.cluster.local",
    "192.0.2.24",
    "10.0.34.2"
  ],
  "CN": "my-pod.my-namespace.pod.cluster.local",
  "key": {
    "algo": "ecdsa",
    "size": 256
  }
}
EOF
```

Where `192.0.2.24` is the service's cluster IP,
`my-svc.my-namespace.svc.cluster.local` is the service's DNS name,
`10.0.34.2` is the pod's IP and `my-pod.my-namespace.pod.cluster.local`
is the pod's DNS name. You should see output similar to:

```
2022/02/01 11:45:32 [INFO] generate received request
2022/02/01 11:45:32 [INFO] received CSR
2022/02/01 11:45:32 [INFO] generating key: ecdsa-256
2022/02/01 11:45:32 [INFO] encoded CSR
```

This command generates two files; it generates `server.csr` containing the PEM
encoded PKCS#10 certification request,
and `server-key.pem` containing the PEM encoded key to the certificate that
is still to be created.
