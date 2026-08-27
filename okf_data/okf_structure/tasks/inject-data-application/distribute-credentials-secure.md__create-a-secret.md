---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-secret
kind: section
title: Create a Secret
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: Create a Secret
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#prerequisites
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-pod-that-has-access-to-the-secret-data-through-a-volume
word_count: 144
---

Here is a configuration file you can use to create a Secret that holds your
username and password:

1. Create the Secret

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/secret.yaml
   ```

1. View information about the Secret:

   ```shell
   kubectl get secret test-secret
   ```

   Output:

   ```
   NAME          TYPE      DATA      AGE
   test-secret   Opaque    2         1m
   ```

1. View more detailed information about the Secret:

   ```shell
   kubectl describe secret test-secret
   ```

   Output:

   ```
   Name:       test-secret
   Namespace:  default
   Labels:     <none>
   Annotations:    <none>

   Type:   Opaque

   Data
   ====
   password:   13 bytes
   username:   7 bytes
   ```

### Create a Secret directly with kubectl

If you want to skip the Base64 encoding step, you can create the
same Secret using the `kubectl create secret` command. For example:

```shell
kubectl create secret generic test-secret --from-literal='username=my-app' --from-literal='password=39528$vdg7Jb'
```

This is more convenient. The detailed approach shown earlier runs
through each step explicitly to demonstrate what is happening.
