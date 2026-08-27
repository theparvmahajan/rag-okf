---
id: okf-structure/concepts/cluster-administration/system-logs.md#klog
kind: section
title: Klog
source: concepts/cluster-administration/system-logs.md
url: https://kubernetes.io/docs/concepts/cluster-administration/system-logs/
heading: Klog
parent: okf-structure/concepts/cluster-administration/system-logs
children: []
prev_sibling: okf-structure/concepts/cluster-administration/system-logs.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/system-logs.md#log-query
word_count: 1069
---

klog is the Kubernetes logging library. klog
generates log messages for the Kubernetes system components.

Kubernetes is in the process of simplifying logging in its components.
The following klog command line flags
are deprecated
starting with Kubernetes v1.23 and removed in Kubernetes v1.26:

- `--add-dir-header`
- `--alsologtostderr`
- `--log-backtrace-at`
- `--log-dir`
- `--log-file`
- `--log-file-max-size`
- `--logtostderr`
- `--one-output`
- `--skip-headers`
- `--skip-log-headers`
- `--stderrthreshold`

Output will always be written to stderr, regardless of the output format. Output redirection is
expected to be handled by the component which invokes a Kubernetes component. This can be a POSIX
shell or a tool like systemd.

In some cases, for example a distroless container or a Windows system service, those options are
not available. Then the
`kube-log-runner`
binary can be used as wrapper around a Kubernetes component to redirect
output. A prebuilt binary is included in several Kubernetes base images under
its traditional name as `/go-runner` and as `kube-log-runner` in server and
node release archives.

This table shows how `kube-log-runner` invocations correspond to shell redirection:

| Usage                                    | POSIX shell (such as bash) | `kube-log-runner <options> <cmd>`                           |
| -----------------------------------------|----------------------------|-------------------------------------------------------------|
| Merge stderr and stdout, write to stdout | `2>&1`                     | `kube-log-runner` (default behavior)                        |
| Redirect both into log file              | `1>>/tmp/log 2>&1`         | `kube-log-runner -log-file=/tmp/log`                        |
| Copy into log file and to stdout         | `2>&1 \| tee -a /tmp/log`  | `kube-log-runner -log-file=/tmp/log -also-stdout`           |
| Redirect only stdout into log file       | `>/tmp/log`                | `kube-log-runner -log-file=/tmp/log -redirect-stderr=false` |

### Klog output

An example of the traditional klog native format:

```
I1025 00:15:15.525108       1 httplog.go:79] GET /api/v1/namespaces/kube-system/pods/metrics-server-v0.3.1-57c75779f-9p8wg: (1.512ms) 200 [pod_nanny/v0.0.0 (linux/amd64) kubernetes/$Format 10.56.1.19:51756]
```

The message string may contain line breaks:

```
I1025 00:15:15.525108       1 example.go:79] This is a message
which has a line break.
```

### Structured Logging

Migration to structured log messages is an ongoing process. Not all log messages are structured in
this version. When parsing log files, you must also handle unstructured log messages.

Log formatting and value serialization are subject to change.

Structured logging introduces a uniform structure in log messages allowing for programmatic
extraction of information. You can store and process structured logs with less effort and cost.
The code which generates a log message determines whether it uses the traditional unstructured
klog output or structured logging.

The default formatting of structured log messages is as text, with a format that is backward
compatible with traditional klog:

```
<klog header> "<message>" <key1>="<value1>" <key2>="<value2>" ...
```

Example:

```
I1025 00:15:15.525108       1 controller_utils.go:116] "Pod status updated" pod="kube-system/kubedns" status="ready"
```

Strings are quoted. Other values are formatted with
`%+v`, which may cause log messages to
continue on the next line depending on the data.

```
I1025 00:15:15.525108       1 example.go:116] "Example" data="This is text with a line break\nand \"quotation marks\"." someInt=1 someFloat=0.1 someStruct={StringField: First line,
second line.}
```

