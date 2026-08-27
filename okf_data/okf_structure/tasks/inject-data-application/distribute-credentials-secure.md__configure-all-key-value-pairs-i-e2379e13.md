---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables
kind: section
title: Configure all key-value pairs in a Secret as container environment variables
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: Configure all key-value pairs in a Secret as container environment variables
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#define-container-environment-variables-using-secret-data
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#example-provide-prod-test-credentials-to-pods-using-secrets-provide-prod-test-creds
word_count: 99
---

This functionality is available in Kubernetes v1.6 and later.

- Create a Secret containing multiple key-value pairs

  ```shell
  kubectl create secret generic test-secret --from-literal=username='my-app' --from-literal=password='39528$vdg7Jb'
  ```

- Use envFrom to define all of the Secret's data as container environment variables.
  The key from the Secret becomes the environment variable name in the Pod.

  

- Create the Pod:

  ```shell
  kubectl create -f https://k8s.io/examples/pods/inject/pod-secret-envFrom.yaml
  ```

- In your shell, display `username` and `password` container environment variables.

  ```shell
  kubectl exec -i -t envfrom-secret -- /bin/sh -c 'echo "username: $username\npassword: $password\n"'
  ```

  The output is similar to:

  ```
  username: my-app
  password: 39528$vdg7Jb
  ```
