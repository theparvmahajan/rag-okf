---
id: okf-structure/tasks/debug/debug-cluster/audit.md#audit-policy
kind: section
title: Audit policy
source: tasks/debug/debug-cluster/audit.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
heading: Audit policy
parent: okf-structure/tasks/debug/debug-cluster/audit
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#introduction
next_sibling: okf-structure/tasks/debug/debug-cluster/audit.md#audit-backends
word_count: 278
---

Audit policy defines rules about what events should be recorded and what data
they should include. The audit policy object structure is defined in the
`audit.k8s.io` API group.
When an event is processed, it's
compared against the list of rules in order. The first matching rule sets the
_audit level_ of the event. The defined audit levels are:

- `None` - don't log events that match this rule.
- `Metadata` - log events with metadata (requesting user, timestamp, resource,
  verb, etc.) but not request or response body.
- `Request` - log events with request metadata and body but not response body.
  This does not apply for non-resource requests.
- `RequestResponse` - log events with request metadata, request body and response body.
  This does not apply for non-resource requests.

You can pass a file with the policy to `kube-apiserver`
using the `--audit-policy-file` flag. If the flag is omitted, no events are logged.
Note that the `rules` field __must__ be provided in the audit policy file.
A policy with no (0) rules is treated as illegal.

Below is an example audit policy file:

You can use a minimal audit policy file to log all requests at the `Metadata` level:

```yaml
# Log all requests at the Metadata level.
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
```

If you're crafting your own audit profile, you can use the audit profile for Google Container-Optimized OS as a starting point. You can check the
configure-helper.sh
script, which generates an audit policy file. You can see most of the audit policy file by looking directly at the script.

You can also refer to the `Policy` configuration reference
for details about the fields defined.
