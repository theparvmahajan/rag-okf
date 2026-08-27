---
id: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubeadm/change-package-repository.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#switching-to-another-kubernetes-package-repository
word_count: 320
---

This document assumes that you're already using the community-owned
package repositories (`pkgs.k8s.io`). If that's not the case, it's strongly
recommended to migrate to the community-owned package repositories as described
in the official announcement.

### Verifying if the Kubernetes package repositories are used

If you're unsure whether you're using the community-owned package repositories or the
legacy package repositories, take the following steps to verify:

Print the contents of the file that defines the Kubernetes `apt` repository:

```shell
# On your system, this configuration file could have a different name
pager /etc/apt/sources.list.d/kubernetes.list
```

If you see a line similar to:

```
deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v/deb/ /
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the official announcement.

Print the contents of the file that defines the Kubernetes `yum` repository:

```shell
# On your system, this configuration file could have a different name
cat /etc/yum.repos.d/kubernetes.repo
```

If you see a `baseurl` similar to the `baseurl` in the output below:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the official announcement.

Print the contents of the file that defines the Kubernetes `zypper` repository:

```shell
# On your system, this configuration file could have a different name
cat /etc/zypp/repos.d/kubernetes.repo
```

If you see a `baseurl` similar to the `baseurl` in the output below:

```
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl
```

**You're using the Kubernetes package repositories and this guide applies to you.**
Otherwise, it's strongly recommended to migrate to the Kubernetes package repositories
as described in the official announcement.

The URL used for the Kubernetes package repositories is not limited to `pkgs.k8s.io`,
it can also be one of:

- `pkgs.k8s.io`
- `pkgs.kubernetes.io`
- `packages.kubernetes.io`
