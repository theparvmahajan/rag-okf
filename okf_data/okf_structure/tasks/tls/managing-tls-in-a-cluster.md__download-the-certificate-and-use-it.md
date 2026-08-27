---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#download-the-certificate-and-use-it
kind: section
title: Download the certificate and use it
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Download the certificate and use it
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#sign-the-certificatesigningrequest-sign-the-certificate-signing-request
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#approving-certificatesigningrequests-approving-certificate-signing-requests
word_count: 111
---

Now, as the requesting user, you can download the issued certificate
and save it to a `server.crt` file by running the following:

```shell
kubectl get csr my-svc.my-namespace -o jsonpath='{.status.certificate}' \
    | base64 --decode > server.crt
```

Now you can populate `server.crt` and `server-key.pem` in a
Secret
that you could later mount into a Pod (for example, to use with a webserver
that serves HTTPS).

```shell
kubectl create secret tls server --cert server.crt --key server-key.pem
```

```none
secret/server created
```

Finally, you can store `ca.pem` in a ConfigMap
and use it as the trust root to verify the serving certificate:

```shell
kubectl create configmap example-serving-ca --from-file ca.crt=ca.pem
```

```none
configmap/example-serving-ca created
```
