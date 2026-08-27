---
id: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#switching-to-another-kubernetes-package-repository
kind: section
title: Switching to another Kubernetes package repository
source: tasks/administer-cluster/kubeadm/change-package-repository.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/change-package-repository/
heading: Switching to another Kubernetes package repository
parent: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/change-package-repository.md#whatsnext
word_count: 219
---

This step should be done upon upgrading from one to another Kubernetes minor
release in order to get access to the packages of the desired Kubernetes minor
version.

1. Open the file that defines the Kubernetes `apt` repository using a text editor of your choice:

   ```shell
   nano /etc/apt/sources.list.d/kubernetes.list
   ```

   You should see a single line with the URL that contains your current Kubernetes
   minor version. For example, if you're using v,
   you should see this:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v/deb/ /
   ```

1. Change the version in the URL to **the next available minor release**, for example:

   ```
   deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable://deb/ /
   ```

1. Save the file and exit your text editor. Continue following the relevant upgrade instructions.

1. Open the file that defines the Kubernetes `yum` repository using a text editor of your choice:

   ```shell
   nano /etc/yum.repos.d/kubernetes.repo
   ```

   You should see a file with two URLs that contain your current Kubernetes
   minor version. For example, if you're using v,
   you should see this:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable:/v/rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable:/v/rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```

1. Change the version in these URLs to **the next available minor release**, for example:

   ```
   [kubernetes]
   name=Kubernetes
   baseurl=https://pkgs.k8s.io/core:/stable://rpm/
   enabled=1
   gpgcheck=1
   gpgkey=https://pkgs.k8s.io/core:/stable://rpm/repodata/repomd.xml.key
   exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
   ```

1. Save the file and exit your text editor. Continue following the relevant upgrade instructions.
