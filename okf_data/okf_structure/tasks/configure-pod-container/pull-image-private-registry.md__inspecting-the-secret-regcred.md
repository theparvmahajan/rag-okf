---
id: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#inspecting-the-secret-regcred
kind: section
title: Inspecting the Secret `regcred`
source: tasks/configure-pod-container/pull-image-private-registry.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
heading: Inspecting the Secret `regcred`
parent: okf-structure/tasks/configure-pod-container/pull-image-private-registry
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-secret-by-providing-credentials-on-the-command-line
next_sibling: okf-structure/tasks/configure-pod-container/pull-image-private-registry.md#create-a-pod-that-uses-your-secret
word_count: 167
---

To understand the contents of the `regcred` Secret you created, start by viewing the Secret in YAML format:

```shell
kubectl get secret regcred --output=yaml
```

The output is similar to this:

```yaml
apiVersion: v1
kind: Secret
metadata:
  ...
  name: regcred
  ...
data:
  .dockerconfigjson: eyJodHRwczovL2luZGV4L ... J0QUl6RTIifX0=
type: kubernetes.io/dockerconfigjson
```

The value of the `.dockerconfigjson` field is a base64 representation of your Docker credentials.

To understand what is in the `.dockerconfigjson` field, convert the secret data to a
readable format:

```shell
kubectl get secret regcred --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode
```

The output is similar to this:

```json
{"auths":{"your.private.registry.example.com":{"username":"janedoe","password":"xxxxxxxxxxx","email":"jdoe@example.com","auth":"c3R...zE2"}}}
```

To understand what is in the `auth` field, convert the base64-encoded data to a readable format:

```shell
echo "c3R...zE2" | base64 --decode
```

The output, username and password concatenated with a `:`, is similar to this:

```none
janedoe:xxxxxxxxxxx
```

Notice that the Secret data contains the authorization token similar to your local `~/.docker/config.json` file.

You have successfully set your Docker credentials as a Secret called `regcred` in the cluster.
