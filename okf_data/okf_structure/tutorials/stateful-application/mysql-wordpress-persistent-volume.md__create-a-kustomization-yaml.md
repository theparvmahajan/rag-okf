---
id: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#create-a-kustomization-yaml
kind: section
title: Create a kustomization.yaml
source: tutorials/stateful-application/mysql-wordpress-persistent-volume.md
url: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
heading: Create a kustomization.yaml
parent: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume
children: []
prev_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#create-persistentvolumeclaims-and-persistentvolumes
next_sibling: okf-structure/tutorials/stateful-application/mysql-wordpress-persistent-volume.md#add-resource-configs-for-mysql-and-wordpress
word_count: 80
---

### Add a Secret generator

A Secret is an object that stores a piece
of sensitive data like a password or key. Since 1.14, `kubectl` supports the
management of Kubernetes objects using a kustomization file. You can create a Secret
by generators in `kustomization.yaml`.

Add a Secret generator in `kustomization.yaml` from the following command.
You will need to replace `YOUR_PASSWORD` with the password you want to use.

```shell
cat <<EOF >./kustomization.yaml
secretGenerator:
- name: mysql-pass
  literals:
  - password=YOUR_PASSWORD
EOF
```
