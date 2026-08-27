---
id: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#labels
kind: section
title: Labels
source: tasks/configure-pod-container/translate-compose-kubernetes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
heading: Labels
parent: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#alternative-conversions
next_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#restart
word_count: 204
---

`kompose` supports Kompose-specific labels within the `docker-compose.yml` file in order to explicitly define a service's behavior upon conversion.

- `kompose.service.type` defines the type of service to be created.

  For example:

  ```yaml
  version: "2"
  services:
    nginx:
      image: nginx
      dockerfile: foobar
      build: ./foobar
      cap_add:
        - ALL
      container_name: foobar
      labels:
        kompose.service.type: nodeport
  ```

- `kompose.service.expose` defines if the service needs to be made accessible from outside the cluster or not. If the value is set to "true", the provider sets the endpoint automatically, and for any other value, the value is set as the hostname. If multiple ports are defined in a service, the first one is chosen to be the exposed.
  - For the Kubernetes provider, an ingress resource is created and it is assumed that an ingress controller has already been configured.
  - For the OpenShift provider, a route is created.

  For example:

  ```yaml
  version: "2"
  services:
    web:
      image: tuna/docker-counter23
      ports:
      - "5000:5000"
      links:
      - redis
      labels:
        kompose.service.expose: "counter.example.com"
    redis:
      image: redis:3.0
      ports:
      - "6379"
  ```

The currently supported options are:

| Key                  | Value                               |
|----------------------|-------------------------------------|
| kompose.service.type | nodeport / clusterip / loadbalancer |
| kompose.service.expose| true / hostname |

The `kompose.service.type` label should be defined with `ports` only, otherwise `kompose` will fail.
