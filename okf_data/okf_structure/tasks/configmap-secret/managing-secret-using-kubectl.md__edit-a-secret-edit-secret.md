---
id: okf-structure/tasks/configmap-secret/managing-secret-using-kubectl.md#edit-a-secret-edit-secret
kind: section
title: Edit a Secret {#edit-secret}
source: tasks/configmap-secret/managing-secret-using-kubectl.md
url: https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/
heading: Edit a Secret {#edit-secret}
parent: okf-structure/tasks/configmap-secret/managing-secret-using-kubectl
children: []
prev_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kubectl.md#create-a-secret
next_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kubectl.md#clean-up
word_count: 115
---

You can edit an existing `Secret` object unless it is
immutable. To edit a
Secret, run the following command:

```shell
kubectl edit secrets <secret-name>
```

This opens your default editor and allows you to update the base64 encoded
Secret values in the `data` field, such as in the following example:

```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file, it will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  password: UyFCXCpkJHpEc2I9
  username: YWRtaW4=
kind: Secret
metadata:
  creationTimestamp: "2022-06-28T17:44:13Z"
  name: db-user-pass
  namespace: default
  resourceVersion: "12708504"
  uid: 91becd59-78fa-4c85-823f-6d44436242ac
type: Opaque
```
