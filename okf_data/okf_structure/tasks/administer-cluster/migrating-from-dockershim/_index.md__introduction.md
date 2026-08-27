---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/_index.md#introduction
kind: section
title: Migrating from dockershim
source: tasks/administer-cluster/migrating-from-dockershim/_index.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/
heading: null
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/_index
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/_index.md#whatsnext
word_count: 228
---

This section presents information you need to know when migrating from
dockershim to other container runtimes.

Since the announcement of dockershim deprecation
in Kubernetes 1.20, there were questions on how this will affect various workloads and Kubernetes
installations. Our Dockershim Removal FAQ is there to help you
to understand the problem better.

Dockershim was removed from Kubernetes with the release of v1.24.
If you use Docker Engine via dockershim as your container runtime and wish to upgrade to v1.24,
it is recommended that you either migrate to another runtime or find an alternative means to obtain Docker Engine support.
Check out the container runtimes
section to know your options.

The version of Kubernetes with dockershim (1.23) is out of support and the v1.24
will run out of support soon. Make sure to
report issues you encountered
with the migration so the issues can be fixed in a timely manner and your cluster would be
ready for dockershim removal. After v1.24 running out of support, you will need
to contact your Kubernetes provider for support or upgrade multiple versions at a time
if there are critical issues affecting your cluster.

Your cluster might have more than one kind of node, although this is not a common
configuration.

These tasks will help you to migrate:

* Check whether Dockershim removal affects you
* Migrating telemetry and security agents from dockershim
