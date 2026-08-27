---
id: okf-structure/concepts/cluster-administration/system-logs.md#log-query
kind: section
title: Log query
source: concepts/cluster-administration/system-logs.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-logs/
heading: Log query
parent: okf-structure/concepts/cluster-administration/system-logs
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-logs.md#klog
next_sibling: okf-structure/concepts/cluster-administration/system-logs.md#whatsnext
word_count: 473
---

The Log Query feature can help debugging issues in both Linux and Windows 
nodes. Introduced in Kubernetes v1.27, the feature allows viewing logs of 
services running on the node. To use the feature, ensure that the kubelet 
configuration options `enableSystemLogHandler` and `enableSystemLogQuery` 
are both set to _true_ for the target node.

In Kubernetes v1.36 this feature graduated to stable and the `NodeLogQuery`feature gate 
is now locked to _true_, hence the feature gate is enabled by default, leaving
`enableSystemLogHandler` as the only option required to enable or disable the
Log Query feature. 

`enableSystemLogHandler` defaults to _false_ and is recommended to be left 
disabled unless actively debugging.

Granting permissions to `nodes/proxy` (even just **get** permission) also
authorizes access to powerful kubelet APIs that can be used to execute commands
in any container running on the node, so be careful about how you manage them.
See Kubelet authentication/authorization
for more information.

On Linux, the assumption is that service logs are available via _journald_. On 
Windows the assumption is that service logs are available in the application log
provider. On both operating systems, logs are also available by reading files
within `/var/log/`.

Provided you are authorized to interact with node objects, you can try out this feature on all your nodes or
just a subset. Here is an example to retrieve the kubelet service logs from a node:

```shell
# Fetch kubelet logs from a node named node-1.example
kubectl get --raw "/api/v1/nodes/node-1.example/proxy/logs/?query=kubelet"
```

You can also fetch files, provided that the files are in a directory that the kubelet allows for log
fetches. For example, you can fetch a log from `/var/log` on a Linux node:

```shell
kubectl get --raw "/api/v1/nodes/<insert-node-name-here>/proxy/logs/?query=/<insert-log-file-name-here>"
```

The kubelet uses heuristics to retrieve logs. This helps if you are not aware whether a given system service is
writing logs to the operating system's native logger like journald or to a log file in `/var/log/`. The heuristics
first checks the native logger and if that is not available attempts to retrieve the first logs from
`/var/log/<servicename>` or `/var/log/<servicename>.log` or `/var/log/<servicename>/<servicename>.log`.

The complete list of options that can be used are:

| Option      | Description                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------|
| `boot`      | boot show messages from a specific system boot                                                      |
| `pattern`   | pattern filters log entries by the provided PERL-compatible regular expression                      |
| `query`     | query specifies services(s) or files from which to return logs (required)                           |
| `sinceTime` | an RFC3339 timestamp from which to show logs (inclusive)  |
| `untilTime` | an RFC3339 timestamp until which to show logs (inclusive) |
| `tailLines` | specify how many lines from the end of the log to retrieve; the default is to fetch the whole log   |

Example of a more complex query:

```shell
# Fetch kubelet logs from a node named node-1.example that have the word "error"
kubectl get --raw "/api/v1/nodes/node-1.example/proxy/logs/?query=kubelet&pattern=error"
```
