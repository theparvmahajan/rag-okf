---
id: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#example-provide-prod-test-credentials-to-pods-using-secrets-provide-prod-test-creds
kind: section
title: 'Example: Provide prod/test credentials to Pods using Secrets {#provide-prod-test-creds}'
source: tasks/inject-data-application/distribute-credentials-secure.md
url: https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/
heading: 'Example: Provide prod/test credentials to Pods using Secrets {#provide-prod-test-creds}'
parent: okf-structure/tasks/inject-data-application/distribute-credentials-secure
children: []
prev_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables
next_sibling: okf-structure/tasks/inject-data-application/distribute-credentials-secure.md#whatsnext
word_count: 355
---

This example illustrates a Pod which consumes a secret containing production credentials and
another Pod which consumes a secret with test environment credentials.

1. Create a secret for prod environment credentials:

   ```shell
   kubectl create secret generic prod-db-secret --from-literal=username=produser --from-literal=password=Y4nys7f11
   ```

   The output is similar to:

   ```
   secret "prod-db-secret" created
   ```

1. Create a secret for test environment credentials.

   ```shell
   kubectl create secret generic test-db-secret --from-literal=username=testuser --from-literal=password=iluvtests
   ```

   The output is similar to:

   ```
   secret "test-db-secret" created
   ```

   
   Special characters such as `$`, `\`, `*`, `=`, and `!` will be interpreted by your
   shell) and require escaping.

   In most shells, the easiest way to escape the password is to surround it with single quotes (`'`).
   For example, if your actual password is `S!B\*d$zDsb=`, you should execute the command as follows:

   ```shell
   kubectl create secret generic dev-db-secret --from-literal=username=devuser --from-literal=password='S!B\*d$zDsb='
   ```

   You do not need to escape special characters in passwords from files (`--from-file`).
   

1. Create the Pod manifests:

   ```shell
   cat <<EOF > pod.yaml
   apiVersion: v1
   kind: List
   items:
   - kind: Pod
     apiVersion: v1
     metadata:
       name: prod-db-client-pod
       labels:
         name: prod-db-client
     spec:
       volumes:
       - name: secret-volume
         secret:
           secretName: prod-db-secret
       containers:
       - name: db-client-container
         image: myClientImage
         volumeMounts:
         - name: secret-volume
           readOnly: true
           mountPath: "/etc/secret-volume"
   - kind: Pod
     apiVersion: v1
     metadata:
       name: test-db-client-pod
       labels:
         name: test-db-client
     spec:
       volumes:
       - name: secret-volume
         secret:
           secretName: test-db-secret
       containers:
       - name: db-client-container
         image: myClientImage
         volumeMounts:
         - name: secret-volume
           readOnly: true
           mountPath: "/etc/secret-volume"
   EOF
   ```

   
   How the specs for the two Pods differ only in one field; this facilitates creating Pods
   with different capabilities from a common Pod template.
   

1. Apply all those objects on the API server by running:

   ```shell
   kubectl create -f pod.yaml
   ```

Both containers will have the following files present on their filesystems with the values
for each container's environment:

```
/etc/secret-volume/username
/etc/secret-volume/password
```

You could further simplify the base Pod specification by using two service accounts:

1. `prod-user` with the `prod-db-secret`
1. `test-user` with the `test-db-secret`

The Pod specification is shortened to:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: prod-db-client-pod
  labels:
    name: prod-db-client
spec:
  serviceAccount: prod-db-client
  containers:
  - name: db-client-container
    image: myClientImage
```

### References

- Secret
- Volume
- Pod
