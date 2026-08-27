---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#define-container-environment-variables-using-secret-data
kind: section
title: Define container environment variables using Secret data
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: Define container environment variables using Secret data
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-pod-that-has-access-to-the-secret-data-through-a-volume
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables
word_count: 226
---

You can consume the data in Secrets as environment variables in your
containers.

If a container already consumes a Secret in an environment variable,
a Secret update will not be seen by the container unless it is
restarted. There are third party solutions for triggering restarts when
secrets change.

### Define a container environment variable with data from a single Secret

- Define an environment variable as a key-value pair in a Secret:

  ```shell
  kubectl create secret generic backend-user --from-literal=backend-username='backend-admin'
  ```

- Assign the `backend-username` value defined in the Secret to the `SECRET_USERNAME` environment variable in the Pod specification.

  

- Create the Pod:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-single-secret-env-variable.yaml
  ```

- In your shell, display the content of `SECRET_USERNAME` container environment variable.

  ```shell
  kubectl exec -i -t env-single-secret -- /bin/sh -c 'echo $SECRET_USERNAME'
  ```

  The output is similar to:

  ```
  backend-admin
  ```

### Define container environment variables with data from multiple Secrets

- As with the previous example, create the Secrets first.

  ```shell
  kubectl create secret generic backend-user --from-literal=backend-username='backend-admin'
  kubectl create secret generic db-user --from-literal=db-username='db-admin'
  ```

- Define the environment variables in the Pod specification.

  

- Create the Pod:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-multiple-secret-env-variable.yaml
  ```

- In your shell, display the container environment variables.

  ```shell
  kubectl exec -i -t envvars-multiple-secrets -- /bin/sh -c 'env | grep _USERNAME'
  ```

  The output is similar to:

  ```
  DB_USERNAME=db-admin
  BACKEND_USERNAME=backend-admin
  ```
