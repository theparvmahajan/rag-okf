---
id: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#using-ssh-to-create-a-socks5-proxy
kind: section
title: Using ssh to create a SOCKS5 proxy
source: tasks/extend-kubernetes/socks5-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/socks5-proxy-access-api/
heading: Using ssh to create a SOCKS5 proxy
parent: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#task-context
next_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#client-configuration
word_count: 107
---

The following command starts a SOCKS5 proxy between your client machine and the remote SOCKS server:

```shell
# The SSH tunnel continues running in the foreground after you run this
ssh -D 1080 -q -N username@kubernetes-remote-server.example
```

The SOCKS5 proxy lets you connect to your cluster's API server based on the following configuration: 
* `-D 1080`: opens a SOCKS proxy on local port :1080.
* `-q`: quiet mode. Causes most warning and diagnostic messages to be suppressed.
* `-N`: Do not execute a remote command. Useful for just forwarding ports.
* `username@kubernetes-remote-server.example`: the remote SSH server behind which the Kubernetes cluster 
  is running (eg: a bastion host).
