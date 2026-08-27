---
id: okf-structure/concepts/workloads/management.md#in-place-updates-of-resources
kind: section
title: In-place updates of resources
source: concepts/workloads/management.md
url: https://kubernetes.io/docs/concepts/workloads/management/
heading: In-place updates of resources
parent: okf-structure/concepts/workloads/management
children: []
prev_sibling: okf-structure/concepts/workloads/management.md#scaling-your-application
next_sibling: okf-structure/concepts/workloads/management.md#disruptive-updates
word_count: 252
---

Sometimes it's necessary to make narrow, non-disruptive updates to resources you've created.

### kubectl apply

It is suggested to maintain a set of configuration files in source control
(see configuration as code),
so that they can be maintained and versioned along with the code for the resources they configure.
Then, you can use `kubectl apply`
to push your configuration changes to the cluster.

This command will compare the version of the configuration that you're pushing with the previous
version and apply the changes you've made, without overwriting any automated changes to properties
you haven't specified.

```shell
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```none
deployment.apps/my-nginx configured
```

To learn more about the underlying mechanism, read server-side apply.

### kubectl edit

Alternatively, you may also update resources with `kubectl edit`:

```shell
kubectl edit deployment/my-nginx
```

This is equivalent to first `get` the resource, edit it in text editor, and then `apply` the
resource with the updated version:

```shell
kubectl get deployment my-nginx -o yaml > /tmp/nginx.yaml
vi /tmp/nginx.yaml
# do some edit, and then save the file

kubectl apply -f /tmp/nginx.yaml
deployment.apps/my-nginx configured

rm /tmp/nginx.yaml
```

This allows you to do more significant changes more easily. Note that you can specify the editor
with your `EDITOR` or `KUBE_EDITOR` environment variables.

For more information, please see kubectl edit.

### kubectl patch

You can use `kubectl patch` to update API objects in place.
This subcommand supports JSON patch,
JSON merge patch, and strategic merge patch.

See
Update API Objects in Place Using kubectl patch
for more details.
