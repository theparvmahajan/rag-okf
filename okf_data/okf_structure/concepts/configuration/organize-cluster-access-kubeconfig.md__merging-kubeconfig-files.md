---
id: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#merging-kubeconfig-files
kind: section
title: Merging kubeconfig files
source: concepts/configuration/organize-cluster-access-kubeconfig.md
url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
heading: Merging kubeconfig files
parent: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig
children: []
prev_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#the-kubeconfig-environment-variable
next_sibling: okf-structure/concepts/configuration/organize-cluster-access-kubeconfig.md#file-references
word_count: 456
---

To see your configuration, enter this command:

```shell
kubectl config view
```

As described previously, the output might be from a single kubeconfig file,
or it might be the result of merging several kubeconfig files.

Here are the rules that `kubectl` uses when it merges kubeconfig files:

1. If the `--kubeconfig` flag is set, use only the specified file. Do not merge.
   Only one instance of this flag is allowed.

   Otherwise, if the `KUBECONFIG` environment variable is set, use it as a
   list of files that should be merged.
   Merge the files listed in the `KUBECONFIG` environment variable
   according to these rules:

   * Ignore empty filenames.
   * Produce errors for files with content that cannot be deserialized.
   * The first file to set a particular value or map key wins.
   * Never change the value or map key.
     Example: Preserve the context of the first file to set `current-context`.
     Example: If two files specify a `red-user`, use only values from the first file's `red-user`.
     Even if the second file has non-conflicting entries under `red-user`, discard them.

   For an example of setting the `KUBECONFIG` environment variable, see
   Setting the KUBECONFIG environment variable.

   Otherwise, use the default kubeconfig file, `$HOME/.kube/config`, with no merging.

1. Determine the context to use based on the first hit in this chain:

    1. Use the `--context` command-line flag if it exists.
    1. Use the `current-context` from the merged kubeconfig files.

   An empty context is allowed at this point.

1. Determine the cluster and user. At this point, there might or might not be a context.
   Determine the cluster and user based on the first hit in this chain,
   which is run twice: once for user and once for cluster:

   1. Use a command-line flag if it exists: `--user` or `--cluster`.
   1. If the context is non-empty, take the user or cluster from the context.

   The user and cluster can be empty at this point.

1. Determine the actual cluster information to use. At this point, there might or
   might not be cluster information.
   Build each piece of the cluster information based on this chain; the first hit wins:

   1. Use command line flags if they exist: `--server`, `--certificate-authority`, `--insecure-skip-tls-verify`.
   1. If any cluster information attributes exist from the merged kubeconfig files, use them.
   1. If there is no server location, fail.

1. Determine the actual user information to use. Build user information using the same
   rules as cluster information, except allow only one authentication
   technique per user:

   1. Use command line flags if they exist: `--client-certificate`, `--client-key`, `--username`, `--password`, `--token`.
   1. Use the `user` fields from the merged kubeconfig files.
   1. If there are two conflicting techniques, fail.

1. For any information still missing, use default values and potentially
   prompt for authentication information.