### Contextual Logging

Contextual logging builds on top of structured logging. It is primarily about
how developers use logging calls: code based on that concept is more flexible
and supports additional use cases as described in the Contextual Logging
KEP.

If developers use additional functions like `WithValues` or `WithName` in
their components, then log entries contain additional information that gets
passed into functions by their caller.

For Kubernetes , this is gated behind the `ContextualLogging`
feature gate and is
enabled by default. The infrastructure for this was added in 1.24 without
modifying components. The
`component-base/logs/example`
command demonstrates how to use the new logging calls and how a component
behaves that supports contextual logging.

```console
$ cd $GOPATH/src/k8s.io/kubernetes/staging/src/k8s.io/component-base/logs/example/cmd/
$ go run . --help
...
      --feature-gates mapStringBool  A set of key=value pairs that describe feature gates for alpha/experimental features. Options are:
                                     AllAlpha=true|false (ALPHA - default=false)
                                     AllBeta=true|false (BETA - default=false)
                                     ContextualLogging=true|false (BETA - default=true)
$ go run . --feature-gates ContextualLogging=true
...
I0222 15:13:31.645988  197901 example.go:54] "runtime" logger="example.myname" foo="bar" duration="1m0s"
I0222 15:13:31.646007  197901 example.go:55] "another runtime" logger="example" foo="bar" duration="1h0m0s" duration="1m0s"
```

The `logger` key and `foo="bar"` were added by the caller of the function
which logs the `runtime` message and `duration="1m0s"` value, without having to
modify that function.

With contextual logging disable, `WithValues` and `WithName` do nothing and log
calls go through the global klog logger. Therefore this additional information
is not in the log output anymore:

```console
$ go run . --feature-gates ContextualLogging=false
...
I0222 15:14:40.497333  198174 example.go:54] "runtime" duration="1m0s"
I0222 15:14:40.497346  198174 example.go:55] "another runtime" duration="1h0m0s" duration="1m0s"
```

### JSON log format

JSON output does not support many standard klog flags. For list of unsupported klog flags, see the
Command line tool reference.

Not all logs are guaranteed to be written in JSON format (for example, during process start).
If you intend to parse logs, make sure you can handle log lines that are not JSON as well.

Field names and JSON serialization are subject to change.

The `--logging-format=json` flag changes the format of logs from klog native format to JSON format.
Example of JSON log format (pretty printed):

```json
{
   "ts": 1580306777.04728,
   "v": 4,
   "msg": "Pod status updated",
   "pod":{
      "name": "nginx-1",
      "namespace": "default"
   },
   "status": "ready"
}
```

Keys with special meaning:

* `ts` - timestamp as Unix time (required, float)
* `v` - verbosity (only for info and not for error messages, int)
* `err` - error string (optional, string)
* `msg` - message (required, string)

List of components currently supporting JSON format:

* kube-controller-manager
* kube-apiserver
* kube-scheduler
* kubelet

### Log verbosity level

The `-v` flag controls log verbosity. Increasing the value increases the number of logged events.
Decreasing the value decreases the number of logged events.  Increasing verbosity settings logs
increasingly less severe events. A verbosity setting of 0 logs only critical events.

### Log location

There are two types of system components: those that run in a container and those
that do not run in a container. For example:

* The Kubernetes scheduler and kube-proxy run in a container.
* The kubelet and container runtime
  do not run in containers.

On machines with systemd, the kubelet and container runtime write to journald.
Otherwise, they write to `.log` files in the `/var/log` directory.
System components inside containers always write to `.log` files in the `/var/log` directory,
bypassing the default logging mechanism.
Similar to the container logs, you should rotate system component logs in the `/var/log` directory.
In Kubernetes clusters created by the `kube-up.sh` script, log rotation is configured by the `logrotate` tool.
The `logrotate` tool rotates logs daily, or once the log size is greater than 100MB.
