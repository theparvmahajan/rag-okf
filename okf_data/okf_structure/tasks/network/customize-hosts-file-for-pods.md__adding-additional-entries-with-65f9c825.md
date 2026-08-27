---
id: okf-structure/tasks/network/customize-hosts-file-for-pods.md#adding-additional-entries-with-hostaliases
kind: section
title: Adding additional entries with hostAliases
source: tasks/network/customize-hosts-file-for-pods.md
url: https://kubernetes.io/docs/tasks/network/customize-hosts-file-for-pods/
heading: Adding additional entries with hostAliases
parent: okf-structure/tasks/network/customize-hosts-file-for-pods
children: []
prev_sibling: okf-structure/tasks/network/customize-hosts-file-for-pods.md#default-hosts-file-content
next_sibling: okf-structure/tasks/network/customize-hosts-file-for-pods.md#why-does-the-kubelet-manage-the-hosts-file-why-does-kubelet-manage-the-hosts-file
word_count: 144
---

In addition to the default boilerplate, you can add additional entries to the
`hosts` file.
For example: to resolve `foo.local`, `bar.local` to `127.0.0.1` and `foo.remote`,
`bar.remote` to `10.1.2.3`, you can configure HostAliases for a Pod under
`.spec.hostAliases`:

You can start a Pod with that configuration by running:

```shell
kubectl apply -f https://k8s.io/examples/service/networking/hostaliases-pod.yaml
```

```
pod/hostaliases-pod created
```

Examine a Pod's details to see its IPv4 address and its status:

```shell
kubectl get pod --output=wide
```

```
NAME                           READY     STATUS      RESTARTS   AGE       IP              NODE
hostaliases-pod                0/1       Completed   0          6s        10.200.0.5      worker0
```

The `hosts` file content looks like this:

```shell
kubectl logs hostaliases-pod
```

```
# Kubernetes-managed hosts file.
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
fe00::0	ip6-mcastprefix
fe00::1	ip6-allnodes
fe00::2	ip6-allrouters
10.200.0.5	hostaliases-pod

# Entries added by HostAliases.
127.0.0.1	foo.local	bar.local
10.1.2.3	foo.remote	bar.remote
```

with the additional entries specified at the bottom.
