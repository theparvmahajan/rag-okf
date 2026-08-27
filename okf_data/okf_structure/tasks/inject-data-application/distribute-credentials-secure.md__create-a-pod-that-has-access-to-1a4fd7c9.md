---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-pod-that-has-access-to-the-secret-data-through-a-volume
kind: section
title: Create a Pod that has access to the secret data through a Volume
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: Create a Pod that has access to the secret data through a Volume
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#create-a-secret
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#define-container-environment-variables-using-secret-data
word_count: 526
---

Here is a configuration file you can use to create a Pod:

1. Create the Pod:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/secret-pod.yaml
   ```

1. Verify that your Pod is running:

   ```shell
   kubectl get pod secret-test-pod
   ```

   Output:

   ```
   NAME              READY     STATUS    RESTARTS   AGE
   secret-test-pod   1/1       Running   0          42m
   ```

1. Get a shell into the Container that is running in your Pod:

   ```shell
   kubectl exec -i -t secret-test-pod -- /bin/bash
   ```

1. The secret data is exposed to the Container through a Volume mounted under
   `/etc/secret-volume`.

   In your shell, list the files in the `/etc/secret-volume` directory:

   ```shell
   # Run this in the shell inside the container
   ls /etc/secret-volume
   ```

   The output shows two files, one for each piece of secret data:

   ```
   password username
   ```

1. In your shell, display the contents of the `username` and `password` files:

   ```shell
   # Run this in the shell inside the container
   echo "$( cat /etc/secret-volume/username )"
   echo "$( cat /etc/secret-volume/password )"
   ```

   The output is your username and password:

   ```
   my-app
   39528$vdg7Jb
   ```

Modify your image or command line so that the program looks for files in the
`mountPath` directory. Each key in the Secret `data` map becomes a file name
in this directory.

### Project Secret keys to specific file paths

You can also control the paths within the volume where Secret keys are projected. Use the
`.spec.volumes[].secret.items` field to change the target path of each key:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      items:
      - key: username
        path: my-group/my-username
```

When you deploy this Pod, the following happens:

- The `username` key from `mysecret` is available to the container at the path
  `/etc/foo/my-group/my-username` instead of at `/etc/foo/username`.
- The `password` key from that Secret object is not projected.

If you list keys explicitly using `.spec.volumes[].secret.items`, consider the
following:

- Only keys specified in `items` are projected.
- To consume all keys from the Secret, all of them must be listed in the
  `items` field.
- All listed keys must exist in the corresponding Secret. Otherwise, the volume
  is not created.

### Set POSIX permissions for Secret keys

You can set the POSIX file access permission bits for a single Secret key.
If you don't specify any permissions, `0644` is used by default.
You can also set a default POSIX file mode for the entire Secret volume, and
you can override per key if needed.

For example, you can specify a default mode like this:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      defaultMode: 0400
```

The Secret is mounted on `/etc/foo`; all the files created by the
secret volume mount have permission `0400`.

If you're defining a Pod or a Pod template using JSON, beware that the JSON
specification doesn't support octal literals for numbers because JSON considers
`0400` to be the _decimal_ value `400`. In JSON, use decimal values for the
`defaultMode` instead. If you're writing YAML, you can write the `defaultMode`
in octal.
