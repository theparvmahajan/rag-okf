---
id: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#bases-and-overlays
kind: section
title: Bases and Overlays
source: tasks/manage-kubernetes-objects/kustomization.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
heading: Bases and Overlays
parent: okf-structure/tasks/manage-kubernetes-objects/kustomization
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#overview-of-kustomize
next_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#how-to-apply-view-delete-objects-using-kustomize
word_count: 269
---

Kustomize has the concepts of **bases** and **overlays**. A **base** is a directory with a `kustomization.yaml`, which contains a
set of resources and associated customization. A base could be either a local directory or a directory from a remote repo,
as long as a `kustomization.yaml` is present inside. An **overlay** is a directory with a `kustomization.yaml` that refers to other
kustomization directories as its `bases`. A **base** has no knowledge of an overlay and can be used in multiple overlays.

The `kustomization.yaml` in an **overlay** directory may refer to multiple `bases`, combining all the resources defined
in these bases into a unified configuration. Additionally, it can apply customizations on top of these resources to meet specific
requirements.

Here is an example of a base:

```shell
# Create a directory to hold the base
mkdir base
# Create a base/deployment.yaml
cat <<EOF > base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 2
  template:
    metadata:
      labels:
        run: my-nginx
    spec:
      containers:
      - name: my-nginx
        image: nginx
EOF

# Create a base/service.yaml file
cat <<EOF > base/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: my-nginx
EOF
# Create a base/kustomization.yaml
cat <<EOF > base/kustomization.yaml
resources:
- deployment.yaml
- service.yaml
EOF
```

This base can be used in multiple overlays. You can add different `namePrefix` or other cross-cutting fields
in different overlays. Here are two overlays using the same base.

```shell
mkdir dev
cat <<EOF > dev/kustomization.yaml
resources:
- ../base
namePrefix: dev-
EOF

mkdir prod
cat <<EOF > prod/kustomization.yaml
resources:
- ../base
namePrefix: prod-
EOF
```
