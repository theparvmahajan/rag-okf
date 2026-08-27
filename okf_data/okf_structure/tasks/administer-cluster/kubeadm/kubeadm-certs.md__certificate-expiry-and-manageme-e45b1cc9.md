---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#certificate-expiry-and-management-check-certificate-expiration
kind: section
title: Certificate expiry and management {#check-certificate-expiration}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Certificate expiry and management {#check-certificate-expiration}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#external-ca-mode-external-ca-mode
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#automatic-certificate-renewal
word_count: 307
---

`kubeadm` cannot manage certificates signed by an external CA.

You can use the `check-expiration` subcommand to check when certificates expire:

```shell
kubeadm certs check-expiration
```

The output is similar to this:

```console
CERTIFICATE                EXPIRES                  RESIDUAL TIME   CERTIFICATE AUTHORITY   EXTERNALLY MANAGED
admin.conf                 Dec 30, 2020 23:36 UTC   364d                                    no
apiserver                  Dec 30, 2020 23:36 UTC   364d            ca                      no
apiserver-etcd-client      Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
apiserver-kubelet-client   Dec 30, 2020 23:36 UTC   364d            ca                      no
controller-manager.conf    Dec 30, 2020 23:36 UTC   364d                                    no
etcd-healthcheck-client    Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
etcd-peer                  Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
etcd-server                Dec 30, 2020 23:36 UTC   364d            etcd-ca                 no
front-proxy-client         Dec 30, 2020 23:36 UTC   364d            front-proxy-ca          no
scheduler.conf             Dec 30, 2020 23:36 UTC   364d                                    no

CERTIFICATE AUTHORITY   EXPIRES                  RESIDUAL TIME   EXTERNALLY MANAGED
ca                      Dec 28, 2029 23:36 UTC   9y              no
etcd-ca                 Dec 28, 2029 23:36 UTC   9y              no
front-proxy-ca          Dec 28, 2029 23:36 UTC   9y              no
```

The command shows expiration/residual time for the client certificates in the
`/etc/kubernetes/pki` folder and for the client certificate embedded in the kubeconfig files used
by kubeadm (`admin.conf`, `controller-manager.conf` and `scheduler.conf`).

Additionally, kubeadm informs the user if the certificate is externally managed; in this case, the
user should take care of managing certificate renewal manually/using other tools.

The `kubelet.conf` configuration file is not included in the list above because kubeadm
configures kubelet
for automatic certificate renewal
with rotatable certificates under `/var/lib/kubelet/pki`.
To repair an expired kubelet client certificate see
Kubelet client certificate rotation fails.

On nodes created with `kubeadm init` from versions prior to kubeadm version 1.17, there is a
bug where you manually have to modify the
contents of `kubelet.conf`. After `kubeadm init` finishes, you should update `kubelet.conf` to
point to the rotated kubelet client certificates, by replacing `client-certificate-data` and
`client-key-data` with:

```yaml
client-certificate: /var/lib/kubelet/pki/kubelet-client-current.pem
client-key: /var/lib/kubelet/pki/kubelet-client-current.pem
```
