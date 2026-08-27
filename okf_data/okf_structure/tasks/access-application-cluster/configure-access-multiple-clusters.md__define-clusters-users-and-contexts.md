---
id: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#define-clusters-users-and-contexts
kind: section
title: Define clusters, users, and contexts
source: tasks/access-application-cluster/configure-access-multiple-clusters.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/
heading: Define clusters, users, and contexts
parent: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#prerequisites
next_sibling: okf-structure/tasks/access-application-cluster/configure-access-multiple-clusters.md#create-a-second-configuration-file
word_count: 794
---

Suppose you have two clusters, one for development work and one for test work.
In the `development` cluster, your frontend developers work in a namespace called `frontend`,
and your storage developers work in a namespace called `storage`. In your `test` cluster,
developers work in the default namespace, or they create auxiliary namespaces as they
see fit. Access to the development cluster requires authentication by certificate. Access
to the test cluster requires authentication by username and password.

Create a directory named `config-exercise`. In your
`config-exercise` directory, create a file named `config-demo` with this content:

```yaml
apiVersion: v1
kind: Config
preferences: {}

clusters:
- cluster:
  name: development
- cluster:
  name: test

users:
- name: developer
- name: experimenter

contexts:
- context:
  name: dev-frontend
- context:
  name: dev-storage
- context:
  name: exp-test
```

A configuration file describes clusters, users, and contexts. Your `config-demo` file
has the framework to describe two clusters, two users, and three contexts.

Go to your `config-exercise` directory. Enter these commands to add cluster details to
your configuration file:

```shell
kubectl config --kubeconfig=config-demo set-cluster development --server=https://1.2.3.4 --certificate-authority=fake-ca-file
kubectl config --kubeconfig=config-demo set-cluster test --server=https://5.6.7.8 --insecure-skip-tls-verify
```

Add user details to your configuration file:

Storing passwords in Kubernetes client config is risky. A better alternative would be to use a credential plugin and store them separately. See: client-go credential plugins

```shell
kubectl config --kubeconfig=config-demo set-credentials developer --client-certificate=fake-cert-file --client-key=fake-key-seefile
kubectl config --kubeconfig=config-demo set-credentials experimenter --username=exp --password=some-password
```

- To delete a user you can run `kubectl --kubeconfig=config-demo config unset users.<name>`
- To remove a cluster, you can run `kubectl --kubeconfig=config-demo config unset clusters.<name>`
- To remove a context, you can run `kubectl --kubeconfig=config-demo config unset contexts.<name>`

Add context details to your configuration file:

```shell
kubectl config --kubeconfig=config-demo set-context dev-frontend --cluster=development --namespace=frontend --user=developer
kubectl config --kubeconfig=config-demo set-context dev-storage --cluster=development --namespace=storage --user=developer
kubectl config --kubeconfig=config-demo set-context exp-test --cluster=test --namespace=default --user=experimenter
```

Open your `config-demo` file to see the added details. As an alternative to opening the
`config-demo` file, you can use the `config view` command.

```shell
kubectl config --kubeconfig=config-demo view
```

The output shows the two clusters, two users, and three contexts:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority: fake-ca-file
    server: https://1.2.3.4
  name: development
- cluster:
    insecure-skip-tls-verify: true
    server: https://5.6.7.8
  name: test
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
- context:
    cluster: development
    namespace: storage
    user: developer
  name: dev-storage
- context:
    cluster: test
    namespace: default
    user: experimenter
  name: exp-test
current-context: ""
kind: Config
preferences: {}
users:
- name: developer
  user:
    client-certificate: fake-cert-file
    client-key: fake-key-file
- name: experimenter
  user:
    # Documentation note (this comment is NOT part of the command output).
    # Storing passwords in Kubernetes client config is risky.
    # A better alternative would be to use a credential plugin
    # and store the credentials separately.
    # See https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins
    password: some-password
    username: exp
```

The `fake-ca-file`, `fake-cert-file` and `fake-key-file` above are the placeholders
for the pathnames of the certificate files. You need to change these to the actual pathnames
of certificate files in your environment.

Sometimes you may want to use Base64-encoded data embedded here instead of separate
certificate files; in that case you need to add the suffix `-data` to the keys, for example,
`certificate-authority-data`, `client-certificate-data`, `client-key-data`.

Each context is a triple (cluster, user, namespace). For example, the
`dev-frontend` context says, "Use the credentials of the `developer`
user to access the `frontend` namespace of the `development` cluster".

Set the current context:

```shell
kubectl config --kubeconfig=config-demo use-context dev-frontend
```

Now whenever you enter a `kubectl` command, the action will apply to the cluster,
and namespace listed in the `dev-frontend` context. And the command will use
the credentials of the user listed in the `dev-frontend` context.

To see only the configuration information associated with
the current context, use the `--minify` flag.

```shell
kubectl config --kubeconfig=config-demo view --minify
```

The output shows configuration information associated with the `dev-frontend` context:

```yaml
apiVersion: v1
clusters:
- cluster:
    certificate-authority: fake-ca-file
    server: https://1.2.3.4
  name: development
contexts:
- context:
    cluster: development
    namespace: frontend
    user: developer
  name: dev-frontend
current-context: dev-frontend
kind: Config
preferences: {}
users:
- name: developer
  user:
    client-certificate: fake-cert-file
    client-key: fake-key-file
```

Now suppose you want to work for a while in the test cluster.

Change the current context to `exp-test`:

```shell
kubectl config --kubeconfig=config-demo use-context exp-test
```

Now any `kubectl` command you give will apply to the default namespace of
the `test` cluster. And the command will use the credentials of the user
listed in the `exp-test` context.

View configuration associated with the new current context, `exp-test`.

```shell
kubectl config --kubeconfig=config-demo view --minify
```

Finally, suppose you want to work for a while in the `storage` namespace of the
`development` cluster.

Change the current context to `dev-storage`:

```shell
kubectl config --kubeconfig=config-demo use-context dev-storage
```

View configuration associated with the new current context, `dev-storage`.

```shell
kubectl config --kubeconfig=config-demo view --minify
```
