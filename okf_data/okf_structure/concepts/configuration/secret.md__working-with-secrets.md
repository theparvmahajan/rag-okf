---
id: okf-structure/concepts/configuration/secret.md#working-with-secrets
kind: section
title: Working with Secrets
source: concepts/configuration/secret.md
url: https://kubernetes.io/docs/concepts/configuration/secret/
heading: Working with Secrets
parent: okf-structure/concepts/configuration/secret
children: []
prev_sibling: okf-structure/concepts/configuration/secret.md#types-of-secret-secret-types
next_sibling: okf-structure/concepts/configuration/secret.md#immutable-secrets-secret-immutable
word_count: 1138
---

### Creating a Secret

There are several options to create a Secret:

- Use `kubectl`
- Use a configuration file
- Use the Kustomize tool

#### Constraints on Secret names and data {#restriction-names-data}

The name of a Secret object must be a valid
DNS subdomain name.

You can specify the `data` and/or the `stringData` field when creating a
configuration file for a Secret. The `data` and the `stringData` fields are optional.
The values for all keys in the `data` field have to be base64-encoded strings.
If the conversion to base64 string is not desirable, you can choose to specify
the `stringData` field instead, which accepts arbitrary strings as values.

The keys of `data` and `stringData` must consist of alphanumeric characters,
`-`, `_` or `.`. All key-value pairs in the `stringData` field are internally
merged into the `data` field. If a key appears in both the `data` and the
`stringData` field, the value specified in the `stringData` field takes
precedence.

#### Size limit {#restriction-data-size}

Individual Secrets are limited to 1MiB in size. This is to discourage creation
of very large Secrets that could exhaust the API server and kubelet memory.
However, creation of many smaller Secrets could also exhaust memory. You can
use a resource quota to limit the
number of Secrets (or other resources) in a namespace.

### Editing a Secret

You can edit an existing Secret unless it is immutable. To
edit a Secret, use one of the following methods:

- Use `kubectl`
- Use a configuration file

You can also edit the data in a Secret using the Kustomize tool. However, this
method creates a new `Secret` object with the edited data.

Depending on how you created the Secret, as well as how the Secret is used in
your Pods, updates to existing `Secret` objects are propagated automatically to
Pods that use the data. For more information, refer to Using Secrets as files from a Pod section.

### Using a Secret

Secrets can be mounted as data volumes or exposed as
environment variables
to be used by a container in a Pod. Secrets can also be used by other parts of the
system, without being directly exposed to the Pod. For example, Secrets can hold
credentials that other parts of the system should use to interact with external
systems on your behalf.

Secret volume sources are validated to ensure that the specified object
reference actually points to an object of type Secret. Therefore, a Secret
needs to be created before any Pods that depend on it.

If the Secret cannot be fetched (perhaps because it does not exist, or
due to a temporary lack of connection to the API server) the kubelet
periodically retries running that Pod. The kubelet also reports an Event
for that Pod, including details of the problem fetching the Secret.

#### Optional Secrets {#restriction-secret-must-exist}

When you reference a Secret in a Pod, you can mark the Secret as _optional_,
such as in the following example. If an optional Secret doesn't exist,
Kubernetes ignores it.

By default, Secrets are required. None of a Pod's containers will start until
all non-optional Secrets are available.

If a Pod references a specific key in a non-optional Secret and that Secret
does exist, but is missing the named key, the Pod fails during startup.

### Using Secrets as files from a Pod {#using-secrets-as-files-from-a-pod}

If you want to access data from a Secret in a Pod, one way to do that is to
have Kubernetes make the value of that Secret be available as a file inside
the filesystem of one or more of the Pod's containers.

For instructions, refer to
Create a Pod that has access to the secret data through a Volume.

When a volume contains data from a Secret, and that Secret is updated, Kubernetes tracks
this and updates the data in the volume, using an eventually-consistent approach.

A container using a Secret as a
subPath volume mount does not receive
automated Secret updates.

The kubelet keeps a cache of the current keys and values for the Secrets that are used in
volumes for pods on that node.
You can configure the way that the kubelet detects changes from the cached values. The
`configMapAndSecretChangeDetectionStrategy` field in the
kubelet configuration controls
which strategy the kubelet uses. The default strategy is `Watch`.

Updates to Secrets can be either propagated by an API watch mechanism (the default), based on
a cache with a defined time-to-live, or polled from the cluster API server on each kubelet
synchronisation loop.

As a result, the total delay from the moment when the Secret is updated to the moment
when new keys are projected to the Pod can be as long as the kubelet sync period + cache
propagation delay, where the cache propagation delay depends on the chosen cache type
(following the same order listed in the previous paragraph, these are:
watch propagation delay, the configured cache TTL, or zero for direct polling).

### Using Secrets as environment variables

To use a Secret in an environment variable
in a Pod:

1. For each container in your Pod specification, add an environment variable
   for each Secret key that you want to use to the
   `env[].valueFrom.secretKeyRef` field.
1. Modify your image and/or command line so that the program looks for values
   in the specified environment variables.

For instructions, refer to
Define container environment variables using Secret data.

It's important to note that the range of characters allowed for environment variable
names in pods is restricted.
If any keys do not meet the rules, those keys are not made available to your container, though
the Pod is allowed to start.

### Container image pull Secrets {#using-imagepullsecrets}

If you want to fetch container images from a private repository, you need a way for
the kubelet on each node to authenticate to that repository. You can configure
_image pull Secrets_ to make this possible. These Secrets are configured at the Pod
level.

#### Using imagePullSecrets

The `imagePullSecrets` field is a list of references to Secrets in the same namespace.
You can use an `imagePullSecrets` to pass a Secret that contains a Docker (or other) image registry
password to the kubelet. The kubelet uses this information to pull a private image on behalf of your Pod.
See the PodSpec API
for more information about the `imagePullSecrets` field.

##### Manually specifying an imagePullSecret

You can learn how to specify `imagePullSecrets` from the
container images
documentation.

##### Arranging for imagePullSecrets to be automatically attached

You can manually create `imagePullSecrets`, and reference these from a ServiceAccount. Any Pods
created with that ServiceAccount or created with that ServiceAccount by default, will get their
`imagePullSecrets` field set to that of the service account.
See Add ImagePullSecrets to a service account
for a detailed explanation of that process.

### Using Secrets with static Pods {#restriction-static-pod}

You cannot use ConfigMaps or Secrets with static Pods.
