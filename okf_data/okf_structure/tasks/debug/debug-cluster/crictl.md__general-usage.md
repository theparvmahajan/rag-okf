---
id: okf-structure/tasks/debug/debug-cluster/crictl.md#general-usage
kind: section
title: General usage
source: tasks/debug/debug-cluster/crictl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/
heading: General usage
parent: okf-structure/tasks/debug/debug-cluster/crictl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/crictl.md#installing-crictl
next_sibling: okf-structure/tasks/debug/debug-cluster/crictl.md#example-crictl-commands
word_count: 176
---

The `crictl` command has several subcommands and runtime flags. Use
`crictl help` or `crictl <subcommand> help` for more details.

You can set the endpoint for `crictl` by doing one of the following:

* Set the `--runtime-endpoint` and `--image-endpoint` flags.
* Set the `CONTAINER_RUNTIME_ENDPOINT` and `IMAGE_SERVICE_ENDPOINT` environment
  variables.
* Set the endpoint in the configuration file `/etc/crictl.yaml`. To specify a
  different file, use the `--config=PATH_TO_FILE` flag when you run `crictl`.

If you don't set an endpoint, `crictl` attempts to connect to a list of known
endpoints, which might result in an impact to performance.

You can also specify timeout values when connecting to the server and enable or
disable debugging, by specifying `timeout` or `debug` values in the configuration
file or using the `--timeout` and `--debug` command-line flags.

To view or edit the current configuration, view or edit the contents of
`/etc/crictl.yaml`. For example, the configuration when using the `containerd`
container runtime would be similar to this:

```
runtime-endpoint: unix:///var/run/containerd/containerd.sock
image-endpoint: unix:///var/run/containerd/containerd.sock
timeout: 10
debug: true
```

To learn more about `crictl`, refer to the `crictl`
documentation.
