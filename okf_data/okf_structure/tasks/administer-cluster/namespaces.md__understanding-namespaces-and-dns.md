---
id: okf-structure/tasks/administer-cluster/namespaces.md#understanding-namespaces-and-dns
kind: section
title: Understanding namespaces and DNS
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Understanding namespaces and DNS
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#understanding-the-motivation-for-using-namespaces
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#whatsnext
word_count: 72
---

When you create a Service, it creates a corresponding
DNS entry.
This entry is of the form `<service-name>.<namespace-name>.svc.cluster.local`, which means
that if a container uses `<service-name>` it will resolve to the service which
is local to a namespace.  This is useful for using the same configuration across
multiple namespaces such as Development, Staging and Production.  If you want to reach
across namespaces, you need to use the fully qualified domain name (FQDN).
