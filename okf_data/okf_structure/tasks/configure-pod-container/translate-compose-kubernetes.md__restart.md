---
id: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#restart
kind: section
title: Restart
source: tasks/configure-pod-container/translate-compose-kubernetes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
heading: Restart
parent: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#labels
next_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#docker-compose-versions
word_count: 216
---

If you want to create normal pods without controllers you can use `restart` construct of docker-compose to define that. Follow table below to see what happens on the `restart` value.

| `docker-compose` `restart` | object created    | Pod `restartPolicy` |
|----------------------------|-------------------|---------------------|
| `""`                       | controller object | `Always`            |
| `always`                   | controller object | `Always`            |
| `on-failure`               | Pod               | `OnFailure`         |
| `no`                       | Pod               | `Never`             |

The controller object could be `deployment` or `replicationcontroller`.

For example, the `pival` service will become pod down here. This container calculated value of `pi`.

```yaml
version: '2'

services:
  pival:
    image: perl
    command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
    restart: "on-failure"
```

### Warning about Deployment Configurations

If the Docker Compose file has a volume specified for a service, the Deployment (Kubernetes) or DeploymentConfig (OpenShift) strategy is changed to "Recreate" instead of "RollingUpdate" (default). This is done to avoid multiple instances of a service from accessing a volume at the same time.

If the Docker Compose file has service name with `_` in it (for example, `web_service`), then it will be replaced by `-` and the service name will be renamed accordingly (for example, `web-service`). Kompose does this because "Kubernetes" doesn't allow `_` in object name.

Please note that changing service name might break some `docker-compose` files.
