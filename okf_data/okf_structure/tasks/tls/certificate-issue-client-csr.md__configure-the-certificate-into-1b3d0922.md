---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#configure-the-certificate-into-kubeconfig
kind: section
title: Configure the certificate into kubeconfig
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Configure the certificate into kubeconfig
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#get-the-certificate
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-role-and-rolebinding
word_count: 62
---

The next step is to add this user to the kubeconfig file.

First, you need to add new credentials:

```shell
kubectl config set-credentials myuser --client-key=myuser.key --client-certificate=myuser.crt --embed-certs=true

```

Then, you need to add the context:

```shell
kubectl config set-context myuser --cluster=kubernetes --user=myuser
```

To test it:

```shell
kubectl --context myuser auth whoami
```

You should see output confirming that you are “myuser“.
