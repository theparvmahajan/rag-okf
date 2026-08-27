---
id: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#edit-a-secret-edit-secret
kind: section
title: Edit a Secret {#edit-secret}
source: tasks/configmap-secret/managing-secret-using-kustomize.md
url: https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/
heading: Edit a Secret {#edit-secret}
parent: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize
children: []
prev_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#create-a-secret
next_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#clean-up
word_count: 65
---

1.  In your `kustomization.yaml` file, modify the data, such as the `password`.
1.  Apply the directory that contains the kustomization file:

    ```shell
    kubectl apply -k <directory-path>
    ```

    The output is similar to:

    ```
    secret/db-user-pass-6f24b56cc8 created
    ```

The edited Secret is created as a new `Secret` object, instead of updating the
existing `Secret` object. You might need to update references to the Secret in
your Pods.
