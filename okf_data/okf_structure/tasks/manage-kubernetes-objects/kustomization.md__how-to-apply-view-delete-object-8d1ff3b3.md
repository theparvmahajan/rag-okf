---
id: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#how-to-apply-view-delete-objects-using-kustomize
kind: section
title: How to apply/view/delete objects using Kustomize
source: tasks/manage-kubernetes-objects/kustomization.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
heading: How to apply/view/delete objects using Kustomize
parent: okf-structure/tasks/manage-kubernetes-objects/kustomization
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#bases-and-overlays
next_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#kustomize-feature-list
word_count: 190
---

Use `--kustomize` or `-k` in `kubectl` commands to recognize resources managed by `kustomization.yaml`.
Note that `-k` should point to a kustomization directory, such as

```shell
kubectl apply -k <kustomization directory>/
```

Given the following `kustomization.yaml`,

```shell
# Create a deployment.yaml file
cat <<EOF > deployment.yaml
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
        ports:
        - containerPort: 80
EOF

# Create a kustomization.yaml
cat <<EOF >./kustomization.yaml
namePrefix: dev-
labels:
  - pairs:
      app: my-nginx
    includeSelectors: true 
resources:
- deployment.yaml
EOF
```

Run the following command to apply the Deployment object `dev-my-nginx`:

```shell
> kubectl apply -k ./
deployment.apps/dev-my-nginx created
```

Run one of the following commands to view the Deployment object `dev-my-nginx`:

```shell
kubectl get -k ./
```

```shell
kubectl describe -k ./
```

Run the following command to compare the Deployment object `dev-my-nginx` against the state
that the cluster would be in if the manifest was applied:

```shell
kubectl diff -k ./
```

Run the following command to delete the Deployment object `dev-my-nginx`:

```shell
> kubectl delete -k ./
deployment.apps "dev-my-nginx" deleted
```
