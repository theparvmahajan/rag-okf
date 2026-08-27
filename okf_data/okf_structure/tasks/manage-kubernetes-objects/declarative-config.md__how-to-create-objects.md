---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-create-objects
kind: section
title: How to create objects
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: How to create objects
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#overview
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-update-objects
word_count: 241
---

Use `kubectl apply` to create all objects, except those that already exist,
defined by configuration files in a specified directory:

```shell
kubectl apply -f <directory>
```

This sets the `kubectl.kubernetes.io/last-applied-configuration: '{...}'`
annotation on each object. The annotation contains the contents of the object
configuration file that was used to create the object.

Add the `-R` flag to recursively process directories.

Here's an example of an object configuration file:

Run `kubectl diff` to print the object that will be created:

```shell
kubectl diff -f https://k8s.io/examples/application/simple_deployment.yaml
```

`diff` uses server-side dry-run,
which needs to be enabled on `kube-apiserver`.

Since `diff` performs a server-side apply request in dry-run mode,
it requires granting `PATCH`, `CREATE`, and `UPDATE` permissions.
See Dry-Run Authorization
for details.

Create the object using `kubectl apply`:

```shell
kubectl apply -f https://k8s.io/examples/application/simple_deployment.yaml
```

Print the live configuration using `kubectl get`:

```shell
kubectl get -f https://k8s.io/examples/application/simple_deployment.yaml -o yaml
```

The output shows that the `kubectl.kubernetes.io/last-applied-configuration` annotation
was written to the live configuration, and it matches the configuration file:

```yaml
kind: Deployment
metadata:
  annotations:
    # ...
    # This is the json representation of simple_deployment.yaml
    # It was written by kubectl apply when the object was created
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment",
      "metadata":{"annotations":{},"name":"nginx-deployment","namespace":"default"},
      "spec":{"minReadySeconds":5,"selector":{"matchLabels":{"app":nginx}},"template":{"metadata":{"labels":{"app":"nginx"}},
      "spec":{"containers":[{"image":"nginx:1.14.2","name":"nginx",
      "ports":[{"containerPort":80}]}]}}}}
  # ...
spec:
  # ...
  minReadySeconds: 5
  selector:
    matchLabels:
      # ...
      app: nginx
  template:
    metadata:
      # ...
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        # ...
        name: nginx
        ports:
        - containerPort: 80
        # ...
      # ...
    # ...
  # ...
```
