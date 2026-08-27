---
id: okf-structure/concepts/cluster-administration/flow-control.md#health-check-concurrency-exemption
kind: section
title: Health check concurrency exemption
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Health check concurrency exemption
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#defaults
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#observability
word_count: 129
---

The suggested configuration gives no special treatment to the health
check requests on kube-apiservers from their local kubelets --- which
tend to use the secured port but supply no credentials. With the
suggested config, these requests get assigned to the `global-default`
FlowSchema and the corresponding `global-default` priority level,
where other traffic can crowd them out.

If you add the following additional FlowSchema, this exempts those
requests from rate limiting.

Making this change also allows any hostile party to then send
health-check requests that match this FlowSchema, at any volume they
like. If you have a web traffic filter or similar external security
mechanism to protect your cluster's API server from general internet
traffic, you can configure rules to block any health check requests
that originate from outside your cluster.
