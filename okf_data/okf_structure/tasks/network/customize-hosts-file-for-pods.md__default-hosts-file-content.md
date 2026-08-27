---
id: okf-structure/tasks/network/customize-hosts-file-for-pods.md#default-hosts-file-content
kind: section
title: Default hosts file content
source: tasks/network/customize-hosts-file-for-pods.md
url: https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/
heading: Default hosts file content
parent: okf-structure/tasks/network/customize-hosts-file-for-pods
children: []
prev_sibling: okf-structure/tasks/network/customize-hosts-file-for-pods.md#introduction
next_sibling: okf-structure/tasks/network/customize-hosts-file-for-pods.md#adding-additional-entries-with-hostaliases
word_count: 102
---

Start an Nginx Pod which is assigned a Pod IP:

```shell
kubectl run nginx --image nginx
```

```
pod/nginx created
```

Examine a Pod IP:

```shell
kubectl get pods --output=wide
```

```
NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
nginx    1/1       Running   0          13s    10.200.0.4   worker0
```

The hosts file content would look like this:

```shell
kubectl exec nginx -- cat /etc/hosts
```

```
# Kubernetes-managed hosts file.
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
fe00::0	ip6-mcastprefix
fe00::1	ip6-allnodes
fe00::2	ip6-allrouters
10.200.0.4	nginx
```

By default, the `hosts` file only includes IPv4 and IPv6 boilerplates like
`localhost` and its own hostname.
