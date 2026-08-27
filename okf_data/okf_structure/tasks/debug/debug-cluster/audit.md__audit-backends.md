---
id: okf-structure/tasks/debug/debug-cluster/audit.md#audit-backends
kind: section
title: Audit backends
source: tasks/debug/debug-cluster/audit.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
heading: Audit backends
parent: okf-structure/tasks/debug/debug-cluster/audit
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#audit-policy
next_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#event-batching-batching
word_count: 401
---

Audit backends persist audit events to an external storage.
Out of the box, the kube-apiserver provides two backends:

- Log backend, which writes events into the filesystem
- Webhook backend, which sends events to an external HTTP API

In all cases, audit events follow a structure defined by the Kubernetes API in the
`audit.k8s.io` API group.

In case of patches, request body is a JSON array with patch operations, not a JSON object
with an appropriate Kubernetes API object. For example, the following request body is a valid patch
request to `/apis/batch/v1/namespaces/some-namespace/jobs/some-job-name`:

```json
[
  {
    "op": "replace",
    "path": "/spec/parallelism",
    "value": 0
  },
  {
    "op": "remove",
    "path": "/spec/template/spec/containers/0/terminationMessagePolicy"
  }
]
```

### Log backend

The log backend writes audit events to a file in JSONlines format.
You can configure the log audit backend using the following `kube-apiserver` flags:

- `--audit-log-path` specifies the log file path that log backend uses to write
  audit events. Not specifying this flag disables log backend. `-` means standard out
- `--audit-log-maxage` defined the maximum number of days to retain old audit log files
- `--audit-log-maxbackup` defines the maximum number of audit log files to retain
- `--audit-log-maxsize` defines the maximum size in megabytes of the audit log file before it gets rotated

If your cluster's control plane runs the kube-apiserver as a Pod, remember to mount the `hostPath`
to the location of the policy file and log file, so that audit records are persisted. For example:

```yaml
  - --audit-policy-file=/etc/kubernetes/audit-policy.yaml
  - --audit-log-path=/var/log/kubernetes/audit/audit.log
```

then mount the volumes:

```yaml
...
volumeMounts:
  - mountPath: /etc/kubernetes/audit-policy.yaml
    name: audit
    readOnly: true
  - mountPath: /var/log/kubernetes/audit/
    name: audit-log
    readOnly: false
```
and finally configure the `hostPath`:

```yaml
...
volumes:
- name: audit
  hostPath:
    path: /etc/kubernetes/audit-policy.yaml
    type: File

- name: audit-log
  hostPath:
    path: /var/log/kubernetes/audit/
    type: DirectoryOrCreate
```

### Webhook backend

The webhook audit backend sends audit events to a remote web API, which is assumed to
be a form of the Kubernetes API, including means of authentication. You can configure
a webhook audit backend using the following kube-apiserver flags:

- `--audit-webhook-config-file` specifies the path to a file with a webhook
  configuration. The webhook configuration is effectively a specialized
  kubeconfig.
- `--audit-webhook-initial-backoff` specifies the amount of time to wait after the first failed
  request before retrying. Subsequent requests are retried with exponential backoff.

The webhook config file uses the kubeconfig format to specify the remote address of
the service and credentials used to connect to it.
