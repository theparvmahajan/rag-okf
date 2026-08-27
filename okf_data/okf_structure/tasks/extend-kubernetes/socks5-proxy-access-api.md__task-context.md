---
id: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#task-context
kind: section
title: Task context
source: tasks/extend-kubernetes/socks5-proxy-access-api.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/socks5-proxy-access-api/
heading: Task context
parent: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubernetes/socks5-proxy-access-api.md#using-ssh-to-create-a-socks5-proxy
word_count: 182
---

This example tunnels traffic using SSH, with the SSH client and server acting as a SOCKS proxy.
You can instead use any other kind of SOCKS5 proxies.

Figure 1 represents what you're going to achieve in this task.

* You have a client computer, referred to as local in the steps ahead, from where you're going to create requests to talk to the Kubernetes API.
* The Kubernetes server/API is hosted on a remote server.
* You will use SSH client and server software to create a secure SOCKS5 tunnel between the local and
  the remote server. The HTTPS traffic between the client and the Kubernetes API will flow over the SOCKS5
  tunnel, which is itself tunnelled over SSH.

graph LR;

  subgraph local[Local client machine]
  client([client])-. local  traffic .->  local_ssh[Local SSH  SOCKS5 proxy];
  end
  local_ssh[SSH SOCKS5  proxy]-- SSH Tunnel -->sshd
  
  subgraph remote[Remote server]
  sshd[SSH  server]-- local traffic -->service1;
  end
  client([client])-. proxied HTTPs traffic  going through the proxy .->service1[Kubernetes API];

  classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
  classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
  classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
  class ingress,service1,service2,pod1,pod2,pod3,pod4 k8s;
  class client plain;
  class cluster cluster;

Figure 1. SOCKS5 tutorial components
