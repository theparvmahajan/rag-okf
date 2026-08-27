---
id: okf-structure/tasks/administer-cluster/dns-debugging-resolution.md#known-issues
kind: section
title: Known issues
source: tasks/administer-cluster/dns-debugging-resolution.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/
heading: Known issues
parent: okf-structure/tasks/administer-cluster/dns-debugging-resolution
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-debugging-resolution.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/dns-debugging-resolution.md#whatsnext
word_count: 216
---

Some Linux distributions (e.g. Ubuntu) use a local DNS resolver by default (systemd-resolved).
Systemd-resolved moves and replaces `/etc/resolv.conf` with a stub file that can cause a fatal forwarding
loop when resolving names in upstream servers. This can be fixed manually by using kubelet's `--resolv-conf` flag
to point to the correct `resolv.conf` (With `systemd-resolved`, this is `/run/systemd/resolve/resolv.conf`).
kubeadm automatically detects `systemd-resolved`, and adjusts the kubelet flags accordingly.

Kubernetes installs do not configure the nodes' `resolv.conf` files to use the
cluster DNS by default, because that process is inherently distribution-specific.
This should probably be implemented eventually.

Linux's libc (a.k.a. glibc) has a limit for the DNS `nameserver` records to 3 by
default and Kubernetes needs to consume 1 `nameserver` record. This means that
if a local installation already uses 3 `nameserver`s, some of those entries will
be lost. To work around this limit, the node can run `dnsmasq`, which will
provide more `nameserver` entries. You can also use kubelet's `--resolv-conf`
flag.

If you are using Alpine version 3.17 or earlier as your base image, DNS may not
work properly due to a design issue with Alpine. 
Until musl version 1.24 didn't include TCP fallback to the DNS stub resolver meaning any DNS call above 512 bytes would fail.
Please upgrade your images to Alpine version 3.18 or above.
