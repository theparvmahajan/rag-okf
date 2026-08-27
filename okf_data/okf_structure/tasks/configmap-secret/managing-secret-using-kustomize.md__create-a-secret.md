---
id: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#create-a-secret
kind: section
title: Create a Secret
source: tasks/configmap-secret/managing-secret-using-kustomize.md
url: https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/
heading: Create a Secret
parent: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize
children: []
prev_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#prerequisites
next_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#edit-a-secret-edit-secret
word_count: 318
---

You can generate a Secret by defining a `secretGenerator` in a
`kustomization.yaml` file that references other existing files, `.env` files, or
literal values. For example, the following instructions create a kustomization
file for the username `admin` and the password `1f2d1e2e67df`.

The `stringData` field for a Secret does not work well with server-side apply.

### Create the kustomization file

secretGenerator:
- name: database-creds
  literals:
  - username=admin
  - password=1f2d1e2e67df

1.  Store the credentials in files. The filenames are the keys of the secret:

    ```shell
    echo -n 'admin' > ./username.txt
    echo -n '1f2d1e2e67df' > ./password.txt
    ```
    The `-n` flag ensures that there's no newline character at the end of your
    files.

1.  Create the `kustomization.yaml` file:

    ```yaml
    secretGenerator:
    - name: database-creds
      files:
      - username.txt
      - password.txt
    ```

You can also define the secretGenerator in the `kustomization.yaml` file by
providing `.env` files. For example, the following `kustomization.yaml` file
pulls in data from an `.env.secret` file:

```yaml
secretGenerator:
- name: db-user-pass
  envs:
  - .env.secret
```

In all cases, you don't need to encode the values in base64. The name of the YAML
file **must** be `kustomization.yaml` or `kustomization.yml`.

### Apply the kustomization file

To create the Secret, apply the directory that contains the kustomization file:

```shell
kubectl apply -k <directory-path>
```

The output is similar to:

```
secret/database-creds-5hdh7hhgfk created
```

When a Secret is generated, the Secret name is created by hashing
the Secret data and appending the hash value to the name. This ensures that
a new Secret is generated each time the data is modified.

To verify that the Secret was created and to decode the Secret data,

```shell
kubectl get -k <directory-path> -o jsonpath='{.data}' 
```

The output is similar to:

```
{ "password": "MWYyZDFlMmU2N2Rm", "username": "YWRtaW4=" }
```

```
echo 'MWYyZDFlMmU2N2Rm' | base64 --decode
```

The output is similar to:

```
1f2d1e2e67df
```

For more information, refer to
Managing Secrets using kubectl and
Declarative Management of Kubernetes Objects Using Kustomize.
