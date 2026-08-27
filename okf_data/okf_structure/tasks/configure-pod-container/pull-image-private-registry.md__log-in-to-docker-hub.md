---
id: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#log-in-to-docker-hub
kind: section
title: Log in to Docker Hub
source: tasks/configure-pod-container/pull-image-private-registry.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
heading: Log in to Docker Hub
parent: okf-structure/tasks/configure-pod-container/pull-image-private-registry
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-secret-based-on-existing-credentials-registry-secret-existing-credentials
word_count: 158
---

On your laptop, you must authenticate with a registry in order to pull a private image.

Use the `docker` tool to log in to Docker Hub. See the _log in_ section of
Docker ID accounts for more information.

```shell
docker login
```

When prompted, enter your Docker ID, and then the credential you want to use (access token,
or the password for your Docker ID).

The login process creates or updates a `config.json` file that holds an authorization token.
Review how Kubernetes interprets this file.

View the `config.json` file:

```shell
cat ~/.docker/config.json
```

The output contains a section similar to this:

```json
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "c3R...zE2"
        }
    }
}
```

If you use a Docker credentials store, you won't see that `auth` entry but a `credsStore` entry with the name of the store as value.
In that case, you can create a secret directly.
See Create a Secret by providing credentials on the command line.
