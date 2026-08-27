---
id: okf-structure/tasks/configmap-secret/managing-secret-using-config-file.md#edit-a-secret-edit-secret
kind: section
title: Edit a Secret {#edit-secret}
source: tasks/configmap-secret/managing-secret-using-config-file.md
url: https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/
heading: Edit a Secret {#edit-secret}
parent: okf-structure/tasks/configmap-secret/managing-secret-using-config-file
children: []
prev_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-config-file.md#create-the-secret-create-the-config-file
next_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-config-file.md#clean-up
word_count: 182
---

To edit the data in the Secret you created using a manifest, modify the `data`
or `stringData` field in your manifest and apply the file to your
cluster. You can edit an existing `Secret` object unless it is
immutable.

For example, if you want to change the password from the previous example to
`birdsarentreal`, do the following:

1. Encode the new password string:

   ```shell
   echo -n 'birdsarentreal' | base64
   ```

   The output is similar to:

   ```
   YmlyZHNhcmVudHJlYWw=
   ```

1. Update the `data` field with your new password string:

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: mysecret
   type: Opaque
   data:
     username: YWRtaW4=
     password: YmlyZHNhcmVudHJlYWw=
   ```

1. Apply the manifest to your cluster:

   ```shell
   kubectl apply -f ./secret.yaml
   ```

   The output is similar to:

   ```
   secret/mysecret configured
   ```

Kubernetes updates the existing `Secret` object. In detail, the `kubectl` tool
notices that there is an existing `Secret` object with the same name. `kubectl`
fetches the existing object, plans changes to it, and submits the changed
`Secret` object to your cluster control plane.

If you specified `kubectl apply --server-side` instead, `kubectl` uses
Server Side Apply instead.
