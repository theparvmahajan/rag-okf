---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors.md#an-example-containerd-configuration-file
kind: section
title: An example containerd configuration file
source: tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/
heading: An example containerd configuration file
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors.md#about-the-incompatible-cni-versions-and-failed-to-destroy-network-for-sandbox-errors
next_sibling: null
word_count: 258
---

The following example shows a configuration for `containerd` runtime v1.6.x,
which supports a recent version of the CNI specification (v1.0.0).

Please see the documentation from your plugin and networking provider for
further instructions on configuring your system.

On Kubernetes, containerd runtime adds a loopback interface, `lo`, to pods as a
default behavior. The containerd runtime configures the loopback interface via a
CNI plugin, `loopback`. The `loopback` plugin is distributed as part of the
`containerd` release packages that have the `cni` designation. `containerd`
v1.6.0 and later includes a CNI v1.0.0-compatible loopback plugin as well as
other default CNI plugins. The configuration for the loopback plugin is done
internally by containerd, and is set to use CNI v1.0.0. This also means that the
version of the `loopback` plugin must be v1.0.0 or later when this newer version
`containerd` is started.

The following bash command generates an example CNI config. Here, the 1.0.0
value for the config version is assigned to the `cniVersion` field for use when
`containerd` invokes the CNI bridge plugin.

```bash
cat << EOF | tee /etc/cni/net.d/10-containerd-net.conflist
{
 "cniVersion": "1.0.0",
 "name": "containerd-net",
 "plugins": [
   {
     "type": "bridge",
     "bridge": "cni0",
     "isGateway": true,
     "ipMasq": true,
     "promiscMode": true,
     "ipam": {
       "type": "host-local",
       "ranges": [
         [{
           "subnet": "10.88.0.0/16"
         }],
         [{
           "subnet": "2001:db8:4860::/64"
         }]
       ],
       "routes": [
         { "dst": "0.0.0.0/0" },
         { "dst": "::/0" }
       ]
     }
   },
   {
     "type": "portmap",
     "capabilities": {"portMappings": true},
     "externalSetMarkChain": "KUBE-MARK-MASQ"
   }
 ]
}
EOF
```

Update the IP address ranges in the preceding example with ones that are based
on your use case and network addressing plan.
