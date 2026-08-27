---
id: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-secret-by-providing-credentials-on-the-command-line
kind: section
title: Create a Secret by providing credentials on the command line
source: tasks/configure-pod-container/pull-image-private-registry.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
heading: Create a Secret by providing credentials on the command line
parent: okf-structure/tasks/configure-pod-container/pull-image-private-registry
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-secret-based-on-existing-credentials-registry-secret-existing-credentials
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#inspecting-the-secret-regcred
word_count: 97
---

Create this Secret, naming it `regcred`:

```shell
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```

where:

* `<your-registry-server>` is your Private Docker Registry FQDN.
  Use `https://index.docker.io/v1/` for DockerHub.
* `<your-name>` is your Docker username.
* `<your-pword>` is your Docker password.
* `<your-email>` is your Docker email.

You have successfully set your Docker credentials in the cluster as a Secret called `regcred`.

Typing secrets on the command line may store them in your shell history unprotected, and
those secrets might also be visible to other users on your PC during the time that
`kubectl` is running.
