---
id: okf-structure/tasks/administer-cluster/nodelocaldns.md#configuration
kind: section
title: Configuration
source: tasks/administer-cluster/nodelocaldns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/
heading: Configuration
parent: okf-structure/tasks/administer-cluster/nodelocaldns
children: []
prev_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#architecture-diagram
next_sibling: okf-structure/tasks/administer-cluster/nodelocaldns.md#stubdomains-and-upstream-server-configuration
word_count: 399
---

The local listen IP address for NodeLocal DNSCache can be any address that
can be guaranteed to not collide with any existing IP in your cluster.
It's recommended to use an address with a local scope, for example,
from the 'link-local' range '169.254.0.0/16' for IPv4 or from the
'Unique Local Address' range in IPv6 'fd00::/8'.

This feature can be enabled using the following steps:

* Prepare a manifest similar to the sample
  `nodelocaldns.yaml`
  and save it as `nodelocaldns.yaml`.

* If using IPv6, the CoreDNS configuration file needs to enclose all the IPv6 addresses
  into square brackets if used in 'IP:Port' format. 
  If you are using the sample manifest from the previous point, this will require you to modify
  the configuration line L70
  like this: "`health [__PILLAR__LOCAL__DNS__]:8080`"

* Substitute the variables in the manifest with the right values:

  ```shell
  kubedns=`kubectl get svc kube-dns -n kube-system -o jsonpath={.spec.clusterIP}`
  domain=<cluster-domain>
  localdns=<node-local-address>
  ```

  `<cluster-domain>` is "`cluster.local`" by default. `<node-local-address>` is the
  local listen IP address chosen for NodeLocal DNSCache.

  * If kube-proxy is running in IPTABLES mode:

    ``` bash
    sed -i "s/__PILLAR__LOCAL__DNS__/$localdns/g; s/__PILLAR__DNS__DOMAIN__/$domain/g; s/__PILLAR__DNS__SERVER__/$kubedns/g" nodelocaldns.yaml
    ```

    `__PILLAR__CLUSTER__DNS__` and `__PILLAR__UPSTREAM__SERVERS__` will be populated by
    the `node-local-dns` pods.
    In this mode, the `node-local-dns` pods listen on both the kube-dns service IP
    as well as `<node-local-address>`, so pods can look up DNS records using either IP address.

  * If kube-proxy is running in IPVS mode:

    ``` bash
    sed -i "s/__PILLAR__LOCAL__DNS__/$localdns/g; s/__PILLAR__DNS__DOMAIN__/$domain/g; s/,__PILLAR__DNS__SERVER__//g; s/__PILLAR__CLUSTER__DNS__/$kubedns/g" nodelocaldns.yaml
    ```

    In this mode, the `node-local-dns` pods listen only on `<node-local-address>`.
    The `node-local-dns` interface cannot bind the kube-dns cluster IP since the
    interface used for IPVS loadbalancing already uses this address.
    `__PILLAR__UPSTREAM__SERVERS__` will be populated by the node-local-dns pods.

* Run `kubectl create -f nodelocaldns.yaml`

* If using kube-proxy in IPVS mode, `--cluster-dns` flag to kubelet needs to be modified
  to use `<node-local-address>` that NodeLocal DNSCache is listening on.
  Otherwise, there is no need to modify the value of the `--cluster-dns` flag,
  since NodeLocal DNSCache listens on both the kube-dns service IP as well as
  `<node-local-address>`.

Once enabled, the `node-local-dns` Pods will run in the `kube-system` namespace
on each of the cluster nodes. This Pod runs CoreDNS
in cache mode, so all CoreDNS metrics exposed by the different plugins will
be available on a per-node basis.

You can disable this feature by removing the DaemonSet, using `kubectl delete -f <manifest>`.
You should also revert any changes you made to the kubelet configuration.
