---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#add-imagepullsecrets-to-a-service-account
kind: section
title: Add ImagePullSecrets to a service account
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: Add ImagePullSecrets to a service account
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#manually-create-an-api-token-for-a-serviceaccount
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#serviceaccount-token-volume-projection
word_count: 267
---

First, create an imagePullSecret.
Next, verify it has been created. For example:

- Create an imagePullSecret, as described in
  Specifying ImagePullSecrets on a Pod.

  ```shell
  kubectl create secret docker-registry myregistrykey --docker-server=<registry name> \
          --docker-username=DUMMY_USERNAME --docker-password=DUMMY_DOCKER_PASSWORD \
          --docker-email=DUMMY_DOCKER_EMAIL
  ```

- Verify it has been created.

  ```shell
  kubectl get secrets myregistrykey
  ```

  The output is similar to this:

  ```
  NAME             TYPE                              DATA    AGE
  myregistrykey    kubernetes.io/.dockerconfigjson   1       1d
  ```

### Add image pull secret to service account

Next, modify the default service account for the namespace to use this Secret as an imagePullSecret.

```shell
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "myregistrykey"}]}'
```

You can achieve the same outcome by editing the object manually:

```shell
kubectl edit serviceaccount/default
```

The output of the `sa.yaml` file is similar to this:

Your selected text editor will open with a configuration looking something like this:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2021-07-07T22:02:39Z
  name: default
  namespace: default
  resourceVersion: "243024"
  uid: 052fb0f4-3d50-11e5-b066-42010af0d7b6
```

Using your editor, delete the line with key `resourceVersion`, add lines for
`imagePullSecrets:` and save it. Leave the `uid` value set the same as you found it.

After you made those changes, the edited ServiceAccount looks something like this:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: 2021-07-07T22:02:39Z
  name: default
  namespace: default
  uid: 052fb0f4-3d50-11e5-b066-42010af0d7b6
imagePullSecrets:
  - name: myregistrykey
```

### Verify that imagePullSecrets are set for new Pods

Now, when a new Pod is created in the current namespace and using the default
ServiceAccount, the new Pod has its `spec.imagePullSecrets` field set automatically:

```shell
kubectl run nginx --image=<registry name>/nginx --restart=Never
kubectl get pod nginx -o=jsonpath='{.spec.imagePullSecrets[0].name}{"\n"}'
```

The output is:

```
myregistrykey
```
