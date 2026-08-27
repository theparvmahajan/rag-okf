---
id: okf-structure/tasks/administer-cluster/ip-masq-agent.md#create-an-ip-masq-agent
kind: section
title: Create an ip-masq-agent
source: tasks/administer-cluster/ip-masq-agent.md
url: https://kubernetes.io/docs/tasks/administer-cluster/ip-masq-agent/
heading: Create an ip-masq-agent
parent: okf-structure/tasks/administer-cluster/ip-masq-agent
children: []
prev_sibling: okf-structure/tasks/administer-cluster/ip-masq-agent.md#ip-masquerade-agent-user-guide
next_sibling: null
word_count: 317
---

To create an ip-masq-agent, run the following kubectl command:

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/ip-masq-agent/master/ip-masq-agent.yaml
```

You must also apply the appropriate node label to any nodes in your cluster that you want the
agent to run on.

```shell
kubectl label nodes my-node node.kubernetes.io/masq-agent-ds-ready=true
```

More information can be found in the ip-masq-agent documentation here.

In most cases, the default set of rules should be sufficient; however, if this is not the case
for your cluster, you can create and apply a
ConfigMap to customize the IP
ranges that are affected. For example, to allow
only 10.0.0.0/8 to be considered by the ip-masq-agent, you can create the following
ConfigMap in a file called
"config".

It is important that the file is called config since, by default, that will be used as the key
for lookup by the `ip-masq-agent`:

```yaml
nonMasqueradeCIDRs:
  - 10.0.0.0/8
resyncInterval: 60s
```

Run the following command to add the configmap to your cluster:

```shell
kubectl create configmap ip-masq-agent --from-file=config --namespace=kube-system
```

This will update a file located at `/etc/config/ip-masq-agent` which is periodically checked
every `resyncInterval` and applied to the cluster node.
After the resync interval has expired, you should see the iptables rules reflect your changes:

```shell
iptables -t nat -L IP-MASQ-AGENT
```

```none
Chain IP-MASQ-AGENT (1 references)
target     prot opt source               destination
RETURN     all  --  anywhere             169.254.0.0/16       /* ip-masq-agent: cluster-local traffic should not be subject to MASQUERADE */ ADDRTYPE match dst-type !LOCAL
RETURN     all  --  anywhere             10.0.0.0/8           /* ip-masq-agent: cluster-local
MASQUERADE  all  --  anywhere             anywhere             /* ip-masq-agent: outbound traffic should be subject to MASQUERADE (this match must come after cluster-local CIDR matches) */ ADDRTYPE match dst-type !LOCAL
```

By default, the link local range (169.254.0.0/16) is also handled by the ip-masq agent, which
sets up the appropriate iptables rules. To have the ip-masq-agent ignore link local, you can
set `masqLinkLocal` to true in the ConfigMap.

```yaml
nonMasqueradeCIDRs:
  - 10.0.0.0/8
resyncInterval: 60s
masqLinkLocal: true
```
