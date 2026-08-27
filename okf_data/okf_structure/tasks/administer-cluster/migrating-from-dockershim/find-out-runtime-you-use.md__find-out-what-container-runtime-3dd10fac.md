---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#find-out-what-container-runtime-endpoint-you-use-which-endpoint
kind: section
title: Find out what container runtime endpoint you use {#which-endpoint}
source: tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/
heading: Find out what container runtime endpoint you use {#which-endpoint}
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#find-out-the-container-runtime-used-on-a-node
next_sibling: null
word_count: 272
---

The container runtime talks to the kubelet over a Unix socket using the CRI
protocol, which is based on the gRPC
framework. The kubelet acts as a client, and the runtime acts as the server.
In some cases, you might find it useful to know which socket your nodes use. For
example, with the removal of dockershim in Kubernetes v1.24 and later, you might
want to know whether you use Docker Engine with dockershim.

If you currently use Docker Engine in your nodes with `cri-dockerd`, you aren't
affected by the dockershim removal.

You can check which socket you use by checking the kubelet configuration on your
nodes.

1.  Read the starting commands for the kubelet process:

    ```
    tr \\0 ' ' < /proc/"$(pgrep kubelet)"/cmdline
    ```
    If you don't have `tr` or `pgrep`, check the command line for the kubelet
    process manually.

1.  In the output, look for the `--container-runtime` flag and the
    `--container-runtime-endpoint` flag.

    *   If your nodes use Kubernetes v1.23 and earlier and these flags aren't
        present or if the `--container-runtime` flag is not `remote`,
        you use the dockershim socket with Docker Engine. The `--container-runtime` command line
        argument is not available in Kubernetes v1.27 and later.
    *   If the `--container-runtime-endpoint` flag is present, check the socket
        name to find out which runtime you use. For example,
        `unix:///run/containerd/containerd.sock` is the containerd endpoint.

If you want to change the Container Runtime on a Node from Docker Engine to containerd,
you can find out more information on migrating from Docker Engine to  containerd,
or, if you want to continue using Docker Engine in Kubernetes v1.24 and later, migrate to a
CRI-compatible adapter like `cri-dockerd`.
