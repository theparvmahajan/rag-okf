---
id: okf-structure/concepts/workloads/management.md#organizing-resource-configurations
kind: section
title: Organizing resource configurations
source: concepts/workloads/management.md
url: https://kubernetes.io/docs/concepts/workloads/management/
heading: Organizing resource configurations
parent: okf-structure/concepts/workloads/management
children: []
prev_sibling: okf-structure/concepts/workloads/management.md#introduction
next_sibling: okf-structure/concepts/workloads/management.md#bulk-operations-in-kubectl
word_count: 314
---

Many applications require multiple resources to be created, such as a Deployment along with a Service.
Management of multiple resources can be simplified by grouping them together in the same file
(separated by `---` in YAML). For example:

Multiple resources can be created the same way as a single resource:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx-app.yaml
```

```none
service/my-nginx-svc created
deployment.apps/my-nginx created
```

The resources will be created in the order they appear in the manifest. Therefore, it's best to
specify the Service first, since that will ensure the scheduler can spread the pods associated
with the Service as they are created by the controller(s), such as Deployment.

`kubectl apply` also accepts multiple `-f` arguments:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-svc.yaml \
  -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

It is a recommended practice to put resources related to the same microservice or application tier
into the same file, and to group all of the files associated with your application in the same
directory. If the tiers of your application bind to each other using DNS, you can deploy all of
the components of your stack together.

A URL can also be specified as a configuration source, which is handy for deploying directly from
manifests in your source control system:

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```none
deployment.apps/my-nginx created
```

If you need to define more manifests, such as adding a ConfigMap, you can do that too.

### External tools

This section lists only the most common tools used for managing workloads on Kubernetes. To see a larger list, view
Application definition and image build
in the CNCF Landscape.

#### Helm {#external-tool-helm}

Helm is a tool for managing packages of pre-configured
Kubernetes resources. These packages are known as _Helm charts_.

#### Kustomize {#external-tool-kustomize}

Kustomize traverses a Kubernetes manifest to add, remove or update configuration options.
It is available both as a standalone binary and as a native feature
of kubectl.
